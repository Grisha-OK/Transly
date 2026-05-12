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
import ctypes
import sys

# GUI modules
from tkinter import Tk, IntVar
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
SWITCH_SHIFT_ALT = False #variable for setting up the layout switch
SWITCH_CTRL_A = False #variable for setting up the text selection switch

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
                raise EOFError(f"Allarm: Attribute {attr} not found in the current object")
                # print(f"Предупреждение: Атрибут {attr} не найден в текущем объекте")

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
            # print(f"Запущено из скомпилированного файла (PyInstaller), по пути: {path_to_main_file}")
            return(True)
        else:
            # Если это обычный .py файл
            # print(f"Запущено как обычный скрипт Python, по пути: {path_to_main_file}")
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
                # print(f"Иконка не найдена. Создаю иконку по пути: {path_to_target_file}")
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
                   # print("превышено количество попыток получения текста из буфера обмена")
                   return(clipboard.paste())
               if self.shron.switch_ctrl_a_config and copy == True:
                   CTRL_A()
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
    def __init__(self, phather_frame, shadow_text_list, shron, switch_attribut_setattr, sw_row=0, sw_column=0):
        '''
        Class for creating a switch and working with it, which is used to change the state of the switch and save it in the general storage class
        phather_frame - the frame in which the switch will be placed, which is used to create a switch and place it in the GUI
        shadow_text_list - the list of text for the switch and its tooltip, which is used to change the text of the switch and its tooltip depending on the current state of the switch
        shron - the general storage class, which is used to save the state of the switch and other settings of the program
        switch_attribut_setattr - the name of the attribute in the general storage class, which is used to save the state of the switch and other settings of the program
        sw_row - the row in which the switch will be placed, which is used to create a switch and place it in the GUI
        sw_column - the column in which the switch will be placed, which is used to create a switch and place it in the GUI
        '''
        if str(getattr(shron, switch_attribut_setattr)) == "True":
            text_on_off = "Вкл."
        else:
            text_on_off = "Откл."
        self.show_text(shadow_text_list)
        self.shron = shron
        self.switch_var = customtkinter.BooleanVar(value=str(getattr(shron, switch_attribut_setattr)))  # Инициализируем переменную для хранения состояния переключателя
        self.switch_fraim = customtkinter.CTkSwitch(
            phather_frame, 
            text=(self.text_on if self.switch_var.get() == True else self.text_off), 
            variable=self.switch_var,
            command=lambda: self.switch_event(
                sw_var=self.switch_var,
                switch_attribut_setattr=switch_attribut_setattr))
        self.switch_fraim.grid(row=sw_row, column=sw_column, padx=20, pady=(0, 10), sticky="w")
        self.tooltip_fraim = CTkToolTip(self.switch_fraim, border_width=1, message=(self.tooltip_on if self.switch_var.get() == True else self.tooltip_off))
    
    def show_text(self, shadow_text_list):
        self.text_on = shadow_text_list["true"]["text"]
        self.text_off = shadow_text_list["false"]["text"]
        self.tooltip_on = shadow_text_list["true"]["tooltip"]
        self.tooltip_off = shadow_text_list["false"]["tooltip"]

    # Function for changing the text of a switch and its tooltip depending on the current state of the switch, as well as for changing the value of the switch in the general storage class
    def switch_event(self, sw_var, switch_attribut_setattr):
        '''
        Function for changing the text of a switch and its tooltip depending on the current state of the switch, as well as for changing the value of the switch in the general storage class
        sw_var - the variable that stores the state of the switch, which is used to change the text of the switch and its tooltip depending on the current state of the switch
        switch_attribut_setattr - the name of the attribute in the general storage class, which is used to save the state of the switch and other settings of the program, 
        which is used to change the value of the switch in the general storage class
        '''
        setattr(self.shron, switch_attribut_setattr, sw_var.get())
        if sw_var.get() == True:
            self.new_text = self.text_on
            self.new_tooltip = self.tooltip_on
        else:
            self.new_text = self.text_off
            self.new_tooltip = self.tooltip_off

        self.switch_fraim.configure(text=self.new_text)
        self.tooltip_fraim.configure(message=self.new_tooltip)

