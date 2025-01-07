import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-us')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        print(f"Error recognizing speech: {e}")
        return ""

    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(f"Received query: {query}")
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    if not query:
        print("No input received. Please try again.")
        eel.DisplayMessage("No input received. Please try again.")
        return

    try:
        if "open" in query:
            from engine.feautures import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.feautures import PlayYoutube
            PlayYoutube(query)
        else:
            from engine.feautures import chatBot
            chatBot(query)
    except Exception as e:
        print(f"Error in processing command: {e}")

    eel.ShowHood()
