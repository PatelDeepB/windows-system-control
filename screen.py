from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
#from PIL import ImageGrab, Image
from PIL import Image
import io
import base64
import time
import tkinter as tk
import tkinter.ttk as ttk
import pyautogui
import sys
from mss import mss
import threading

# Deactivating security
pyautogui.FAILSAFE = 0.
input_text = None

app = Flask(__name__, template_folder='.',static_folder='static')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Default capture area
capture_area = [0, 0, 0, 0]
capture_area_for_mss = {"top": 0, "left": 0, "width": 0, "height": 0}

sleep_time_continious = 1.2 # expect for no spinners, othewise update the value from tk UI 

def set_capture_area():
    # Function to set the capture area manually
    root = tk.Tk()
    root.title("Select Capture Area")
    root.attributes("-alpha", 0.5)
    root.attributes('-fullscreen', True)
    
    canvas = tk.Canvas(root, cursor="cross", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    def on_press(event):
        # Update capture area on mouse press
        capture_area[0] = event.x
        capture_area[1] = event.y

    def on_drag(event):
        # Update capture area on mouse drag
        capture_area[2] = event.x
        capture_area[3] = event.y
        canvas.coords(rect, capture_area[0], capture_area[1], capture_area[2], capture_area[3])

    def on_release(event):
        # Close the window on mouse release
        root.destroy()
    
    canvas.bind("<ButtonPress-1>", on_press)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)

    rect = canvas.create_rectangle(0, 0, 0, 0, outline="red", width=2)

    root.mainloop()

@app.route('/')
def index():
    # Route for serving the index.html template
    return render_template('index.html') # change to index.html after testing issue# 3

def capture_screen_image(capture_area_for_mss):
    with mss() as sct:
        sct_img = sct.grab(capture_area_for_mss)
        # Convert to PIL/Pillow Image
        screenshot = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        buffer = io.BytesIO()
        screenshot.save(buffer, format="PNG", quality=100)
        screenshot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return screenshot_base64
   
# UI tk
def create_window():
    global input_text
    root = tk.Tk()
    root.title("Tkinter Application")

    # Create a frame for better organization and spacing
    frame = ttk.Frame(root, padding=20)
    frame.pack()

    ### labels
    # Create a label for better description
    label_titre = ttk.Label(frame, text="this is a sample app!", font=("Arial", 12, "bold"), foreground="red")

    # Style and packing
    label_titre.pack(pady=10)

    root.mainloop()

def run_tkinter():
    create_window()

if __name__ == '__main__':
    # Start by setting the capture area manually
    set_capture_area()

    # Create a thread to run the Tkinter main loop
    tkinter_thread = threading.Thread(target=run_tkinter)
    tkinter_thread.start()

    # Run the Flask app with SocketIO
    host_ip = "0.0.0.0"
    if len( sys.argv ) > 1:
        host_ip = sys.argv[1]
    socketio.run(app, host=host_ip, port=9000)