class RadiouttonPool:
    def __init__(self, phather_frame, shadow_text_list, shron, radio_button_attribut_setattr, gui_obj, attr_value, radio_value, rb_row=0, rd_column=0):
        self.show_text(shadow_text_list)
        self.shron = shron
        self.radio_attr = radio_button_attribut_setattr
        self.obj_value = gui_obj # Ссылка на главный класс, где лежит переменная
        self.radio_button_var = getattr(gui_obj, attr_value)
        
        # Упрощаем определение текста
        #self.text_on_off = "On" if bool(getattr(shron, radio_button_attribut_setattr)) else "Off"

        self.radio_button_fraim = customtkinter.CTkRadioButton(
            phather_frame, 
            text=(self.text_on if self.radio_button_var.get() == radio_value else self.text_off), 
            variable=self.radio_button_var, 
            value=radio_value,
            command=self.update_all_tooltips # Вызываем метод обновления всех
        )
        self.radio_button_fraim.grid(row=rb_row, column=rd_column, padx=30, pady=(0, 10), sticky="w")
        
        self.tooltip_fraim = CTkToolTip(
            self.radio_button_fraim, 
            border_width=1, 
            message=(self.tooltip_on if self.radio_button_var.get() == radio_value else self.tooltip_off)
        )

    def show_text(self, shadow_text_list):
        self.text_on = shadow_text_list["true"]["text"]
        self.text_off = shadow_text_list["false"]["text"]
        self.tooltip_on = shadow_text_list["true"]["tooltip"]
        self.tooltip_off = shadow_text_list["false"]["tooltip"]

    def set_list_radio_pools(self, list_radio_buttons):
        '''
        The method for setting the list of radio button pools, which is used to update the text of all radio buttons and their tooltips in the pool when the state of one of the radio buttons changes
        list_radio_buttons - the name of the attribute in the main class, which is used to store the list of radio button pools, which is used to update the text of all radio buttons and their tooltips in the pool when the state of one of the radio buttons changes
        '''
        self.list_radio_pools = getattr(self.obj_value, list_radio_buttons)

    def update_all_tooltips(self):
        '''
        The method that updates the text of all radio buttons and their tooltips in the pool, as well as updates the value of the radio button in the general storage class
        '''
        setattr(self.shron, self.radio_attr, self.radio_button_var.get())
        for pool_item in self.list_radio_pools:
            pool_item.refresh_tooltip_text()

    def refresh_tooltip_text(self):
        '''
        The method that updates the text of the radio button and its tooltip depending on the current state of the radio button
        '''
        self.is_active = self.radio_button_var.get() == self.radio_button_fraim.cget("value")
        if self.is_active:
            self.new_text = self.text_on
            self.new_tooltip = self.tooltip_on
        else:
            self.new_text = self.text_off
            self.new_tooltip = self.tooltip_off

        self.radio_button_fraim.configure(text=self.new_text)
        self.tooltip_fraim.configure(message=self.new_tooltip)

