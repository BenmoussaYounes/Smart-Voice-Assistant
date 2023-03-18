
import win32api
import pyttsx3 as tts
import sys
import speech_recognition
import json



recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)


def create_note():
    global recognizer
    speaker.say('What you want to add to your list ?')
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Chose a file name ?")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f'note created {filename}')
                speaker.runAndWait()

        except speech_recognition.UnknownValueError :
            recognizer = speech_recognition.Recognizer()
            speaker.say("i didnt understand")
            speaker.runAndWait()


def add_todo():
    global  recognizer
    speaker.say("what task u want me to add")
    speaker.runAndWait()

    done = False
    while not done:
        try :
            with speech_recognition.Microphone() as Mic:
                recognizer.adjust_for_ambient_noise(Mic, duration=0.2)
                audio = recognizer.listen(Mic)

                note = recognizer.recognize_google(Mic)
                note = note.lower()

                speaker.say('Chose a file name')
                speaker.runAndWait()
                recognizer.adjust_for_ambient_noise(Mic, duration=0.2)
                audio = recognizer.listen(Mic)
                file_name  = recognizer.recognize_google(Mic)
                file_name = file_name.lower()

            with open(file_name, "w") as f:
             f.write(note)
             done = True
             speaker.say(f"I created the Note  ${note}")
             speaker.runAndWait()

        except speech_recognition.UnknownValueError:
           recognizer = speech_recognition.Recognizer()
           speaker.say("i didnt note understand please try again")
           speaker.runAndWait()


todolist = ["Clean the room","study for school","go shooping"]
def show_todos():
    speaker.say("The item on your list are ")
    for item in todolist:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say("Hello what you need help with ")
    speaker.runAndWait()

def exit():
    speaker.say('Good by')
    speaker.runAndWait()
    sys.exit(0)


mapping = {
    "create_note": create_note(),
    "add_todo": add_todo(),
    "exit": exit(),
    "show_todos": show_todos(),
    "greeting": hello(),
}

