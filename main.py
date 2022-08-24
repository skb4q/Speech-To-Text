import speech_recognition as sr
from gingerit.gingerit import GingerIt
from googletrans import Translator

# Flag to stop the while loop until the user says "Stop"
finished = False

# Uses the SpeechRecognition API to record and transcribe the user's audio lines from audio input
recognizer = sr.Recognizer()

# Cleans up the speech-to-text to be as grammatically correct as the script can manage
parser = GingerIt()

# Translates the spoken English into the current selected language that the Google Trans API supports
translator = Translator()

while not finished:
    try:
        with sr.Microphone() as mic:
            yOrN = ""
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            sTText = recognizer.recognize_google(audio)

            if sTText.lower() == "stop":
                print("Program ending")
                finished = True
                break

            cleanedText = parser.parse(sTText.capitalize())['result']

            print(f"Recognized: {cleanedText}")

            print("Is this what you want to translate? Say \"Yes\" or \"No\": ")

            while yOrN.lower() != "yes" and yOrN.lower() != "no":
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                yOrN = recognizer.recognize_google(audio)

                if yOrN.lower() == "yes":
                    translation = translator.translate(cleanedText, dest='fr')
                    print(f"Translation: {translation.text}")
                    break
                elif yOrN.lower() == "no":
                    break
                else:
                    print("Sorry, I didn't catch that. \"Yes\" or \"No\"? ")

    except Exception as e:
        if sr.UnknownValueError():
            recognizer = sr.Recognizer()
            continue
        pass
