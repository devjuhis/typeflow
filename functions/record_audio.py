import sys
import sounddevice as sd
import numpy as np
import keyboard

sample_rate = 16000

def record_audio():

    audio_chunks = []

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        audio_chunks.append(indata.copy())

    with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate, dtype='int16'):
        print("🎤 Tallennus käynnissä...")
        while keyboard.is_pressed('ctrl+shift'):
            sd.sleep(100)

    print("⏹️ Tallennus päättyi.")
    return np.concatenate(audio_chunks, axis=0) if audio_chunks else None
