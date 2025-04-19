class AppState:
    def __init__(self):
        self.mode = "default"
        self.log_box = None  
    
    def set_mode(self, mode):
        self.mode = mode
    
    def get_mode(self):
        return self.mode
    
    def set_log_box(self, log_box):
        self.log_box = log_box

    def get_log_box(self):
        return self.log_box

state = AppState()