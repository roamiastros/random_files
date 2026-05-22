import keyboard
import pyautogui
import time
import random

answers=["red","blue","yellow","green"]
pyautogui.PAUSE=0



def key(key):
    return keyboard.is_pressed(key)

class kahoot:
    def __init__(self,red,blue,yellow,green):
        self.red=red
        self.blue=blue
        self.yellow=yellow
        self.green=green
    def M_red(self):
        pyautogui.moveTo(self.red)
        pyautogui.click()
    def M_blue(self):
        pyautogui.moveTo(self.blue)
        pyautogui.click()
    def M_yellow(self):
        pyautogui.moveTo(self.yellow)
        pyautogui.click()
    def M_green(self):
        pyautogui.moveTo(self.green)
        pyautogui.click()
    def R_ans(self):
        #global choice
        choice=random.choice(answers)
        di[choice]()
        answers.remove(choice)
        

tr=kahoot((1176,296),(1677,320),(1206, 467),(1674,467))             #kahoot answer locations when you use windows to have each take up 1/4 of your screen
tl=kahoot((247,311),(735,324),(255,476),(709,465))
bl=kahoot((250,905),(739,913),(244,1072),(696,1062))
br=kahoot((1206,923),(1675,916),(1208,1073),(1691,1064))

trO={
    "red":tr.M_red,
    "blue":tr.M_blue,
    "yellow":tr.M_yellow,
    "green":tr.M_green
    }
tlO={
    "red":tl.M_red,
    "blue":tl.M_blue,
    "yellow":tl.M_yellow,
    "green":tl.M_green
    }
brO={
    "red":br.M_red,
    "blue":br.M_blue,
    "yellow":br.M_yellow,
    "green":br.M_green
    }
blO={
    "red":bl.M_red,
    "blue":bl.M_blue,
    "yellow":bl.M_yellow,
    "green":bl.M_green
    }


di=trO

while True:

    if key("q"):
        tr.M_red()                                   # if key pressed do it
        tl.M_red()
        bl.M_red()
        br.M_red()
    if key("w"):
        tr.M_blue()
        tl.M_blue()
        br.M_blue()
        bl.M_blue()
    if key("a"):
        tr.M_yellow()
        tl.M_yellow()
        br.M_yellow()
        bl.M_yellow()
    if key("s"):
        tr.M_green()
        tl.M_green()
        br.M_green()
        bl.M_green()
    if key("e"):
        di=trO
        tr.R_ans()
        di=tlO
        tl.R_ans()
        di=blO
        bl.R_ans()
        di=brO
        br.R_ans()
        answers=["red","blue","yellow","green"]
        
    if key("esc"):
        break
        quit()
    time.sleep(0.05)   