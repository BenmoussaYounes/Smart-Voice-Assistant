import win32api
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
from mapping import mapping

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

assistant = GenericAssistant('intents.json', intent_methods=mapping)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone as Mic:
         recognizer.adjust_for_ambient_noise(Mic, duration=0.2)
         audio  = recognizer.listen(Mic)

         message = recognizer.recognize_google(audio)
         message = message.lower()

        assistant.request(message)

    except speech_recognition.UnknownValueError:
       recognizer = speech_recognition.Recognizer()

