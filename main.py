import speech_recognition as sr
import pyautogui as p
import speak
import recog
import threading
from mail2 import *
import pygame
import os.path
import time
import pyaudio
class imageHandler:
  def __init__ ( self ):
    self.pics = dict()

  def loadFromFile ( self, filename, id=None ):
    if id == None: id = filename
    self.pics [ id ] = pygame.image.load ( filename ).convert()

  def loadFromSurface ( self, surface, id ):
    self.pics [ id ] = surface.convert_alpha()

  def render ( self, surface, id, position = None, clear = False, size = None ):
    if clear == True:
      surface.fill ( (5,2,23) ) #

    if position == None:
      picX = int ( surface.get_width() / 2 - self.pics [ id ].get_width() / 2 )
    else:
      picX = position [0]
      picY = position [1]

    if size == None:
      surface.blit ( self.pics [ id ], ( picX, picY ) ) #

    else:
      surface.blit ( pygame.transform.smoothscale ( self.pics [ id ], size ), ( picX, picY ) )
      
#Initialises the display-------------------------------------------------------
pygame.display.init() # Initiates the display pygame
#screen = pygame.display.set_mode((400,400), pygame.RESIZABLE) #uncomment this line for smaller window
screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE) #allows fullscreen #comment this line out for smaller window
handler = imageHandler()

def display():
    #AI NOT SPEAKING
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/1.gif", "1" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/2.gif", "2" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/3.gif", "3" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/4.gif", "4" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/5.gif", "5" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/6.gif", "6" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/7.gif", "7" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/8.gif", "8" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/9.gif", "9" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/10.gif", "10" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/11.gif", "11" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/12.gif", "12" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/13.gif", "13" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/14.gif", "14" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/15.gif", "15" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/16.gif", "16" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/17.gif", "17" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/18.gif", "18" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/19.gif", "19" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/20.gif", "20" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/21.gif", "21" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/22.gif", "22" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/23.gif", "23" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/24.gif", "24" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/25.gif", "25" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/26.gif", "26" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/27.gif", "27" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/28.gif", "28" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/29.gif", "29" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/30.gif", "30" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/31.gif", "31" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/32.gif", "32" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/33.gif", "33" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/34.gif", "34" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/35.gif", "35" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/36.gif", "36" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/37.gif", "37" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/38.gif", "38" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/39.gif", "39" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/40.gif", "40" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/41.gif", "41" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/42.gif", "42" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/43.gif", "43" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/44.gif", "44" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/45.gif", "45" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/46.gif", "46" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/47.gif", "47" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/48.gif", "48" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/49.gif", "49" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/50.gif", "50" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/51.gif", "51" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/52.gif", "52" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/53.gif", "53" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/54.gif", "54" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/55.gif", "55" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/56.gif", "56" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/57.gif", "57" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/58.gif", "58" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/59.gif", "59" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/60.gif", "60" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/61.gif", "61" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/62.gif", "62" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/63.gif", "63" )
    # handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/64.gif", "64" )
    # #AI TALKING
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/101.gif", "101" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/102.gif", "102" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/103.gif", "103" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/104.gif", "104" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/105.gif", "105" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/106.gif", "106" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/107.gif", "107" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/108.gif", "108" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/109.gif", "109" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/110.gif", "110" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/111.gif", "111" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/112.gif", "112" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/113.gif", "113" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/114.gif", "114" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/115.gif", "115" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/116.gif", "116" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/117.gif", "117" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/118.gif", "118" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/119.gif", "119" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/120.gif", "120" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/121.gif", "121" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/122.gif", "122" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/123.gif", "123" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/124.gif", "124" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/125.gif", "125" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/126.gif", "126" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/127.gif", "127" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/128.gif", "128" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/129.gif", "129" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/130.gif", "130" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/131.gif", "131" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/132.gif", "132" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/133.gif", "133" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/134.gif", "134" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/135.gif", "135" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/136.gif", "136" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/137.gif", "137" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/138.gif", "138" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/139.gif", "139" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/140.gif", "140" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/141.gif", "141" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/142.gif", "142" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/143.gif", "143" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/144.gif", "144" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/145.gif", "145" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/146.gif", "146" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/147.gif", "147" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/148.gif", "148" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/149.gif", "149" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/150.gif", "150" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/151.gif", "151" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/152.gif", "152" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/153.gif", "153" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/154.gif", "154" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/155.gif", "155" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/156.gif", "156" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/157.gif", "157" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/158.gif", "158" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/159.gif", "159" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/160.gif", "160" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/161.gif", "161" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/162.gif", "162" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/163.gif", "163" )
    handler.loadFromFile ( "C:/Users/asus/Desktop/Workspace/Jarvis-master/Gui/164.gif", "164" )



def face():
  A = 240
  B = -5
  x = 550
  y = 550
    
  COUNT =101
  
  while True:
      
    # if TALKING== False:
    #   if COUNT>= 65:
    #     COUNT = COUNT - 100
    #   img = str(COUNT)
    #   handler.render(screen, img, ( A, B ), True, ( x, y ) )
    #   pygame.display.update(A,B,x,y)
    #   time.sleep(.03)
    #   COUNT = COUNT + 1
    #   if COUNT == 65:
    #     COUNT = 1 

    # elif TALKING==True:
      if COUNT ==100:
        COUNT = COUNT + 100
      img= str(COUNT)
      handler.render (screen, img, ( A, B ), True, ( x, y ) )
      pygame.display.update(A,B,x,y)
      time.sleep(.03)
      COUNT = COUNT + 1
      if COUNT== 165:
        COUNT=101







def Jmain() :
    r = sr.Recognizer()
    #global TALKING
    keywords = [("jarvis", 1), ("hey jarvis", 1)]
    source = sr.Microphone()

    def callback(recognizer, audio):
        try:
            speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
            print(speech_as_text)
            if "jarvis" in speech_as_text or "hey jarvis":
             
                speak.Speak("Yes sir?")
                recog.recog_main()
             
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")

    def start_recognizer():
        print("Waiting for a keyword...Jarvis or Hey Jarvis")
        r.listen_in_background(source, callback)
        time.sleep(1000000)
    start_recognizer()
Jmain()
# def main( ):
#     t1=threading.Thread(target=Jmain)
#    # t2=threading.Thread(target=face)
#     #t3=threading.Thread(target=display)
#    # t3.start()
#     #t3.join()
#     t1.start()
#    # t2.start()

# main()

