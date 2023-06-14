import time
import speech_recognition as sr
import speak
import Chatgpt
import Volume
import musicsystem
from mail2 import *
import timevar
import tkinter
music_suggest=['can you suggest some songs','do you have any music suggestions','can you play some music','do you have some music suggestions','play music','play some music']

def recog_main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        data = data.lower()
        print("You said: " + data)
        if "what is the time" in data:
            timevar.Timevar()
        elif "mute" in data :
            speak.Speak("The sound has been muted")
            Volume.set_vol(0)
        elif (("set " or "change"or "raise") and "volume") in data :
            if "max" in data :
                Volume.set_vol(100)
                speak.Speak("The volume is set to maximum")
            else :
                separators=[" ","%"]
                vol_list=Volume.split_string(data,separators)
                sound=Volume.extract_integers(vol_list)
                Volume.set_vol(sound[0])
                speak.Speak("the volume is set to "+str(sound)+"%")
        elif  "send mail" in data:
            root = tk.Tk()
            login_window(root)
            root.mainloop()
            
        elif data in music_suggest:
            speak.Speak("certainly. how are you feeling right now ?")
            with sr.Microphone() as source:
                audio=r.listen(source)
            mood=musicsystem.get_user_preferences(r.recognize_google(audio))
            
            if mood:
                playlist=musicsystem.search_playlists(mood)
                if playlist:
                    musicsystem.play_on_youtube(playlist)
                    speak.Speak("Here is a song that you might enjoy")
                else :
                    speak.Speak("there is no playlist found for your given mood ")
            else:
                speak.Speak("there is no mood given in your input")
        else:
            response=Chatgpt.generate_response(data)
            speak.Speak(response) 
        return data
    
    except sr.UnknownValueError: 
        print("Jarvis did not understand your request")
    except sr.RequestError as e: # if you get a request error from Google speech engine
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 