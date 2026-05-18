import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import pywhatkit

r = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')

#female voice
engine.setProperty('voice', voices[1].id)

#voice speed
engine.setProperty('rate', 170)

#contact dictionary
contacts = {
    "mom": "+919434411657",
    "mum": "+919434411657",
    "mother": "+919434411657"
}



# =========================
# Listen Function
# =========================
def listen():

    with sr.Microphone() as source:

        print("Listening...")

        # Reduce Noise
        r.adjust_for_ambient_noise(source, duration=1)

        # Listen Audio
        audio = r.listen(source)

    try:

        # Convert Speech To Text
        text = r.recognize_google(audio)

        print("You Said:", text)

        return text.lower()

    except sr.UnknownValueError:

        print("Could not understand audio")

        return ""

    except sr.RequestError:

        print("Internet connection issue")

        return ""


#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print("inside processCommand", c)
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
    elif c.lower().startswith("play"):
        song = c.lower()
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        webbrowser.open("https://www.google.com/search?q=news+today&oq=news+today&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORixAxjJAxiABDINCAEQABiDARixAxiABDIKCAIQABixAxiABDINCAMQABiDARixAxiABDIKCAQQABixAxiABDINCAUQABiSAxiABBiKBTIKCAYQABixAxiABDINCAcQABiDARixAxiABDIKCAgQABixAxiABDINCAkQABiDARixAxiABNIBCDIyMzdqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8")
    # -------------------------
    # WHATSAPP AUTOMATION
    # -------------------------
    elif "send message to" in c.lower():

        # Extract Contact Name
        name = c.lower().replace(
            "send message to",
            ""
        ).strip()

        print("Detected Contact:", name)

        # Check Contact Exists
        if name in contacts:
            print("inside if ")

            number = contacts[name]

            speak(f"What should I send to {name}")

            # Listen Message
            message = listen()

            if message != "":

                # Current Time
                now = time.localtime()

                hour = now.tm_hour
                minute = now.tm_min + 2

                speak("Sending message")

                # Send WhatsApp Message
                pywhatkit.sendwhatmsg(
                    number,
                    message,
                    hour,
                    minute
                )

                speak("Message sent successfully")

        else:

            speak("Contact not found")
    # -------------------------
    # TIME FEATURE
    # -------------------------
    elif "time" in c.lower():

        current_time = time.strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    # -------------------------
    # STOP JARVIS
    # -------------------------
    elif "stop" in c.lower() or "exit" in c.lower():

        speak("Goodbye Laxmi")

        exit()

    else:
        speak("Command not recognized")
        #let openAI handle the request


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
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                print(repr(word))
                print("You said: ", word)
             
                if "jarvis" in word.lower():
                    print(word)
                    
                    # listen for command
                    with sr.Microphone() as source:
                        speak("Ya")
                        time.sleep(1)
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        print(repr(command))
                        print("command ---", command)
                        processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

