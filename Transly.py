"""                                 
I apologize for this appeal :D
                                    
"""    

# External libraries
import clipboard
import keyboard

from googletrans import Translator
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image

# Standard Python modules
from pathlib import Path
import inspect
import time
import json
import os
#import getpass
import ctypes
import sys

# GUI modules
from tkinter import Tk
import customtkinter
from CTkToolTip import CTkToolTip

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
SWITCH_SIFT_ALT = False #variable for setting up the layout switch

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
def CTRL_A():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # Ctrl down
    ctypes.windll.user32.keybd_event(0x41, 0, 0, 0)  # A down
    ctypes.windll.user32.keybd_event(0x41, 0, 2, 0)  # A up
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # Ctrl up 
def SHIFT_ALT():
    ctypes.windll.user32.keybd_event(0x10, 0, 0, 0)  # Shift down
    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # Alt down
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)  # Alt up
    ctypes.windll.user32.keybd_event(0x10, 0, 2, 0)  # Shift up

# General storage switch value
class BacupsShron:
    '''A class for storing and working with system variables and values ​​from a backup.'''
    def __init__(self):
        pass

    def atribute_arow(self, busup_dict):
        '''
        A function for setting attributes of the class
        busup_dict - a dictionary with the names of the attributes as keys and their values as values
        '''
        for key, value in busup_dict.items():
            setattr(self, key, value)
    
    def atribute_list(self):
        '''
        A function for getting a list of the names of the attributes of the class
        '''
        members = inspect.getmembers(self)
        only_vars = [
            m[0] for m in members
            if not m[0].startswith('__') and not inspect.ismethod(m[1])
        ]
        return(only_vars)
    
    def atreibute_list_value(self):
        '''
        A function for getting a dictionary of the names of the attributes of the class as keys and their values as values
        '''
        list_value = {}
        for i in self.atribute_list():
            list_value[i] = getattr(self, i)
        return list_value

    def push_attributes(self, target_obj, attribute_names=None):
        """
        A function for copying attributes from one object to another
        target_obj - the object to which the attributes will be copied
        attribute_names - a list of attribute names to copy. If None, all attributes will be copied
        """
        if attribute_names is None:
            attribute_names = list(self.atreibute_list_value().keys())

        for attr in attribute_names:
            if hasattr(self, attr):  # Проверяем, существует ли такой атрибут у нас
                value = getattr(self, attr)
                setattr(target_obj, attr, value)
            else:
                print(f"Предупреждение: Атрибут {attr} не найден в текущем объекте")

