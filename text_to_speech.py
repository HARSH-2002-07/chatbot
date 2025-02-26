import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)

# Text to convert
text = "Hello! Welcome to the world of Python text-to-speech."

# Convert text to speech
engine.say(text)
engine.runAndWait()  # Wait for the speech to finish
