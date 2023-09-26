import speech_recognition as sr 
#  for robot to listen to our voice 

import pyttsx3
#to convert text to speech
import pywhatkit
#for advance controle on browser
import datetime
import wikipedia
# to get data from wikipedia
import pyjokes
# to get jokes#     engine.say(text)
#     engine.runAndwait()

recognizer =sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)


try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand your speech.")




nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize

command = word_tokenize(text)


commands = {
    "open": "Open a file or application",
    "search": "Perform a web search",
    "tell me the time": "Display the current time",
    # Add more commands and corresponding actions
}


if command[0] in commands:
    action = commands[command[0]]
    if action == "Open a file or application":
        # Implement file/application opening logic
        # elif action == "Perform a web search":
        # Implement web search logic
    elif action == "Display the current time":
        # Implement time display logic
    # Add more actions as needed
else:
    print("Command not recognized.")



engine = pyttsx3.init()
engine.say("Here is the result of your command.")
engine.runAndWait()



while True:
    # Listen for the wake word or another trigger
    # Execute the steps mentioned above

