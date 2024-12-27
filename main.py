from pynput import mouse
import pyautogui
global mouseLoc
mouseLoc=[]
def run_listener():
    data = []  # List to store all event data

    # Define callback functions for events
    def on_click(x, y, button, pressed):
        print(button,pressed)
        data.append(["click", x, y, str(button), pressed])# Add click data

    def on_scroll(x, y, dx, dy):
        print(dy)
        data.append(["scroll", x, y, dx, dy])  # Add scroll data

    # Create the listener
    listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
    listener.start()

    try:
        while True:
            global mouseLoc
            position = pyautogui.position()
            mouseLoc.append(position)
            
            if len(mouseLoc) > 3:
                d=mouseLoc[1][0]-position[0]
                if d**2 > 0:
                    print(d)
                mouseLoc=[]

            pass
    except KeyboardInterrupt:
        listener.stop()  
        print("Listener stopped.")

    return data  # Return the collected data

# Run the functio
events = run_listener()

