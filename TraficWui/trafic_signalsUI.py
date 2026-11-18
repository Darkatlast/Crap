import tkinter as tk
import subprocess

# Run C++ program and get output
def run_cpp(color):
    try:
        process = subprocess.Popen(
            ["./trafic_signals.exe"],  # change to ./trafic_signals on Linux/Mac
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, _ = process.communicate(input=color + "\n")
        result = output.strip()

        # Update label
        label.config(text=result)

        # Reset lights
        canvas.itemconfig(red_light, fill="grey20")
        canvas.itemconfig(yellow_light, fill="grey20")
        canvas.itemconfig(green_light, fill="grey20")

        # Light up selected
        if color == "RED":
            canvas.itemconfig(red_light, fill="red")
        elif color == "YELLOW":
            canvas.itemconfig(yellow_light, fill="yellow")
        elif color == "GREEN":
            canvas.itemconfig(green_light, fill="lime")
    except Exception as e:
        label.config(text=f"Error: {e}")

# Window setup
root = tk.Tk()
root.title("Traffic Light")
root.geometry("300x500")
root.config(bg="black")

# Title
tk.Label(root, text="Traffic Light", font=("Arial", 20, "bold"), bg="black", fg="white").pack(pady=10)

# Traffic light box
canvas = tk.Canvas(root, width=150, height=300, bg="black", highlightthickness=0)
canvas.pack(pady=10)

# Traffic light housing (rectangle)
canvas.create_rectangle(30, 10, 120, 290, outline="white", width=3)

# Lights (default grey)
red_light = canvas.create_oval(40, 20, 110, 90, fill="grey20")
yellow_light = canvas.create_oval(40, 110, 110, 180, fill="grey20")
green_light = canvas.create_oval(40, 200, 110, 270, fill="grey20")

# Buttons
frame = tk.Frame(root, bg="black")
frame.pack(pady=20)

btn_style = {"font": ("Arial", 12, "bold"), "width": 10, "relief": "raised", "bd": 3}

tk.Button(frame, text="RED", fg="red", command=lambda: run_cpp("RED"), **btn_style).grid(row=0, column=0, padx=5)
tk.Button(frame, text="YELLOW", fg="orange", command=lambda: run_cpp("YELLOW"), **btn_style).grid(row=0, column=1, padx=5)
tk.Button(frame, text="GREEN", fg="lime", command=lambda: run_cpp("GREEN"), **btn_style).grid(row=0, column=2, padx=5)

# Status label
label = tk.Label(root, text="Select a color", font=("Arial", 16, "bold"), bg="black", fg="white")
label.pack(pady=15)

root.mainloop()