"""                                 
I apologize for this appeal :D
                                    
"""    

# pip install ...
# External libraries
import clipboard
import keyboard
#import pystray

from googletrans import Translator
# from pystray import MenuItem as item
# from PIL import Image #pip install pillow

# Standard Python modules
import time
import json
import os
import getpass
import ctypes
import shutil
#import sys

# GUI modules
from tkinter import Tk
from gui import TranslyGUI

# So-called alphabet
ALPHABET_LANGUAGE = {
    "ё": "`", "Ё": "~", "й": "q", "Й": "Q", "ц": "w", "Ц": "W", "у": "e", "У": "E", "к": "r", "К": "R", "е": "t", "Е": "T", "н": "y", "Н": "Y", "г": "u", "Г": "U", "ш": "i",
     "Ш": "I", "щ": "o", "Щ": "O", "з": "p", "З": "P", "х": "[", "Х": "{", "ъ": "]", "Ъ": "}", "ф": "a", "Ф": "A", "ы": "s", "Ы": "S", "в": "d", "В": "D", "а": "f", "А": "F", "п": "g", "П": "G",
      "р": "h", "Р": "H", "о": "j", "О": "J", "л": "k", "Л": "K", "д": "l", "Д": "L", "ж": ";", "Ж": ":", "э": "'", "Э": '"', "я": "z", "Я": "Z", "ч": "x", "Ч": "X", "с": "c", "С": "C", "м": "v",
       "М": "V", "и": "b", "И": "B", "т": "n", "Т": "N", "ь": "m", "Ь": "M", "б": ",", "Б": "<", "ю": ".", "Ю": ">", 
        '`': 'ё', '~': 'Ё', 'q': 'й', 'Q': 'Й', 'w': 'ц', 'W': 'Ц', 'e': 'у', 'E': 'У', 'r': 'к', 'R': 'К', 't': 'е', 'T': 'Е', 'y': 'н', 'Y': 'Н', 'u': 'г', 'U': 'Г', 'i': 'ш',
         'I': 'Ш', 'o': 'щ', 'O': 'Щ', 'p': 'з', 'P': 'З', '[': 'х', '{': 'Х', ']': 'ъ', '}': 'Ъ', 'a': 'ф', 'A': 'Ф', 's': 'ы', 'S': 'Ы', 'd': 'в', 'D': 'В', 'f': 'а', 'F': 'А', 'g': 'п', 'G': 'П',
          'h': 'р', 'H': 'Р', 'j': 'о', 'J': 'О', 'k': 'л', 'K': 'Л', 'l': 'д', 'L': 'Д', ';': 'ж', ':': 'Ж', "'": 'э', '"': 'Э', 'z': 'я', 'Z': 'Я', 'x': 'ч', 'X': 'Ч', 'c': 'с', 'C': 'С', 'v': 'м',
           'V': 'М', 'b': 'и', 'B': 'И', 'n': 'т', 'N': 'Т', 'm': 'ь', 'M': 'Ь', ',': 'б', '<': 'Б', '.': 'ю', '>': 'Ю',
            "\n": "\n", '?': ',', " ": " "}

HOT_KEY_LAYOUT = ("ctrl + F9")
HOT_KEY_TRANSLATION = ("ctrl + F8")
LANGUAGE_EN = ("en")
LANGUAGE_RU = ("ru")
SWITCH_OFF = False #variable for setting up the layout switch

# Function to create a folder for storing the service file
def reate_a_folder():
    username = getpass.getuser()
    path = (f"C:/Users/{username}/.transly")
    try:
        os.makedirs(f"{path}/img")
        return(path)
    except:
        return(path)
path = reate_a_folder()

# Function to find the path to the file directory
def file_path(tild):
    name_file = os.path.basename(__file__)
    path_to_file = os.path.realpath(__file__).replace(name_file, tild)
    if "Temp" in path_to_file: #condition for checking if the file is compiled
        return(path_to_file)
    elif "GitHub" in path_to_file: #condition for checking if the file is development
        shutil.copy(path_to_file, f"{path}/img/favicon.ico") #copy the picture to the working directory
        return(path_to_file)
    else:  
        try:
            shutil.move(path_to_file, f"{path}/img/favicon.ico") #move the picture to the working directory
            return(f"{path}/img/favicon.ico")
        except:
            return(f"{path}/img/favicon.ico")
file_icon_path = file_path("favicon.ico")

