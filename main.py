import speech_recognition as sr
import sys

recognizer = sr.Recognizer()

sTText = ""

while True:
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            sTText = recognizer.recognize_google(audio)
            sTText = sTText.lower()

            print(f"Recognized: {sTText}")

            if sTText == "done":
                sys.exit("\"Done\" recognized")

    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue
