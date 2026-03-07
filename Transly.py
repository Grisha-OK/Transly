"""                                 
I apologize for this appeal :D
                                    
"""    

# pip install ...
# External libraries
import clipboard
import keyboard
import pystray

from googletrans import Translator
from pystray import MenuItem as item
from PIL import Image #pip install pillow

# Standard Python modules
import time
import json
import os
import getpass
import ctypes
import shutil
import sys

# GUI modules
from tkinter import Tk
import customtkinter #pip install customtkinter

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

switch_off = ''

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
class TransProches:
    def __init__(self, ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF):
 
        self.ALPHABET_LANGUAGE = ALPHABET_LANGUAGE
        self.HOT_KEY_LAYOUT = HOT_KEY_LAYOUT
        self.HOT_KEY_TRANSLATION = HOT_KEY_TRANSLATION
        self.LANGUAGE_EN = LANGUAGE_EN
        self.LANGUAGE_RU = LANGUAGE_RU
        self.SWITCH_OFF = SWITCH_OFF

        global switch_off
        
        self.CONSTANT_LIST = {}
        self.path = self.reate_a_folder()
        self.file_icon_path = self.file_path("favicon.ico")
        self.shron = self.json_worker()

        switch_off = self.shron["switch_off"]               #call the language_ru text
        self.hot_key_n1 = self.shron["hot_key_layout"]           #call the hot-key-№1 text
        self.hot_key_n2 = self.shron["hot_key_translation"]      #call the hot-key-№2 text
        self.language_1 = self.shron["language_en"]              #call the language_en text
        self.language_2 = self.shron["language_ru"]              #call the language_ru text
        self.dictionary = self.shron["alphabet_language"]        #call the dictionary text

    # Function to create a folder for storing the service file
    def reate_a_folder(self):
        username = getpass.getuser()
        path = (f"C:/Users/{username}/.transly")
        try:
            os.makedirs(f"{path}/img")
            return(path)
        except:
            return(path)
    
    # Function to find the path to the file directory
    def file_path(self, tild):
        name_file = os.path.basename(__file__)
        path_to_file = os.path.realpath(__file__).replace(name_file, tild)
        if "Temp" in path_to_file: #condition for checking if the file is compiled
            return(path_to_file)
        elif "GitHub" in path_to_file: #condition for checking if the file is development
            shutil.copy(path_to_file, f"{self.path}/img/favicon.ico") #copy the picture to the working directory
            return(path_to_file)
        else:  
            try:
                shutil.move(path_to_file, f"{self.path}/img/favicon.ico") #move the picture to the working directory
                return(f"{self.path}/img/favicon.ico")
            except:
                return(f"{self.path}/img/favicon.ico")
    
    # Function to assemble text for JSON deserialization
    def mergiing(self, nomber, text):
        self.CONSTANT_LIST[nomber] = text
    
    # Function for filling a list of constants
    def setting_dap(self):
        self.mergiing("switch_off", SWITCH_OFF)                   #call the text assembly for JSON deserialization with key 1 and value switch_off
        self.mergiing("hot_key_layout", HOT_KEY_LAYOUT)           #call the text assembly for JSON deserialization with key 2 and value hot_key_№1
        self.mergiing("hot_key_translation", HOT_KEY_TRANSLATION) #call the text assembly for JSON deserialization with key 3 and value hot_key_№2
        self.mergiing("language_en", LANGUAGE_EN)                 #call the text assembly for JSON deserialization with key 4 and value language_en
        self.mergiing("language_ru", LANGUAGE_RU)                 #call the text assembly for JSON deserialization with key 5 and value language_ru
        self.mergiing("alphabet_language", ALPHABET_LANGUAGE)     #call the text assembly for JSON deserialization with key 6 and value alphabet_language
        return(self.CONSTANT_LIST)
    
    # Function to create json file
    def push_config_file(self, const_shron_dump):
        with open(f"{self.path}/dictionary.json", "w") as write_file:
            json.dump(dict(const_shron_dump), write_file, indent=4)
    
    # Function to encode text settings in it
    def json_worker(self):
        try:
            with open(f"{self.path}/dictionary.json", "r") as write_file: #file opened only in the with open construct
                interlayer = {}
                interlayer = json.loads(write_file.read())
                return(interlayer) 
        except FileNotFoundError:
            const_shron = self.setting_dap()
            self.push_config_file(const_shron)
            return(const_shron)

    # Function for extracting text from the input hoop
    def selecting_text(self, typ_is):
        try:
            def clip_get():
                CTRL_C()
                return(Tk().clipboard_get())
            if typ_is == "master_keyboard_worker":
                self.master_keyboard_worker(clip_get())
            elif typ_is == "master_transly_worker":
                self.master_transly_worker(clip_get())
            else:
                return
        except:
            #print("ошибка")
            time.sleep(0.1)
            self.selecting_text(typ_is)
    
    # Function for copying, translating, assembling and pasting text
    def master_keyboard_worker(self, select_text):
        re_print = ''
        #preparing the copied text
        for i in select_text:
            try:
                re_print = str(re_print + self.dictionary[i])
            except:
                re_print = re_print + i
        clipboard.copy(re_print)  #add the finished text to the clipboard
        CTRL_V()
        
        if switch_off == True: #condition for switching the layout
            SHIFT_ALT()
    
    # Function for working with Google translator
    def master_transly_worker(self, select_text):
        translator = Translator()
        detected = translator.detect(select_text)
        if detected.lang == self.language_1:
            for_translation = "ru"
        elif detected.lang == self.language_2:
            for_translation = "en"
        else:
            for_translation = "en"
        translation = translator.translate(select_text, dest=for_translation)
        clipboard.copy(translation.text)  #add the finished text to the clipboard
        CTRL_V()
    
    # Hot-key check
    def check_hotkey(self):
        try:
            keyboard.add_hotkey(self.hot_key_n1, lambda: self.selecting_text("master_keyboard_worker"))
            keyboard.add_hotkey(self.hot_key_n2, lambda: self.selecting_text("master_transly_worker"))
        except:
            return
