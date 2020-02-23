# Code by Irimia David (https://github.com/daverave1212/Ppender)
# Idea by Logofeteanu Stefan

import sys
import time
import pynput
import pynput.keyboard as keyboard
from pynput.keyboard import Key
import pyperclip
import os
import win32clipboard
import shutil

def on_press(key):
    char_code = str(key)
    print(char_code)

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
