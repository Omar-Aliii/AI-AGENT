import ctranslate2
import yaml
import platform
import pyaudio
import wave
import os
import tempfile
import threading
import time
import sys
import requests
import json
import pygame
from TTS.api import TTS
from faster_whisper import WhisperModel
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QHBoxLayout, QGroupBox
from PySide6.QtCore import Qt
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.text_splitter import CharacterTextSplitter
import datetime

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
# Initialize Pygame mixer
pygame.mixer.init()
# Initialize the RAG model
model_local = ChatOllama(model="cassie")

# Load data from a local PDF file
urls = [
    "D:\openchat\AASTMT.pdf"
]
Start_embeddings= time.time()
docs = [PyPDFLoader(url).load() for url in urls]

docs_list = [item for sublist in docs for item in sublist]

# Split data into chunks
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=3000, chunk_overlap=100)
doc_splits = text_splitter.split_documents(docs_list)

# Convert documents to Embeddings and store them
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text'),
)
retriever = vectorstore.as_retriever()
end_embeddings = time.time()
embed_time= end_embeddings - Start_embeddings
print(f"Embedding is done, Time taken:{embed_time}")
# After RAG

after_rag_template = """Answer the question based only on the following context:
{context}
Question: {question}
"""
after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
after_rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | after_rag_prompt
    | model_local
    | StrOutputParser()
)

class CheckQuantizationSupport:
    def has_cuda_device(self):
        cuda_device_count = ctranslate2.get_cuda_device_count()
        return cuda_device_count > 0

    def get_supported_quantizations_cuda(self):
        cuda_quantizations = ctranslate2.get_supported_compute_types("cuda")
        return [q for q in cuda_quantizations if q != 'int16']

    def get_supported_quantizations_cpu(self):
        cpu_quantizations = ctranslate2.get_supported_compute_types("cpu")
        return [q for q in cpu_quantizations if q != 'int16']

    def update_supported_quantizations(self):
        cpu_quantizations = self.get_supported_quantizations_cpu()
        self._update_supported_quantizations_in_config("cpu", cpu_quantizations)

        if self.has_cuda_device():
            cuda_quantizations = self.get_supported_quantizations_cuda()
            self._update_supported_quantizations_in_config("cuda", cuda_quantizations)

    def _update_supported_quantizations_in_config(self, device, quantizations):
        try:
            with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = {}

        if "supported_quantizations" not in config:
            config["supported_quantizations"] = {}

        config["supported_quantizations"][device] = quantizations

        with open("config.yaml", "w") as f:
            yaml.safe_dump(config, f, default_style="'")
        
        print(f"Updated {device} quantizations in config.yaml to: {quantizations}")

class VoiceRecorder:
    def __init__(self, window, format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024):
        self.format, self.channels, self.rate, self.chunk = format, channels, rate, chunk
        self.window = window
        self.is_recording, self.frames = False, []
        self.load_settings()

    def load_settings(self):
        try:
            with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)
                if "device_type" not in config:
                    config["device_type"] = "cpu"
                if "model_name" not in config:
                    config["model_name"] = "base.en"
                if "quantization_type" not in config:
                    config["quantization_type"] = "int8"

                self.update_model(config["model_name"], config["quantization_type"], config["device_type"])
        except FileNotFoundError:
            self.update_model("base.en", "int8", "cpu")

    def save_settings(self, model_name, quantization_type, device_type):
        try:
            with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = {}

        config["model_name"] = model_name
        config["quantization_type"] = quantization_type
        config["device_type"] = device_type

        with open("config.yaml", "w") as f:
            yaml.safe_dump(config, f)

    def update_model(self, model_name, quantization_type, device_type):
        model_str = f"ctranslate2-4you/whisper-{model_name}-ct2-{quantization_type}"
        self.model = WhisperModel(model_str, device=device_type, compute_type=quantization_type, cpu_threads=26)
        self.window.update_status(f"Model updated to {model_name} with {quantization_type} quantization on {device_type}")
        self.save_settings(model_name, quantization_type, device_type)

    def transcribe_audio(self, audio_file):
        Start_time = time.time()
        start_transcrpt = time.time()
        segments, _ = self.model.transcribe(audio_file)
        transcript = "\n".join([segment.text for segment in segments])
        end_transcript = time.time()
        Transcript_time= end_transcript - start_transcrpt        
        # Print the transcribed text
        print(f"{transcript}") 
        print("\nTime taken for Transcript: {:.3g} seconds".format(Transcript_time))
        start_rag= time.time()
        # Send transcript to RAG
        rag_response = after_rag_chain.invoke(transcript)
        end_rag = time.time()
        rag = end_rag- start_rag
        print(f"Response from RAG: {rag_response} Time taken to preform Rag:{rag}")
        print("\nTime taken to preform Rag {:.3g} seconds".format(rag))
        start_audio= time.time()

        # Generate and play audio for the RAG response
        generate_and_play_audio(rag_response)
        end_audio = time.time()
        audio= end_audio- start_audio
        end_time = time.time()
        total_time= end_time - Start_time
        print("\nTime taken to genrate total Audio: {:.3g} seconds".format(audio))
        print("\nTotal Time: {:.3g} seconds".format(total_time))
        # # Send transcript to Ollama
        # self.send_to_ollama(transcript)

        # self.window.update_status("Audio transcribed and sent to RAG and Ollama")

    def send_to_ollama(self, transcript):
        # Endpoint URL for sending messages to Ollama
        url = "http://127.0.0.1:11434/api/chat"

        # Prepare the message payload
        payload = {
            "model": "cassie",  # Update with the desired model
            "messages": [{"role": "user", "content": transcript}],
            "stream": True
        }

        try:
            start_time = time.time()
            response = requests.post(url, json=payload)
            response.raise_for_status()
            end_time = time.time()

            # Print Ollama's response
            for line in response.iter_lines():
                body = json.loads(line)
                if "error" in body:
                    raise Exception(body["error"])
                if body.get("done") is False:
                    message = body.get("message", "")
                    content = message.get("content", "")
                    
                    # print(content, end="", flush=True)
            # print(f"\nTime taken to transcribe and receive response: {end_time - start_time} seconds")
          
        except Exception as e:
            print("Error occurred while sending to Ollama:", e)

    def record_audio(self):
        self.window.update_status("Recording...")
        p = pyaudio.PyAudio()
        try:
            stream = p.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk)
            [self.frames.append(stream.read(self.chunk)) for _ in iter(lambda: self.is_recording, False)]
            stream.stop_stream()
            stream.close()
        finally:
            p.terminate()

    def save_audio(self):
        self.is_recording = False
        temp_filename = tempfile.mktemp(suffix=".wav")
        with wave.open(temp_filename, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b"".join(self.frames))

        start_time = time.time()  # Record start time
        self.transcribe_audio(temp_filename)
        end_time = time.time()  # Record end time
        time_taken = end_time - start_time  # Calculate time taken
        

        os.remove(temp_filename)
        self.frames.clear()

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            threading.Thread(target=self.record_audio).start()
            

