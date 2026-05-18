import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarivis....")
    while True:
    #Listen for the wake word "Jarivis"
    # obtain audio from the microphone

        r = sr.Recognizer()
    

        # command = r.recognize_sphinx(audio)
        # print(command)
        # recognize speech using sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2)
            command = r.recognize_google(audio)
            print(command)
            if(command.lower() == "jarvis"):
                speak("Ya")
                # listen for command
        except Exception as e:
            print("Error; {0}".format(e))

