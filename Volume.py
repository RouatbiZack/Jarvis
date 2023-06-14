import pyautogui as p
import math, time
import re
import tkinter
root = tkinter.Tk()
root.withdraw()
def set_vol(new_volume):
    p.press('volumedown', presses = 50) #sets volume to zero
    time.sleep(0.5) #using time.sleep to space the presses 
    x = math.floor(new_volume / 2) #setting the amount of presses required
    p.press('volumeup', presses = x) #setting volume
def extract_integers(list):
    result = []
    for token in list:
        try:
            result.append(int(token))
        except ValueError:
            continue
    return result
def split_string(string, separators):
    pattern = '|'.join(map(re.escape, separators))
    return re.split(pattern, string)