import pyttsx3

def Speak(text):
   
    rate = 100
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate+50)
   
    print("J.A.R.V.I.S :"+text+"\n")
    engine.say(text)
    engine.runAndWait()
   
