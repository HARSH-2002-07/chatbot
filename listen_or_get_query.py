import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as source
with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
    audio = recognizer.listen(source)  # Capture audio

try:
    # Convert speech to text
    query = recognizer.recognize_google(audio)
    print("You said: " + query)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio")
except sr.RequestError:
    print("Could not request results, check your internet connection")
