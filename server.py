from flask import Flask, send_from_directory, request
import os
import pyautogui
app = Flask(__name__)

# Store the file content in memory to avoid re-reading after the clear request
file_content_cache = None
file_path = "./serverD/command"

def read_file():
    """Helper function to read the file into memory (if needed)"""
    global file_content_cache
    if file_content_cache is None:  # Only read if cache is empty
        try:
            with open(file_path, "r") as file:
                file_content_cache = file.read()
        except FileNotFoundError:
            file_content_cache = None
    return file_content_cache

@app.route("/get")
def get_file():

    """Serve the current file content"""
    file_name = request.args.get("file", "command")  # Default file if none specified
    file_path = f"./serverD/{file_name}"
    
    try:
        # Use send_from_directory for better performance when serving files
        return send_from_directory(directory="./serverD", path=file_name, as_attachment=True)
        
    except FileNotFoundError:
        return "File not found", 404

@app.route("/clear")
def clear():

    with open(file_path, "w") as file:
        file.write(f"{pyautogui.size()[0]},{pyautogui.size()[1]}\n")  
    

    global file_content_cache
    file_content_cache = None  
    
    return "File cleared successfully", 200

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)