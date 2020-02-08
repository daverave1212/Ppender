import sys
import time
import pynput
import pynput.keyboard as keyboard
from pynput.keyboard import Key
import pyperclip
import os
import win32clipboard
import shutil

import config


controller = keyboard.Controller()
capture_keys = True

config.configure()

def do_paste_magic():
    capture_keys = False
    controller.release(Key.ctrl_l)
    time.sleep(0.01)
    if config.press_f2_on_ctrl1:
        press_f2()
        time.sleep(0.01)
    time.sleep(0.01)
    type_string(get_clipboard_text(remove_newline=True) + config.phrase_to_paste)
    if config.does_press_enter:
        time.sleep(0.01)
        press_enter()
    time.sleep(0.01)
    capture_keys = True

def copy_selected_file_to_path(destination_path):
    time.sleep(0.01)
    press_ctrl_c()
    time.sleep(0.01)
    if not is_clipboard_hdrop():
        print("ERROR: Something went wrong.")
        return
    (source_path, ) = get_clipboard_hdrop_path()    # It's a tuple of one element
    print('Copying ' + source_path + ' to ' + destination_path)
    if not os.path.exists(destination_path):
        print('The given path does not exist.')
        return
    if not os.path.exists(source_path):
        print('The file in your clipboard does not exist.')
        return
    if os.path.isdir(source_path):
        print("It's a directory, mate...")
    else:
        file_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, file_name)
        if config.cut_instead_of_copy:
            print('Moving..')
            shutil.move(source_path, destination_path)
        else:
            os.replace(source_path, destination_path)        
        print('Done')




def on_press(key):
    global is_ctrl_down
    if capture_keys is False:
        return
    if key == Key.f3:                           # F3
        do_paste_magic()
    elif key == Key.f5 and config.exit_on_f5:   # F5
        sys.exit()
    elif str(key) == '<49>':                    # ctrl + 1
        do_paste_magic()
    elif str(key) == '<50>':                    # ctrl + 2
        copy_selected_file_to_path(config.config['PATH1'])
    elif str(key) == '<51>':                    # ctrl + 2
        copy_selected_file_to_path(config.config['PATH2'])
    else:
        print(key)

def on_release(key):
    pass

def type_string(string):
    for char in string:
        controller.press(char)
        controller.release(char)

def press_enter():
    controller.press(Key.enter)
    controller.release(Key.enter)

def press_f2():
    controller.press(Key.f2)
    controller.release(Key.f2)

def press_ctrl_c():
    controller.press(Key.ctrl_l)
    controller.press('c')
    controller.release(Key.ctrl_l)
    controller.release('c')

def get_clipboard_text(remove_newline=False):
    text = pyperclip.paste()
    if remove_newline:
        text = text.rstrip()
    return text

def is_clipboard_hdrop():
    win32clipboard.OpenClipboard()
    is_it_hdrop = False
    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_HDROP):
        is_it_hdrop = True
    win32clipboard.CloseClipboard()
    return is_it_hdrop

def get_clipboard_hdrop_path(): # Will crash if it's not a CF_HDROP format. Use the previous function to check
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
    win32clipboard.CloseClipboard()
    return data



with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



