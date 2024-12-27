from flask import Flask, send_file, request

app = Flask(__name__)

@app.route("/get")
def get_file():
    file_name = request.args.get("file", "command")  # Default file if none specified
    file_path = f"./serverD/{file_name}"
    
    try:
        return send_file(file_path, as_attachment=True)
        
    except FileNotFoundError:
        return "File not found", 404
@app.route("/clear")
def clear():
    open("./serverD/command","w").write("")
    

if __name__ == "__main__":
    # Replace 0.0.0.0 with your local IP address if needed
    app.run(host="0.0.0.0", port=5000, debug=True)