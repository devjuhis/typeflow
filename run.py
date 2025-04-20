import threading
import tkinter as tk
from PIL import Image, ImageTk
from ui.main_window import app 
from ui.splash_screen import create_splash_screen

create_splash_screen(app)

from functions.hotkey_listener import wait_for_trigger_keys
threading.Thread(target=wait_for_trigger_keys, daemon=True).start()

app.mainloop()
