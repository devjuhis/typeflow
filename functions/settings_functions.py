import json
import os

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "hotkey": "ctrl+shift",
    "model": "base",
    "ai_processing": True
}

def save_settings(settings, filename=SETTINGS_FILE):
    with open(filename, 'w') as f:
        json.dump(settings, f, indent=4)

def read_settings(filename=SETTINGS_FILE):
    if not os.path.exists(filename):
        print("Asetustiedostoa ei löytynyt. Palautetaan oletusasetukset.")
        return DEFAULT_SETTINGS.copy()
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Virhe asetuksia luettaessa: {e}")
        return DEFAULT_SETTINGS.copy()
