from pynput.mouse import Controller
import requests
from pynput import mouse
import pyautogui
mouseC=Controller()
import socket
import time
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0 
pv=""
previusScroll=0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 3834))  
def get_local_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = "⚠️ Oops! Couldn't find your local IP. Please make sure you're connected to a network."
    try:
        s.connect(("192.168.1.1", 80)) 
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

print(f"🌍 Your local IP is: {get_local_ip()} 🌍")
print("🔗 Type this IP into the sender device to connect. Let's go!")
ps=0

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', 3834)) 
        data, addr = sock.recvfrom(1024)
        f=data.decode()
        if not f==pv:
            pv=f
            theList=eval(f)
            
            screenS=theList[3]
            dx=pyautogui.size()[0]/int(screenS[0])
            dy=pyautogui.size()[1]/int(screenS[1])
            left=theList[0][0]
            right=theList[0][1]
            scr=theList[2]
            # print(scr,previusScroll)
            mouseP=theList[1]
            mX=mouseP[0]
            mY=mouseP[1]
            

            pyautogui.moveTo(mX*dx, mY*dy)
            if left:
                mouseC.press(mouse.Button.left)
            if not left:
                mouseC.release(mouse.Button.left)
            if right:
                mouseC.press(mouse.Button.right)
            if not right:
                mouseC.release(mouse.Button.right)
            if not scr == previusScroll:
                
                theScroll=scr-previusScroll
                print(theScroll)  
                previusScroll=scr
                mouseC.scroll(0,theScroll*3)
    except:
        pass