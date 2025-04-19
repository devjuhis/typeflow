import keyboard
import pygame
from functions.record_audio import record_audio
from functions.transcription import transcribe_audio
from ui.main_window import status_label, app
pygame.mixer.init()

def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

is_recording = False

def wait_for_trigger_keys():
    global is_recording

    while True:

        if keyboard.is_pressed('ctrl+shift') and not is_recording:
            is_recording = True
            play_sound("sounds/on.mp3")
            app.after(0, lambda: status_label.configure(text="🎙️Recording...", text_color="lightblue"))
            audio = record_audio()

            if audio is not None:
                play_sound("sounds/off.mp3")
                app.after(0, lambda: status_label.configure(text="🧠 Transcripting..."))
                transcribe_audio(audio)
            else:
                app.after(0, lambda: status_label.configure(text="⚠️ No audio recorded", text_color="red"))

            is_recording = False
            app.after(0, lambda: status_label.configure(text="Recorder on hold", text_color="gray"))
