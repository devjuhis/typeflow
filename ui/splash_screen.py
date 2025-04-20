import tkinter as tk
from PIL import Image, ImageTk

def create_splash_screen(app):
    app.withdraw()

    splashscreen = tk.Toplevel()
    splashscreen.overrideredirect(True)
    splashscreen.geometry("400x400")
    splashscreen.configure(bg="#1e1e1e")
    label = tk.Label(splashscreen, text="Loading TypeFlow...", font=("Arial", 16), fg="white", bg="#1e1e1e")
    label.place(relx=0.5, rely=0.7, anchor="center")
    splashscreen.update()

    try:
        image = Image.open('assets/Typeflow_logo.png')
        image = image.resize((150, 150), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(splashscreen, image=photo, bg="#1e1e1e")
        image_label.image = photo
        image_label.place(relx=0.5, rely=0.4, anchor="center") 
    except Exception as e:
        print(f"Image not found or failed to load: {e}")

    def start_bounce():
        direction = 1
        offset = 0

        def bounce():
            nonlocal direction, offset
            offset += direction
            if offset >= 10 or offset <= -10:
                direction *= -1
            image_label.place_configure(rely=0.4 + offset / 400) 
            splashscreen.after(30, bounce)

        bounce()

    start_bounce()

    def show_main_app():
        splashscreen.destroy()
        app.deiconify()

    splashscreen.after(5000, show_main_app)