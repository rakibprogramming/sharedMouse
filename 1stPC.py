from pynput import mouse
import pyautogui
mouseC=mouse.Controller()
Sx,Sy=pyautogui.size()
Sx=Sx/2
Sy=Sy/2
global mouseLoc
mouseLoc=[]
global data
data=[[False,False],0]
cleftState=False
crightState=False
dataCount=[]

running=False

def run_listener():
    global running
    
    global dataCount
    a=0
    global cleftState
    global crightState
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
                print("Running")
                dataCount.append([data[0][:], data[1]])

                fileC=open("./serverD/command","a")            
                global mouseLoc
                position = pyautogui.position()
                mouseLoc.append(position)
                dx=0
                dy=0
                leftBC=0
                rightBC=0
                for i in dataCount:
                    if i[0][0]:
                        leftBC+=1
                    if i[0][1]:
                        rightBC+=1



                if len(mouseLoc) > 6:
                        dx=mouseLoc[1][0]-position[0]
                        dy=mouseLoc[1][1]-position[1]
                        mouseLoc=[]
                leftButstate=str(data[0][0])
                rightButstate=str(data[0][1])
                scrollC="0"
                totalPositon=dx+dy
                if(len(dataCount)>200):
                    dataCount.clear()
                if totalPositon**2 > 0 or (data[0][0] and leftBC <1) or (data[0][1] and rightBC < 1) or data[1]**2:

                    mouseDistaceX=str(dx)
                    mouseDistaceY=str(dy)

                    scrollCOndintion=str(data[1])
                    theStringeToWrite=f"[[{leftButstate},{rightButstate}],[{mouseDistaceX},{mouseDistaceY}],{scrollCOndintion}]\n"
                    fileC.write(theStringeToWrite)
                if len(dataCount) == 0:
                    mouseDistaceX=str(dx)
                    mouseDistaceY=str(dy)
                    scrollCOndintion=str(data[1])
                    theStringeToWrite=f"[[{leftButstate},{rightButstate}],[{mouseDistaceX},{mouseDistaceY}],{scrollCOndintion}]\n"
                    fileC.write(theStringeToWrite)  
             
                    


                data[1]=0
            
    except KeyboardInterrupt:
        listener.stop()  
        print("Listener stopped.")

    return data

events = run_listener()

