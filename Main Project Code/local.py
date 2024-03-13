import json
import requests
import time
from TTS.api import TTS
import pygame
# import os
import datetime

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# Initialize Pygame mixer
pygame.mixer.init()

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "vader"  # TODO: update this for whatever model you wish to use

def chat(messages, output_file):
    start_time = time.time()  # Record the start time
    r = requests.post(
        "http://127.0.0.1:11434/api/chat",
        json={"model": model, "messages": messages, "stream": True},
    )
    r.raise_for_status()
    output = ""
    end_time = time.time()  # Record the end time

    with open(output_file, 'a') as f:
        for line in r.iter_lines():
            body = json.loads(line)
            if "error" in body:
                raise Exception(body["error"])
            if body.get("done") is False:
                message = body.get("message", "")
                content = message.get("content", "")
                output += content
                # Write content to the file
                f.write(content)

                # Print the response as we receive it
                print(content, end="", flush=True)

        if body.get("done", False):
            message["content"] = output
            # No need to return anything as we're writing directly to the file
            return message, end_time - start_time  # Return the message and the time taken

def generate_and_play_audio(text):
    start_a= time.time()
    output_file = "output_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".wav"
    # Generate speech using TTS
    tts.tts_to_file(text=text,
                    file_path=output_file,
                    speaker_wav=["D:\\openchat\\something's-happening-i'm-not-the-jedi-i-should-be-i-want-more-and-i-know-i-shouldn't.wav"],
                    language="en",
                    split_sentences=True)
    # Load the generated audio file
    pygame.mixer.music.load(output_file)
    # Play the loaded audio file
    end_a = time.time()
    audio= end_a - start_a
    print("Audio generation and playback time:", audio)
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    end_a = time.time()
    print("Audio generation and playback time:", end_a - start_a)


def main():
    messages = []

    while True:
        user_input = input("Enter a prompt: ")
        if not user_input:
            print("Unloading the model and exiting...")
            requests.post("http://127.0.0.1:11434/api/generate", json={"model": model, "keep_alive": 0})  # Unload the model
            pygame.mixer.quit()  # End Pygame mixer
            exit()  # Exit the program

        print()
        messages.append({"role": "user", "content": user_input})
        message, time_taken = chat(messages, "output.txt")
        print("  Time taken: {:.3g} seconds".format(time_taken))  # Displaying time with first three significant figures
        messages.append(message)

        # Generate and play audio for the chat response
        generate_and_play_audio(message['content'])

        print("\n\n")

if __name__ == "__main__":
    main()