class MyWindow(QWidget):
    def __init__(self, cuda_available=False):
        super().__init__()

        layout = QVBoxLayout(self)

        self.status_label = QLabel('', self)
        layout.addWidget(self.status_label)

        self.recorder = VoiceRecorder(self)

        try:
            with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)
                model = config.get("model_name", "base.en")
                quantization = config.get("quantization_type", "int8")
                device = config.get("device_type", "auto")
                self.supported_quantizations = config.get("supported_quantizations", {"cpu": [], "cuda": []})
        except FileNotFoundError:
            model, quantization, device = "base.en", "int8", "cpu"
            self.supported_quantizations = {"cpu": [], "cuda": []}

        self.recorder.update_model(model, quantization, device)

        for text, callback in [("Record", self.recorder.start_recording),
                               ("Stop and Copy to Clipboard", self.recorder.save_audio)]:
            button = QPushButton(text, self)
            button.clicked.connect(callback)
            layout.addWidget(button)

        settings_group = QGroupBox("Settings")
        settings_layout = QVBoxLayout()

        h_layout = QHBoxLayout()

        model_label = QLabel('Model')
        h_layout.addWidget(model_label)
        self.model_dropdown = QComboBox(self)
        self.model_dropdown.addItems(["tiny", "tiny.en", "base", "base.en", "small", "small.en", "medium", "medium.en", "large-v2"])
        h_layout.addWidget(self.model_dropdown)
        self.model_dropdown.setCurrentText(model)

        quantization_label = QLabel('Quantization')
        h_layout.addWidget(quantization_label)
        self.quantization_dropdown = QComboBox(self)
        h_layout.addWidget(self.quantization_dropdown)

        device_label = QLabel('Device')
        h_layout.addWidget(device_label)
        self.device_dropdown = QComboBox(self)

        if cuda_available:
            self.device_dropdown.addItems(["cpu", "cuda"])
        else:
            self.device_dropdown.addItems(["cpu"])

        h_layout.addWidget(self.device_dropdown)
        self.device_dropdown.setCurrentText(device)

        settings_layout.addLayout(h_layout)

        update_model_btn = QPushButton("Update Settings", self)
        update_model_btn.clicked.connect(self.update_model)
        settings_layout.addWidget(update_model_btn)

        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)

        self.setFixedSize(425, 250)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.device_dropdown.currentTextChanged.connect(self.update_quantization_options)
        self.update_quantization_options(quantization)

    def update_quantization_options(self, current_quantization):
        self.quantization_dropdown.clear()
        options = self.supported_quantizations.get(self.device_dropdown.currentText(), [])
        self.quantization_dropdown.addItems(options)
        if current_quantization in options:
            self.quantization_dropdown.setCurrentText(current_quantization)
        else:
            self.quantization_dropdown.setCurrentText("")

    def update_model(self):
        self.recorder.update_model(self.model_dropdown.currentText(), self.quantization_dropdown.currentText(), self.device_dropdown.currentText())

    def update_status(self, text):
        self.status_label.setText(text)

def generate_and_play_audio(text):
    start_a = time.time()
    output_file = "output_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".wav"
    # Generate speech using TTS
    tts.tts_to_file(text=text,
                    file_path=output_file,
                    speaker_wav=["D:\\openchat\\female_01.wav"],
                    language="en",
                    split_sentences=True)

    # Initialize Pygame mixer if not initialized
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Load the generated audio file
    pygame.mixer.music.load(output_file)
    # Play the loaded audio file
    end_a = time.time()
    audio = end_a - start_a
    # print("Audio generation and playback time:", audio)
    pygame.mixer.music.play()
    print("\nTime taken to genrate Audio: {:.3g} seconds".format(audio))

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    end_a = time.time()
    # print("Audio generation and playback time:", end_a - start_a)

def main():
    quantization_checker = CheckQuantizationSupport()
    cuda_available = quantization_checker.has_cuda_device()
    quantization_checker.update_supported_quantizations()

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyWindow(cuda_available)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