# Function to press the keys
def CTRL_C():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # Ctrl down
    ctypes.windll.user32.keybd_event(0x43, 0, 0, 0)  # C down
    ctypes.windll.user32.keybd_event(0x43, 0, 2, 0)  # C up
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # Ctrl up    
def CTRL_V():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # Ctrl down
    ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)  # V down
    ctypes.windll.user32.keybd_event(0x56, 0, 2, 0)  # V up
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # Ctrl up
def SHIFT_ALT():
    ctypes.windll.user32.keybd_event(0x10, 0, 0, 0)  # Shift down
    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # Alt down
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)  # Alt up
    ctypes.windll.user32.keybd_event(0x10, 0, 2, 0)  # Shift up

# Function to assemble text for JSON deserialization
CONSTANT_LIST = {}
def mergiing(nomber, text):
    global CONSTANT_LIST
    CONSTANT_LIST[nomber] = text

# Function for filling a list of constants
def setting_dap():
    mergiing("switch_off", SWITCH_OFF)                   #call the text assembly for JSON deserialization with key 1 and value switch_off
    mergiing("hot_key_layout", HOT_KEY_LAYOUT)           #call the text assembly for JSON deserialization with key 2 and value hot_key_№1
    mergiing("hot_key_translation", HOT_KEY_TRANSLATION) #call the text assembly for JSON deserialization with key 3 and value hot_key_№2
    mergiing("language_en", LANGUAGE_EN)                 #call the text assembly for JSON deserialization with key 4 and value language_en
    mergiing("language_ru", LANGUAGE_RU)                 #call the text assembly for JSON deserialization with key 5 and value language_ru
    mergiing("alphabet_language", ALPHABET_LANGUAGE)     #call the text assembly for JSON deserialization with key 6 and value alphabet_language
    return(CONSTANT_LIST)

# Function to create json file
def push_config_file(const_shron_dump):
    with open(f"{path}/dictionary.json", "w") as write_file:
        json.dump(dict(const_shron_dump), write_file, indent=4)

# Function to encode text settings in it
def json_worker():
    try:
        with open(f"{path}/dictionary.json", "r") as write_file: #file opened only in the with open construct
            interlayer = {}
            interlayer = json.loads(write_file.read())
            return(interlayer) 
    except FileNotFoundError:
        const_shron = setting_dap()
        push_config_file(const_shron)
        return(const_shron)

shron = {}
shron = json_worker()

switch_off = shron["switch_off"]               #call the language_ru text
hot_key_n1 = shron["hot_key_layout"]           #call the hot-key-№1 text
hot_key_n2 = shron["hot_key_translation"]      #call the hot-key-№2 text
language_1 = shron["language_en"]              #call the language_en text
language_2 = shron["language_ru"]              #call the language_ru text
dictionary = shron["alphabet_language"]        #call the dictionary text

# Function for extracting text from the input hoop
def selecting_text(typ_is):
    try:
        def clip_get():
            CTRL_C()
            return(Tk().clipboard_get())
        if typ_is == "master_keyboard_worker":
            master_keyboard_worker(clip_get())
        elif typ_is == "master_transly_worker":
            master_transly_worker(clip_get())
        else:
            return
    except:
        #print("ошибка")
        time.sleep(0.1)
        selecting_text(typ_is)

# Function for copying, translating, assembling and pasting text
def master_keyboard_worker(select_text):
    re_print = ''
    #preparing the copied text
    for i in select_text:
        try:
            re_print = str(re_print + dictionary[i])
        except:
            re_print = re_print + i
    clipboard.copy(re_print)  #add the finished text to the clipboard
    CTRL_V()
    
    if switch_off == True: #condition for switching the layout
        SHIFT_ALT()

# Function for working with Google translator
def master_transly_worker(select_text):
    translator = Translator()
    detected = translator.detect(select_text)
    if detected.lang == language_1:
        for_translation = "ru"
    elif detected.lang == language_2:
        for_translation = "en"
    else:
        for_translation = "en"
    translation = translator.translate(select_text, dest=for_translation)
    clipboard.copy(translation.text)  #add the finished text to the clipboard
    CTRL_V()

# Hot-key check
def check_hotkey():
    try:
        keyboard.add_hotkey(hot_key_n1, lambda: selecting_text("master_keyboard_worker"))
        keyboard.add_hotkey(hot_key_n2, lambda: selecting_text("master_transly_worker"))
    except:
        return

if __name__ == "__main__":
    check_hotkey() #hot-key check
    app = TranslyGUI(file_icon_path, switch_off, shron, push_config_file)
    app.run()