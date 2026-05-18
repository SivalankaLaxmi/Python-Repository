import speech_recognition as sr
import webbrowser
import pyttsx3
import time

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        print("Google is opening")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        print("Facebook is opening")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        print("Youtube is opening")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        print("LinkedIn is opening")
        webbrowser.open("https://linkedin.com")
    else:
        speak("Command not recognized")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
    #Listen for the wake word "Jarivis"
    # obtain audio from the microphone

        # r = sr.Recognizer()
    

        # command = r.recognize_sphinx(audio)
        # print(command)
        # recognize speech using sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                word = r.recognize_google(audio)
                print(repr(word))
                print("You said: ", word)
             
                if "jarvis" in word.lower():
                    print(word)
                    speak("Ya")
                    time.sleep(1)
                    # listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        print(repr(command))
                        print("command ---", command)
                        processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

