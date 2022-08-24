import speech_recognition as sr
from gingerit.gingerit import GingerIt

recognizer = sr.Recognizer()
parser = GingerIt()
finished = False

while not finished:
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            sTText = recognizer.recognize_google(audio)

            if sTText != "done":
                print(f"Recognized: {parser.parse(sTText)['result']}")
            else:
                finished = True

    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue
