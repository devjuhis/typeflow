import customtkinter as ctk
from functions.settings_functions import save_settings, read_settings

def create_settings_window(app, on_hotkey_update=None):
    settings_window = ctk.CTkToplevel(app)
    settings_window.title("Settings")
    settings_window.geometry("400x330")
    settings_window.lift()
    settings_window.attributes("-topmost", 1)

    settings = read_settings()

    ctk.CTkLabel(settings_window, text="Hotkey:").pack(pady=(15, 0))
    hotkey_entry = ctk.CTkEntry(settings_window)
    hotkey_entry.insert(0, settings.get("hotkey", "ctrl+shift"))
    hotkey_entry.pack()

    def update_hotkey():
        new_hotkey = hotkey_entry.get()
        settings["hotkey"] = new_hotkey
        save_settings(settings)
        if on_hotkey_update:
            on_hotkey_update(new_hotkey)

    ctk.CTkButton(settings_window, text="Save Hotkey", command=update_hotkey).pack(pady=5)

    ctk.CTkLabel(settings_window, text="Model:").pack(pady=(15, 0))
    model_var = ctk.StringVar(value=settings.get("model", "base"))
    def update_model(value):
        settings["model"] = value
        save_settings(settings)

    model_selector = ctk.CTkOptionMenu(
        settings_window,
        values=["tiny", "base", "small", "medium"],
        variable=model_var,
        command=update_model
    )
    model_selector.pack()

    ctk.CTkLabel(settings_window, text="Device:").pack(pady=(15, 0))
    model_var = ctk.StringVar(value=settings.get("device", "cpu"))
    def update_device(value):
        settings["device"] = value
        save_settings(settings)

    device_selector = ctk.CTkOptionMenu(
        settings_window,
        values=["cpu", "cuda", "mps", "xla"],
        variable=model_var,
        command=update_device
    )
    device_selector.pack()

    ctk.CTkLabel(settings_window, text="AI Processing:").pack(pady=(15, 0))
    ai_var = ctk.BooleanVar(value=settings.get("ai_processing", True))
    def toggle_ai():
        settings["ai_processing"] = ai_var.get()
        save_settings(settings)

    ai_checkbox = ctk.CTkCheckBox(
        settings_window,
        text="Enable AI processing",
        variable=ai_var,
        command=toggle_ai
    )
    ai_checkbox.pack()

    ctk.CTkButton(settings_window, text="Close", command=settings_window.destroy).pack(pady=20)
