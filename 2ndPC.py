from pynput.mouse import Controller
import requests
from pynput import mouse
import pyautogui
mouseC=Controller()
import time


# f=requests.get("http://192.168.0.114:8000/command")
while True:
    try:
        f=requests.get("http://192.168.0.114:5000/get").text
        requests.get("http://192.168.0.114:5000/clear")
        
        f=f[:-1]
        
        scr=0
        left=False
        right=False
        theList=f.split("\n")
        
        screenS=theList[0].split(",")
        dx=pyautogui.size()[0]/int(screenS[0])
        dy=pyautogui.size()[1]/int(screenS[1])
        theList=theList[1:]

        
        for i in theList:     
            nl=eval(i)       
            if nl[0][0]:
                left=True
            if nl[0][1]:
                left=True
            scr+=nl[2]
        mouseP=theList[len(theList)-1]
        mouseP=eval(mouseP)
        mX=mouseP[1][0]
        mY=mouseP[1][1]
        print(mX,mY)
        pyautogui.moveTo(mX*dx, mY*dy)
        mouseC.move((dx-(dx*2))*2,(dy-(dy*2))*2)

        if left:
            mouseC.press(mouse.Button.left)
        if not left:
            mouseC.release(mouse.Button.left)
        if right:
            mouseC.press(mouse.Button.right)
        if not right:
            mouseC.release(mouse.Button.right)
        mouseC.scroll(0,(scr)*3)
    except:
        pass
        
