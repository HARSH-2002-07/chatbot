"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="you are a vitual assistant in a robotics lab in KIET group of institutions, you are professional assisstant",
)

history = []
print("Hello, how can i help you?")

while True:

  user_input = input("You: ")

  chat_session = model.start_chat(
    history= history
    )

  response = chat_session.send_message(user_input)

  model_response = response.text
  print(f'Bot: {model_response}')
  print()

history.append({"role": "user", "parts": [user_input]})
history.append({"role": "model", "parts": [model_response]})
