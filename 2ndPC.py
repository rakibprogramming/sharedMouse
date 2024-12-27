from pynput.mouse import Controller
import requests
from pynput import mouse
mouseC=Controller()
a=0
# f=requests.get("http://192.168.0.114:8000/command")
while True:
    try:
        f=requests.get("http://192.168.0.115:5000/get").text
        f=f[:-1]
        dx=0
        dy=0
        scr=0
        left=False
        right=False
        theList=f.split("\n")
        a=0
        for i in theList:     
            nl=eval(i)       
            dx=dx+nl[1][0]
            dy=dy+nl[1][1]
            a+=1
            if nl[0][0]:
                left=True
            if nl[0][1]:
                left=True
            scr+=nl[2]

        
        print(dx,dy,scr,left,right)
        

        
        
        mouseC.move(dx)
        if left:
            mouseC.press(mouse.Button.left)
        if not left:
            mouseC.release(mouse.Button.left)
        if right:
            mouseC.press(mouse.Button.right)
        if not right:
            mouseC.release(mouse.Button.right)
        mouseC.scroll(0,scr)
    except:
        pass
        