class TranslyGUI(customtkinter.CTk):
    def __init__(self, shron, icon_path, push_config_file, icon, menu, item):
        '''
        Class for creating the main GUI window for the Transly application.
        shron - the object for saving and storaging sistem variable
        icon_path - the path to the file icon directory, which is used to store the icon of the program in the system tray
        push_config_file - the function for writing the settings of the program to a JSON file, which is used to store the settings of the program
        icon - the class for creating an icon for the program in the system tray, which is used to create an icon for the program in the system tray
        menu - the class for creating a menu for the program in the system tray, which is used to create a menu for the program in the system tray
        item - the class for creating a menu item for the program in the system tray, which is used to create a menu item for the program in the system tray
        '''
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

        # configure main window grid so tabview stays at top and extra space is below
        self.grid_rowconfigure(0, weight=1)  # табвью
        self.grid_rowconfigure(1, weight=0)  # футер
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, height=0)
        self.tabview.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")
        self.tabview.grid_rowconfigure(3, weight=1)  # content row inside Home
        self.tabview.grid_columnconfigure(0, weight=1)
        self.tabview.add("Home")
        self.tabview.add("Settings")
        self.tabview.add("Stayle")
        self.tabview.tab("Home").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Home").grid_rowconfigure(2, weight=1)
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Stayle").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Stayle").grid_rowconfigure(0, weight=1)

        # Create a frame with text on the first tab
        self.lable_frame = customtkinter.CTkFrame(self.tabview.tab("Home"), height=100, fg_color=("gray75", "gray25"), corner_radius=5)
        self.lable_frame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsew")
        self.lable_frame.grid_columnconfigure(0, weight=1)
        self.lable_frame.grid_columnconfigure(1, weight=1)
        self.lable_text = customtkinter.CTkLabel(self.lable_frame, text="This is program for change layout and language\nfor charging layout and language press hotkeys")
        self.lable_text.grid(row=0, column=1, padx=20, pady=(10, 10), sticky="w")

        # Create a frame with switches on the first tab
        self.switch_frame = customtkinter.CTkFrame(self.tabview.tab("Home"), height=50, fg_color=("gray75", "gray25"), corner_radius=5)
        self.switch_frame.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="nsew")
        #self.switch_frame.grid_columnconfigure(0, weight=1)

        with_ext_select = {
                    "true":{
                        "text": "On.", 
                        "tooltip": "Auto press ctrl + a, for auto selection text: on"
                        },
                    "false":{
                        "text": "Off.", 
                        "tooltip": "Auto press ctrl + a, for auto selection text: off"}}
        with_trans_layout = {
                  "true":{
                      "text": "On.", 
                      "tooltip": "Auto press ctrl + shift, for translate layout: on"
                      }, 
                  "false":{
                      "text": "Off.", 
                      "tooltip": "Auto press ctrl + shift, for translate layout: off"}}
        
        # Text and switch for text selection
        self.lable_text_select = customtkinter.CTkLabel(self.switch_frame, text="Auto selection text")
        self.lable_text_select.grid(row=0, column=1, padx=20, pady=(10, 0), sticky="w")
        # Switch one
        self.switch_text_selection = Switchpool(self.switch_frame, with_ext_select, self.shron, switch_attribut_setattr="switch_ctrl_a_config", sw_row=1, sw_column=1)
        
        # Text and switch for layout switching
        self.lable_trans_layout = customtkinter.CTkLabel(self.switch_frame, text="Auto translate layout")
        self.lable_trans_layout.grid(row=2, column=1, padx=20, pady=(0, 0), sticky="w")  
        # Switch two
        self.switch_trans_layout = Switchpool(self.switch_frame, with_trans_layout, self.shron, switch_attribut_setattr="switch_shift_alt_config", sw_row=3, sw_column=1)

        # Red frame for checking the correct placement of switches and text, which will be removed in the future
        # self.jangle_patch = customtkinter.CTkFrame(self.switch_frame, height=0, fg_color=("red"))
        # self.jangle_patch.grid(row=4, column=1, padx=435, pady=0, sticky="w")
        
        # Create a frame with options on the second tab
        self.frame_settings_tab = customtkinter.CTkFrame(self.tabview.tab("Settings"), fg_color=("gray75", "gray25"), corner_radius=5)
        self.frame_settings_tab.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")

        self.frame_autostart = customtkinter.CTkFrame(self.frame_settings_tab, height=50, fg_color=("gray75", "gray25"), corner_radius=5)
        self.frame_autostart.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")
        self.frame_autostart.grid_columnconfigure(0, weight=1)
        self.frame_autostart.grid_columnconfigure(1, weight=1)

        self.lable_autostart = customtkinter.CTkLabel(self.frame_autostart, text="Launch Transly")
        self.lable_autostart.grid(row=0, column=0, padx=10, pady=(2, 1), sticky="w")

        self.radio_button_var = customtkinter.BooleanVar(value=shron.radio_autostart_config)
        
        self.all_radio_pools = []

        with_window = {
                    "true":{
                        "text": "Windowed mode", 
                        "tooltip": "Run an application in windowed mode: on"
                        },
                    "false":{
                        "text": "Windowed mode", 
                        "tooltip": "Run an application in windowed mode: off"}}
        with_tray = {
                  "true":{
                      "text": "Tray mode", 
                      "tooltip": "Run an application in tray mode: on"
                      }, 
                  "false":{
                      "text": "Tray mode", 
                      "tooltip": "Run an application in tray mode: off"}}
        
        self.tray_start_on = RadiouttonPool(self.frame_autostart, with_window, self.shron, "radio_autostart_config", self, "radio_button_var", True, rb_row=1, rd_column=0)
        self.tray_start_off = RadiouttonPool(self.frame_autostart, with_tray, self.shron, "radio_autostart_config", self, "radio_button_var", False, rb_row=2, rd_column=0)
        
        self.all_radio_pools.extend([self.tray_start_on, self.tray_start_off])
        self.tray_start_off.set_list_radio_pools("all_radio_pools")
        self.tray_start_on.set_list_radio_pools("all_radio_pools")

        # Create a frame with options on the third tab
        self.frame_stayle_tab = customtkinter.CTkFrame(self.tabview.tab("Stayle"), fg_color=("gray75", "gray25"), corner_radius=5)
        self.frame_stayle_tab.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")

        # Create a frame with options on the third tab
        self.option_menu_1 = customtkinter.CTkOptionMenu(self.frame_stayle_tab, dynamic_resizing=False,
                                                        values=["System", "Light", "Dark"],
                                                        command=self.change_appearance_mode_event)
        self.option_menu_1.grid(row=0, column=0, padx=20, pady=(35, 10))
        self.option_menu_2 = customtkinter.CTkOptionMenu(self.frame_stayle_tab, dynamic_resizing=False,
                                                        values=["english", "Russian"],
                                                        command=self.change_appearance_mode_event)
        self.option_menu_2.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.option_menu_3 = customtkinter.CTkOptionMenu(self.frame_stayle_tab, dynamic_resizing=False,
                                                        values=["normal", "aero", "win7"],
                                                        command=self.change_appearance_mode_event)
        self.option_menu_3.grid(row=2, column=0, padx=20, pady=(10, 10))
        
        # Footer with a button to exit the program
        self.footer_frame = customtkinter.CTkFrame(self, fg_color=None, corner_radius=5)
        self.footer_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        self.footer_frame.grid_columnconfigure(0, weight=1)
        
        # Button to exit the program for footer frame
        self.quit_button = customtkinter.CTkButton(self.footer_frame, text="Quit", fg_color=None, hover_color="#ff5c5c", command=self.quit_and_push)
        self.quit_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.setup_tray()

    # Function for changing the appearance of the program
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Check window closing and tray icon initialization
    def setup_tray(self):
        self.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.push_config_file(self.shron.atreibute_list_value())
    
    # Hide the window and show it on the system taskbar
    def hide_window(self):
       self.withdraw()
       image = Image.open(self.icon_path)
       menu = (item('Quit', lambda : self.quit_window()),
               item('Show', lambda : self.show_window()))
       self.icon = icon("name", image, "Trans Translation", menu)
       self.icon.run()
    
    # Define a function to exit the window / and by compatibility for exiting the entire program
    def quit_window(self):
           self.icon.stop()
           os.abort()

    def quit_and_push(self):
        super().quit()
        self.push_config_file(self.shron.atreibute_list_value())
    
    # A function for re-displaying the window
    def show_window(self):
        self.icon.stop()
        self.deiconify() #I'll probably leave it here <win.after(0,win.deiconify())>

    def run(self):
        self.mainloop() 

def main():
    VALUE_LIST = {
        "hot_key_layout": HOT_KEY_LAYOUT,
        "hot_key_translate": HOT_KEY_TRANSLATION,
        "language_en": LANGUAGE_EN,
        "language_ru": LANGUAGE_RU,
        "simvol_alphabet_language": ALPHABET_LANGUAGE,
        "switch_shift_alt_config": SWITCH_SHIFT_ALT,
        "switch_ctrl_a_config": SWITCH_CTRL_A,
        "radio_autostart_config": True
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
