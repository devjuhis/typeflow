import os
import tempfile
import keyboard
import soundfile as sf
from faster_whisper import WhisperModel

from functions.writer import write
from ai.text_processor import process_voice_prompt
from ai.writing_assistant import writing_assistant
from states.state import state
from ui.log_window import add_log

model_size = "base"
device = "cpu"
sample_rate = 16000

model = WhisperModel(model_size, device=device, compute_type="int8")

def transcribe_audio(audio_data):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        temp_filename = tmpfile.name

    try:
        sf.write(temp_filename, audio_data, samplerate=sample_rate)

        print("🧠 Transcripting...")
        segments, _ = model.transcribe(temp_filename)

        full_text = ""
        for segment in segments:
            full_text += " " + segment.text
        
        add_log(state.get_log_box(), f"Text before processing: {full_text.strip()}")

        if "delete all" in full_text.lower() or "poista kaikki" in full_text.lower():
            add_log(state.get_log_box(), "'delete all' command.")
            keyboard.send('ctrl+a')
            keyboard.send('delete')
            return

        if state.mode == "default":
            try:
                processed_text = process_voice_prompt(full_text.strip())
                add_log(state.get_log_box(), f"Text after processing: {processed_text.strip()}")
            except Exception as e:
                add_log(state.get_log_box(), f"Error contacting AI")
                print(f"Error processing text: {e}")
                processed_text = full_text.strip() 
        else:
            try:
                processed_text = writing_assistant(full_text.strip())
                add_log(state.get_log_box(), f"AI written text: {processed_text.strip()}")
            except Exception as e:
                processed_text = full_text.strip()
                add_log(state.get_log_box(), f"Error contacting AI")
                print(f"Error processing text: {e}")

        
        write(processed_text)

    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

