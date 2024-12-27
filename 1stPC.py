from pynput import mouse
import pyautogui
global mouseLoc
mouseLoc=[]
global data
data=[[False,False],0]
cleftState=False
crightState=False
def run_listener():
    a=0
    global cleftState
    global crightState
    global data
    data=[[False,False],0]
    data[1]=0
    button_state = [False,False]


    def on_click(x, y, button, pressed):
        if button == mouse.Button.left:
            button_state[0] = pressed
            data[0][0]=pressed 
        elif button == mouse.Button.right:
            data[0][1] = pressed  
    
    def on_scroll(x, y, dx, dy):
        data[1]=dy 

    listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
    listener.start()

    try:
        while True:
            fileC=open("./serverD/command","w")            
            global mouseLoc
            position = pyautogui.position()
            mouseLoc.append(position)
            d=0
            if len(mouseLoc) > 3:
                d=mouseLoc[1][0]-position[0]
                if d**2 > 0:
                    print(d)
                mouseLoc=[]
            leftButstate=str(data[0][0])
            rightButstate=str(data[0][1])
            scrollC="0"
            if not data[1] ==0:
                print("Scrolling")
            
            mouseDistace=str(d)
            scrollCOndintion=str(data[1])
            theStringeToWrite=f"[[{leftButstate},{rightButstate},{mouseDistace}],{scrollCOndintion}]"
            fileC.write(theStringeToWrite)
            a=a+1
            print(a)


            data[1]=0
            pass
    except KeyboardInterrupt:
        listener.stop()  
        print("Listener stopped.")

    return data

events = run_listener()

