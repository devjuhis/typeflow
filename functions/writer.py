import keyboard
import pyperclip
import time

def write(text):
    pyperclip.copy(text)        
    time.sleep(0.1)          
    keyboard.press_and_release('ctrl+v')