class TransJson:
    '''
    Class for working with JSON file, which stores the settings of the program, and also for working with the file system in general
    '''
    def __init__(self):
        pass

    # Function to check if the file is compiled, which is used to determine the path to the file icon and config directory
    def we_compiled(self):
        '''Function to check if the file is compiled, which is used to determine the path to the file icon and config directory'''
        path_to_main_file = Path(__file__).resolve()
        if getattr(sys, 'frozen', False):
            # Если скрипт скомпилирован
            print(f"Запущено из скомпилированного файла (PyInstaller), по пути: {path_to_main_file}")
            return(True)
        else:
            # Если это обычный .py файл
            print(f"Запущено как обычный скрипт Python, по пути: {path_to_main_file}")
            return(False)   

    # Function to find the path to the file icon directory
    def file_icon_path(self, file, folder_path = ""):
        '''
        Function to find the path to the file icon directory, which is used to store the icon of the program in the system tray
        file - the name of the icon file
        folder_path - the relative path to the folder where the configuration file is stored. This is necessary for the file to work both in the compiled and non-compiled state, since the path to the file icon directory is different in these states
        '''
        path_main_file = Path(__file__).resolve()
        path_to_nain_folder = path_main_file.parent
        if self.we_compiled(): #condition for checking if the file is compiled
            path_to_icon_config = path_to_nain_folder / file
        else:
            path_to_icon_config = path_to_nain_folder / folder_path / file
        # Function to create an icon if it does not exist, which is used to create an icon for the program in the system tray if it does not exist   
        def ensure_icon_exists(path_to_target_file, color=(70, 70, 70), size=(256, 256)):
            if not os.path.exists(path_to_target_file):
                print(f"Иконка не найдена. Создаю иконку по пути: {path_to_target_file}")
                img = Image.new("RGB", size, color=color)
                os.makedirs(os.path.dirname(path_to_target_file) if os.path.dirname(path_to_target_file) else ".", exist_ok=True)
                img.save(path_to_target_file, format="ICO")
            return()
        ensure_icon_exists(str(path_to_icon_config))
        return(str(path_to_icon_config))

    # Function to find the path to the file config directory
    def file_config_path(self, file, user_folder_path = "", desctop_folder_path = ""):
        '''
        Function to find the path to the file config directory, which is used to store the settings of the program
        file - the name of the config file
        #folder_path - the path to the folder where the config file is stored
        '''
        user_home = Path.home()
        path_main_file = Path(__file__).resolve()
        path_to_nain_folder = path_main_file.parent
        if self.we_compiled(): #condition for checking if the file is compiled
            path_to_json_config = user_home / user_folder_path / file
        else:
            path_to_json_config = path_to_nain_folder / desctop_folder_path / file
        
        # Function to create a folder for storing the service file
        def create_a_folder(where):
            try:
                os.makedirs(where)
                return(where)
            except:
                return(where)
        create_a_folder(str(path_to_nain_folder))
        return(str(path_to_json_config))

    # Function for setting attributes of the class, which are used in different parts of the program
    def setting_attributes(self, shron, VALUE_LIST, icon_path, config_path):
        '''
        Function for setting attributes of the class, which are used in different parts of the program
        shron - the JSON worker instance, which is used to work with the JSON file, which stores the settings of the program
        VALUE_LIST - the list of values to be set as attributes
        icon_path - the path to the file icon directory
        config_path - the path to the file config directory
        '''
        #worcking attributes
        self.shron = shron
        self.VALUE_LIST = VALUE_LIST
        self.icon_path = icon_path
        self.config_path = config_path
        self.json_worker()
    
    # Function to create json file
    def push_config_file(self, const_shron_dump):
        '''
        Function to write the settings of the program to a JSON file, which is used to store the settings of the program
        const_shron_dump - the settings of the program, which is used to store the settings of the program
        '''
        with open(self.config_path, "w") as write_file:
            json.dump(dict(const_shron_dump), write_file, indent=4)
    
    # Function to encode text settings in it
    def json_worker(self):
        '''Function for working with JSON file, which stores the settings of the program, and also for working with the file system in general'''
        try:
            with open(self.config_path, "r") as write_file: #file opened only in the with open construct
                interlayer = {}
                interlayer = json.loads(write_file.read())
                # return(interlayer)
                self.shron.atribute_arow(interlayer)
                return()
        except FileNotFoundError:
            self.push_config_file(self.VALUE_LIST)
            self.shron.atribute_arow(self.VALUE_LIST)
            return()
        
class TransLayout():
    def __init__(self, shron):
        #forwarding attributes from TransJson, including hot class, language, and switch state attributes
        self.shron = shron

    # Function for extracting text from the input hoop
    def selecting_text(self, copy=True):
        '''
        Function for extracting text from the input hoop, which is used to get the text that the user wants to translate or change the layout of
        copy - a boolean value that determines whether to copy the text from the input hoop or not, which is used to get the text that the user wants to translate or change the layout of
        '''
        def clip_get(counter=0):
           try:
               if counter == 5:
                   print("превышено количество попыток получения текста из буфера обмена")
                   return(clipboard.paste())
            #    if self.shron.switch_ctrl_a_config and copy == True:
            #        CTRL_A()
               if copy:
                   CTRL_C()
               return(Tk().clipboard_get())
           except:
               #print("ошибка")
               time.sleep(0.1)
               return(clip_get(counter+1))
        return(clip_get())
    
    # Function for copying, translating, assembling and pasting text
    def master_keyboard_worker(self, select_text, paste=True):
        '''
        The main function of character-by-character translation of text from a dictionary, layout and insertion of text, used to change the layout of the text that the user wants to change.
        select_text - the text that the user wants to change the layout of, which is used to change the layout of the text that the user wants to change the layout of
        paste - a boolean value that determines whether to paste the text after changing the layout or not, which is used to change the layout of the text that the user wants to change the layout of
        '''
        re_print = ''
        #preparing the copied text
        for i in select_text:
            try:
                re_print = str(re_print + self.shron.simvol_alphabet_language[i])
            except:
                re_print = re_print + i
        clipboard.copy(re_print)  #add the finished text to the clipboard
        if paste == True:
            CTRL_V()
        else:
            return(re_print)

        if self.shron.switch_shift_alt_config: #condition for switching the layout
            SHIFT_ALT()
    
    # Function for working with Google translator
    def master_transly_worker(self, select_text, paste=True):
        '''
        The main function for working with Google translator, which is used to translate the text that the user wants to translate.
        select_text - the text that the user wants to translate, which is used to translate the text that the user wants to translate
        paste - a boolean value that determines whether to paste the text after translating or not, which is used to translate the text that the user wants to translate
        '''
        translator = Translator()
        detected = translator.detect(select_text)
        if detected.lang == self.shron.language_en:
            for_translation = "ru"
        elif detected.lang == self.shron.language_ru:
            for_translation = "en"
        else:
            for_translation = "en"
        translation = translator.translate(select_text, dest=for_translation)
        clipboard.copy(translation.text)  #add the finished text to the clipboard
        if paste:
            CTRL_V()
        else:
            return(translation.text)

    # Hot-key check
    def check_hotkey(self):
        '''Hot-key check, which is used to set up the hot-keys for changing the layout and translating the text that the user wants to change the layout of or translate'''
        try:
            keyboard.add_hotkey(self.shron.hot_key_layout, lambda: self.master_keyboard_worker(self.selecting_text()))
            keyboard.add_hotkey(self.shron.hot_key_translate, lambda: self.master_transly_worker(self.selecting_text()))
        except:
            return

