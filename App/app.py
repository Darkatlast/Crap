from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Run C++ program and get output
def run_cpp(color):
    process = subprocess.Popen(
        ["./trafic.exe"],  # Change to ./trafic_signals on Linux/Mac
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, _ = process.communicate(input=color + "\n")
    return output.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    message = "Select a color"
    active = None
    if request.method == "POST":
        color = request.form["color"]
        message = run_cpp(color)
        active = color
    return render_template("index.html", message=message, active=active)

if __name__ == "__main__":
    app.run(debug=True)