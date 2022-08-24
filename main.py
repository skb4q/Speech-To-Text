import speech_recognition as sr
from gingerit.gingerit import GingerIt
from googletrans import Translator

recognizer = sr.Recognizer()
parser = GingerIt()
finished = False
translator = Translator()

while not finished:
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            sTText = recognizer.recognize_google(audio)

            cleanedText = parser.parse(sTText.capitalize())['result']

            if sTText.lower() == "stop":
                print("Program ending")
                finished = True
                break

            print(f"Recognized: {cleanedText}")
            translation = translator.translate(cleanedText, dest='fr')
            print(f"Translation: {translation.text}")
            bToEn = translator.translate(translation.text, dest='en')
            print(f"Back to English: {bToEn.text}")

    except Exception as e:
        if sr.UnknownValueError():
            recognizer = sr.Recognizer()
            continue
        pass
