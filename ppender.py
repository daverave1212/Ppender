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
    print('Copying...')
    press_ctrl_c()
    time.sleep(0.01)
    if not is_clipboard_hdrop():
        print("  ERROR: Something went wrong.")
        return
    (source_path, ) = get_clipboard_hdrop_path()    # It's a tuple of one element
    if not os.path.exists(destination_path):
        print('  The given path (' + destination_path + ') does not exist.')
        return
    if not os.path.exists(source_path):
        print('  The file in your clipboard (' + source_path + ') does not exist.')
        return
    if os.path.isdir(source_path):
        print("  It's a directory, mate...")
    else:
        file_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, file_name)
        if config.cut_instead_of_copy:
            print('  Moving from ' + source_path + ' to ' + destination_path)
            shutil.move(source_path, destination_path)
        else:
            os.replace(source_path, destination_path)        
        print('Done')


def on_press(key):
    if capture_keys is False:
        return
    elif key == Key.f5 and config.exit_on_f5:   # F5
        print('Exiting.')
        sys.exit()
    elif key == Key.f8:                         # F8
        do_paste_magic()
    elif key == Key.f9:                         # F9
        copy_selected_file_to_path(config.config['PATH1'])
    elif key == Key.f10:                        # F10
        copy_selected_file_to_path(config.config['PATH2'])
    '''
    elif str(key) == '<49>':                    # ctrl + 1
        do_paste_magic()
    elif str(key) == '<50>':                    # ctrl + 2
        copy_selected_file_to_path(config.config['PATH1'])
    elif str(key) == '<51>':                    # ctrl + 2
        copy_selected_file_to_path(config.config['PATH2'])
    else:
        print(key)
    '''

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


try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except:
    print('Oh no! Looks like Ppender has crashed! No worries, send the messages above to Dave and he will know what to do!')

print('Press enter to exit.')
input()