class TranslyGUI:
    def __init__(self, file_icon_path, shron, push_config_file):

        self.file_icon_path = file_icon_path
        self.shron = shron
        self.push_config_file = push_config_file

        # Create an instance of the tkinter frame or window
        self.win = customtkinter.CTk()
        self.win.title("Transly")
        self.win.iconbitmap(file_icon_path)
        self.win.geometry("300x85")
        customtkinter.set_widget_scaling(0.85)

        self._create_widgets()
        self._setup_tray()

    def _create_widgets(self):
        # Add a separating border
        self.frame = customtkinter.CTkFrame(self.win)
        self.frame.pack(fill='both', side='left', expand=True)

        # Add indentation
        customtkinter.CTkLabel(self.frame, text="Changing the layout:", font=(0, 17)
                               ).pack(side='top', pady=10)
        customtkinter.CTkLabel(self.win, text="   ", fg_color="transparent"
                               ).pack(side='top', pady=0)
        
        # Add a button to exit the program
        customtkinter.CTkButton(self.win, text="Quit", font=(0, 17), command=lambda: sys.exit(),
                                fg_color="gray10", corner_radius=16).pack(
                                    side='top',
                                    padx=(10,10),
                                    pady=(0,20),
                                    ipadx=5,
                                    ipady=5)
        
        # Specifically the toggle itself:
        self.is_on = customtkinter.BooleanVar(value=False)
        self.toggle_button = customtkinter.CTkSwitch(
            self.frame,
            text="", width=10,
            variable=self.is_on, onvalue="on",
            offvalue="off", command=lambda: self._toggle_switch())
        self.toggle_button.pack(side='top')
        
        if switch_off:
            self.toggle_button.select()
   
    #Check window closing and tray icon initialization
    def _setup_tray(self):
        self.win.protocol('WM_DELETE_WINDOW', self._hide_window)
    
    # Function true/false switch
    def _toggle_switch(self):
        global switch_off
        switch_off = not(switch_off)
        self.shron["switch_off"] = switch_off
        self.push_config_file(self.shron)
    
    # Hide the window and show it on the system taskbar
    def _hide_window(self):
       self.win.withdraw()
       image = Image.open(self.file_icon_path)
       menu = (item('Quit', lambda : self._quit_window(self.icon)),
               item('Show', lambda : self._show_window(self.icon)))
       self.icon = pystray.Icon("name", image, "Trans Translation", menu)
       self.icon.run()
    
    # Define a function to exit the window / and by compatibility for exiting the entire program
    def _quit_window(self):
           self.icon.stop()
           os.abort()
    
    # A function for re-displaying the window
    def _show_window(self):
        self.icon.stop()
        self.win.deiconify() #I'll probably leave it here <win.after(0,win.deiconify())>

    def run(self):
        self.win.mainloop() 

if __name__ == "__main__":
    main = TransProches(ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF)
    main.check_hotkey() #hot-key check
    app = TranslyGUI(main.file_icon_path, main.shron, main.push_config_file)
    app.run()