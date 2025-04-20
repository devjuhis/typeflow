import customtkinter as ctk
from states.state import state

def create_log_window(app):
    log_window = ctk.CTkToplevel(app) 
    log_window.title("Logs")  
    log_window.geometry("400x330")

    app.iconbitmap('./assets/Typeflow_logo.ico')

    log_window.lift()
    log_window.attributes("-topmost", 1)

    log_box = ctk.CTkTextbox(log_window, width=380, height=250, font=("Consolas", 12), wrap="word")
    log_box.pack(pady=(10, 5))
    log_box.insert("end", "📝 Log window started...\n")
    log_box.configure(state="disabled") 

    def clear_log():
        log_box.configure(state="normal")
        log_box.delete("1.0", "end")
        log_box.insert("end", "📝 Log window cleared.\n")
        log_box.configure(state="disabled")

    clear_button = ctk.CTkButton(log_window, text="clear log", command=clear_log)
    clear_button.pack(pady=(0, 10))

    state.set_log_box(log_box)
    
    return log_box

def add_log(log_box, message):
    if log_box is not None:
        log_box.configure(state="normal")
        log_box.insert("end", message + "\n")
        log_box.configure(state="disabled")