class Switchpool:
    '''
    Class for
    '''
    def __init__(self, phather_frame, shron, sw_row=0, sw_column=0):
        self.shron = shron
        self.switch_var = customtkinter.BooleanVar(value=str(shron.switch_shift_alt_config))  # Инициализируем переменную для хранения состояния переключателя
        self.switch_fraim = customtkinter.CTkSwitch(phather_frame, text=str(shron.switch_shift_alt_config), variable=self.switch_var,
                                                              command=lambda: self.switch_event(sw_var=self.switch_var,
                                                                                                 switch_pointer=self.switch_fraim))
        self.switch_fraim.grid(row=sw_row, column=sw_column, padx=10, pady=(0, 10), sticky="w")
        self.tooltip_fraim = CTkToolTip(self.switch_fraim, border_width=1, message=(f"Нажмите, чтобы {'включить' if self.switch_var.get() == False else 'отключить'}"))
        # if self.baf_state.switch_side:
        #    self.switch_fraim.select()

    # Функция для изменения текста переключателя и его тултипа в зависимости от текущего состояния
    def switch_event(self, sw_var, switch_pointer):
        # Изменение состояния переключателя и сохранение его в конфиге
        self.shron.switch_shift_alt_config = sw_var.get()
        print(self.shron.switch_shift_alt_config)
        # self.push_config_file(self.shron.atreibute_list_value())

        if sw_var.get() == True:
            switch_pointer.configure(text="Вкл.")
            new_tooltip = "Нажмите, чтобы отключить"
        else:
            switch_pointer.configure(text="Откл.")
            new_tooltip = "Нажмите, чтобы включить"
        self.tooltip_fraim.configure(message=new_tooltip)

class TranslyGUI(customtkinter.CTk):
    '''
    Class for 
    '''
    def __init__(self, shron, icon_path, push_config_file, icon, menu, item):
        customtkinter.set_widget_scaling(0.85)
        super().__init__()

        self.shron = shron
        self.icon_path = icon_path
        self.push_config_file = push_config_file
        self.icon = icon
        self.menu = menu
        self.item = item

        self.iconbitmap(icon_path)
        self.title("Transly")
        self.geometry("400x330")

        self.frame = customtkinter.CTkFrame(self, height=100, fg_color="red")
        self.frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.switch_alt_shift = Switchpool(self, self.shron, sw_row=2, sw_column=2)



def main():
    VALUE_LIST = {
        "hot_key_layout": HOT_KEY_LAYOUT,
        "hot_key_translate": HOT_KEY_TRANSLATION,
        "language_en": LANGUAGE_EN,
        "language_ru": LANGUAGE_RU,
        "simvol_alphabet_language": ALPHABET_LANGUAGE,
        "switch_shift_alt_config": SWITCH_SIFT_ALT
    }
    shron = BacupsShron()
    tjson = TransJson()
    tjson.setting_attributes(shron, VALUE_LIST, tjson.file_icon_path("favicon.ico", "img"), tjson.file_config_path("config.json", ".transly"))
    tlay = TransLayout(shron)
    tlay.check_hotkey() #hot-key check
    app = TranslyGUI(shron, tjson.icon_path, tjson.push_config_file, icon, menu, item)
    app.mainloop()


if __name__ == "__main__":
    main()
