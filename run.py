import threading
from functions.hotkey_listener import wait_for_trigger_keys
from ui.main_window import app

threading.Thread(target=wait_for_trigger_keys, daemon=True).start()
app.mainloop()