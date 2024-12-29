from pynput import mouse
import keyboard
import time
import pyautogui
import tkinter as tk
import socket
import threading
mouseC=mouse.Controller()
Sx,Sy=pyautogui.size()
Sx=Sx/2
espKeyChekingState=0
Sy=Sy/2
global mouseLoc
mouseLoc=[]

global data
data=[[False,False],0]
totalScroll=0

dataCount=[]
window_active = False  
running=False
counter=0
print("✨ Please enter the receiver's IP address to connect✨")
rIp=input("ip: ")
print("Running... (press esc key to start and stop sharing)")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (rIp, 3834)
def transparent_window():
    
    global window_active
    root = tk.Tk()
    root.attributes('-fullscreen', True) 
    root.attributes('-alpha', 0.01)       
    root.configure(bg="black")   
    root.config(cursor="plus")  
    root.lift()
    root.focus_force()     

    def check_and_close():

        global window_active
        if not window_active:
            root.destroy()

    while window_active:
        root.update() 
        check_and_close()

    root.mainloop()

def manage_thread():
    threading.Thread(target=transparent_window, daemon=True).start()


def run_listener():
    global sock
    global server_address
    global window_active
    global espKeyChekingState
    global running
    global counter
    global dataCount
    global totalScroll

    global data
    data=[[False,False],0]
    data[1]=0
    button_state = [False,False]
    global middle_button_pressed
    middle_button_pressed=0

    def on_click(x, y, button, pressed):
        global middle_button_pressed
        if button == mouse.Button.left:
            button_state[0] = pressed
            data[0][0]=pressed 
        elif button == mouse.Button.right:
            data[0][1] = pressed  
        elif button == mouse.Button.middle:
            middle_button_pressed+=1
    
    def on_scroll(x, y, dx, dy):
        data[1]=dy 

    listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
    listener.start()

    try:
        while True:
            key = keyboard.is_pressed('esc')
            if (key and counter < 50) or (counter > 0 and counter < 50):
                    time.sleep(0.01)
                    counter+=1

            if counter > 49:
                counter=0
            if key and counter ==1:
                
                if not running and not window_active and espKeyChekingState==0:
                    running=True
                    print("Sharing....")
                    window_active=True
                    middle_button_pressed=0
                    manage_thread()
                    espKeyChekingState=1     
                if running and not espKeyChekingState==1:
                    running=False
                    print("Sharing Stopped")
                    espKeyChekingState=0
                    window_active=False
                    middle_button_pressed=0               
            if middle_button_pressed==2:
                
                
                if not running and middle_button_pressed==2:
                    running=True
                    window_active=True
                    middle_button_pressed=0
                    manage_thread()
                if running and middle_button_pressed==2:
                    running=False
                    window_active=False
                    middle_button_pressed=0
                    
            if running:
                espKeyChekingState+=1
                
                position = pyautogui.position()

                posX=position[0]
                posY=position[1]
                leftButstate=str(data[0][0])
                rightButstate=str(data[0][1])
                mouseDistaceX=str(posX)
                mouseDistaceY=str(posY)
                totalScroll+=data[1]

                scrollCOndintion=str(totalScroll)
                scX=pyautogui.size()[0]
                scY=pyautogui.size()[1]
                theStringeToWrite=f"[[{leftButstate},{rightButstate}],[{mouseDistaceX},{mouseDistaceY}],{scrollCOndintion},[{scX},{scY}]]\n"
            
                sock.sendto(str(theStringeToWrite).encode(), server_address)
                    


                data[1]=0
            pass
    except KeyboardInterrupt:
        listener.stop()  
        print("Listener stopped.")

    return data

events = run_listener()

