## Gemini Voice to Voice Bot

I am thrilled to present our Voice-to-Voice Interactive Chatbot project. This endeavor seamlessly integrates cutting-edge technologies such as Google Speech Recognition and Google Generative AI to offer a captivating chat experience driven entirely by voice interactions.

## Features
- Speech recognition for user input
- Integration with Google Generative AI for response generation
- Text-to-speech conversion for audio output

## Requirements
- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library
- Google Cloud Project with Generative AI API enabled. [Instructions](https://cloud.google.com/ai/generative-ai)
- [dotenv](https://github.com/theskumar/python-dotenv) library
- [Pygame](https://www.pygame.org/) library
- Google API Key for Generative AI. [Get API Key](https://ai.google.dev/gemini-api/docs/api-key)

## Installation
Install required libraries:
```bash
pip install speechrecognition google-generativeai gtts pygame python-dotenv
```

## Setup
1. **Get API Key from Google AI Studio**
   - Create a new file named `.env` in the root directory of the project.
   - Add the following line to the `.env` file, replacing `GOOGLE_API_KEY` with your actual API key:
     
   - ```
     GOOGLE_API_KEY = GOOGLE_API_KEY
     ```

2. **Install Required Libraries:**
   - Install the necessary Python libraries using pip:

   - ```bash
     pip install speechrecognition google-generativeai gtts pygame python-dotenv
     ```


3. **Optional: Modify Microphone Device Index:**
   - Open the `main.py` file and locate the `device_index` variable.
   - Modify the `device_index` variable to select a different microphone device if needed.

## Running the Project
1. Make sure your `.env` file is present in the project directory.
2. Run the script:

   ```bash
   python main.py
   ```

## How it Works
1. The script starts by initializing the speech recognition engine and listing available microphone devices.
2. The user selects a microphone and speaks a question.
3. The speech is recognized using Google Speech Recognition.
4. The recognized text is sent to the Generative AI model for response generation.
5. The generated response is converted to speech using Text-to-Speech and played back to the user.

## Contributing

Feel free to contribute to this project by improving the code, adding features, or fixing bugs. Your contributions are welcome!
