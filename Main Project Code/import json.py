from gtts import gTTS
import time
import pygame
import os

language = "en"
text = "Hello, I am a Football player" 

start_time = time.time()
speech = gTTS(text=text, lang=language, slow=False)
speech.save("textToSpeech.mp3")
end_time = time.time()

print("Time taken to generate speech:", end_time - start_time, "seconds")

# Initialize pygame mixer
pygame.mixer.init()

# Load the saved speech file
pygame.mixer.music.load("textToSpeech.mp3")

# Play the speech file
pygame.mixer.music.play()

# Wait until the audio finishes playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Stop the pygame mixer
pygame.mixer.quit()

# Delay before attempting to delete the file (1 second)
time.sleep(1)

# Check if the file exists before attempting to delete it
if os.path.exists("textToSpeech.mp3"):
    # Try to remove the file
    try:
        os.remove("textToSpeech.mp3")
        print("File removed successfully.")
    except Exception as e:
        print("Error:", e)
else:
    print("File does not exist.")
