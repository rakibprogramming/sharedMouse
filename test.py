from pynput import mouse

is_remote_control_active = False

def on_click(x, y, button, pressed):
    if is_remote_control_active:
        # Block local clicks by not performing any action
        return False  # Stops further propagation
    else:
        # Allow local clicks
        print(f"Mouse clicked at ({x}, {y}) with {button}")

# Start the listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()