import pyttsx3
#initialise the engine
engine = pyttsx3.init()

if __name__ == '__main__':
    print("WELCOME TO MY ROBOSPEAKER - BY TANISHA")
    while True:
        txt = input("Enter text you want to speak aloud or 'quit' to exit: ")
        if txt.lower()=="quit":
            engine.say("THANKYOU, have a good day")
            engine.runAndWait()
            break
        engine.say(txt)
        engine.runAndWait()
