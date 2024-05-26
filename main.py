import os
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import pygame
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Google Generative AI API with the provided API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Print available microphone devices
print("Available microphone devices:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")

# Select the microphone device index
device_index = 1

# Use the selected microphone as the audio source
with sr.Microphone(device_index=device_index) as source:
    print("Please say something:")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Listening...")
    audio_data = recognizer.listen(source, timeout=2, phrase_time_limit=10)

# Recognize speech using Google Speech Recognition
try:
    text = recognizer.recognize_google(audio_data, language="en-in")
    spoken_text = text
    print("You said:", spoken_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response from the generative model and play it
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    full_output = ""
    for chunk in response:
        full_output += chunk.text  # Append each chunk to the full_output string
        print(full_output)
    tts = gTTS(text=full_output, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    print("Audio is playing...")

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


gemini_response = get_gemini_response(spoken_text)

