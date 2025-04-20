import sys
import sounddevice as sd
import numpy as np
import keyboard
from functions.settings_functions import read_settings
from ui.log_window import add_log
from states.state import state

settings = read_settings()
hotkey = settings.get("hotkey", "ctrl+shift")

sample_rate = 16000

def record_audio():
    audio_chunks = []

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        audio_chunks.append(indata.copy())

    with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate, dtype='int16'):
        add_log(state.get_log_box(), "Recording started...")
        
        while True:
            if keyboard.is_pressed(hotkey):
                sd.sleep(100)
            else:
                break 

    add_log(state.get_log_box(), "Recording stopped.")
    return np.concatenate(audio_chunks, axis=0) if audio_chunks else None
