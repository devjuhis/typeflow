import customtkinter as ctk
import ctypes

from ui.log_window import create_log_window
from states.state import state

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("TypeFlow")
app.geometry("400x300")

myappid = 'typeflow.speech.to.text'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app.iconbitmap('./assets/Typeflow_logo.ico')

title_label = ctk.CTkLabel(app, text="TypeFlow", font=("Arial", 20))
title_label.pack(pady=15)

info_label = ctk.CTkLabel(app, text="Hold Ctrl + Shift to record", font=("Arial", 12))
info_label.pack(pady=15)

status_label = ctk.CTkLabel(app, text="Recorder on hold", text_color="gray", font=("Arial", 14))
status_label.pack(pady=10)

mode_var = ctk.StringVar(value=state.mode)

def update_mode(mode):
    state.set_mode(mode)
    if state.mode == "default":
        mode_var.set("default")
    elif state.mode == "writing_assistant":
        mode_var.set("writing_assistant")

speech_to_text_radio = ctk.CTkRadioButton(app, text="Speech to Text", variable=mode_var, value="default", command=lambda: update_mode("default"))
speech_to_text_radio.pack(pady=5)

writer_assistant_radio = ctk.CTkRadioButton(app, text="Writing Assistant", variable=mode_var, value="writing_assistant", command=lambda: update_mode("writing_assistant"))
writer_assistant_radio.pack(pady=5)

log_button = ctk.CTkButton(app, text="Open Log", command=lambda: create_log_window(app))
log_button.pack(pady=15)
