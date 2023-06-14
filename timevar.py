import datetime
import time
import speak
def Timevar():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak.Speak(f"the time is {strTime}")
    time.sleep(2)


