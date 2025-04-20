import os
import tempfile
import keyboard
import soundfile as sf
import time 
from faster_whisper import WhisperModel

from functions.writer import write
from ai.text_processor import process_voice_prompt
from ai.writing_assistant import writing_assistant
from states.state import state
from ui.log_window import add_log
from functions.settings_functions import read_settings

def transcribe_audio(audio_data):

    model_loading_start_time = time.time()

    settings = read_settings()
    model_size = settings.get("model", "base")
    ai_processing = settings.get("ai_processing", True)
    device = settings.get("device", "cpu")
    sample_rate = 16000

    model = WhisperModel(model_size, device=device, compute_type="int8")

    add_log(state.get_log_box(), f"whisper model: {model_size}, time: {time.time() - model_loading_start_time:.2f} seconds")
    add_log(state.get_log_box(), f"device: {device}")
    
    transcription_start_time = time.time()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        temp_filename = tmpfile.name

    try:
        sf.write(temp_filename, audio_data, samplerate=sample_rate)
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
                if ai_processing:
                    processed_text = process_voice_prompt(full_text.strip())
                    add_log(state.get_log_box(), f"Text after processing: {processed_text.strip()}")
                else:
                    processed_text = full_text.strip()
                    add_log(state.get_log_box(), f"AI processing disabled.")

            # If the ai processing is enabled but cant connect to the AI, it will just write the text as is.
            except Exception as e:
                add_log(state.get_log_box(), f"Error contacting AI")
                print(f"Error processing text: {e}")
                processed_text = full_text.strip() 

        # If the mode is set to writing_assistant, it will use the writing_assistant function to process the text.
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
        transcription_end_time = time.time()
        transcription_time = transcription_end_time - transcription_start_time

        add_log(state.get_log_box(), f"Transcription and processing took {transcription_time:.2f} seconds.")

        if os.path.exists(temp_filename):
            os.remove(temp_filename)
