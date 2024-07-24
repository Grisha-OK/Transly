"""                                 
I apologize for this appeal :D
                                    
"""                                  
# pip install ...
import clipboard
import keyboard
import pystray

from pystray import MenuItem as item

# Import standard python modules
from PIL import Image
from tkinter import Tk, Button, Label, Menu, FALSE, TOP
import tkinter as tk
import json
import os
import sys
import getpass
import shutil
import ctypes

# So-called alphabet
alphabet_language = {
    "ё": "`", "Ё": "~", "й": "q", "Й": "Q", "ц": "w", "Ц": "W", "у": "e", "У": "E", "к": "r", "К": "R", "е": "t", "Е": "T", "н": "y", "Н": "Y", "г": "u", "Г": "U", "ш": "i",
     "Ш": "I", "щ": "o", "Щ": "O", "з": "p", "З": "P", "х": "[", "Х": "{", "ъ": "]", "Ъ": "}", "ф": "a", "Ф": "A", "ы": "s", "Ы": "S", "в": "d", "В": "D", "а": "f", "А": "F", "п": "g", "П": "G",
      "р": "h", "Р": "H", "о": "j", "О": "J", "л": "k", "Л": "K", "д": "l", "Д": "L", "ж": ";", "Ж": ":", "э": "'", "Э": '"', "я": "z", "Я": "Z", "ч": "x", "Ч": "X", "с": "c", "С": "C", "м": "v",
       "М": "V", "и": "b", "И": "B", "т": "n", "Т": "N", "ь": "m", "Ь": "M", "б": ",", "Б": "<", "ю": ".", "Ю": ">", 
        '`': 'ё', '~': 'Ё', 'q': 'й', 'Q': 'Й', 'w': 'ц', 'W': 'Ц', 'e': 'у', 'E': 'У', 'r': 'к', 'R': 'К', 't': 'е', 'T': 'Е', 'y': 'н', 'Y': 'Н', 'u': 'г', 'U': 'Г', 'i': 'ш',
         'I': 'Ш', 'o': 'щ', 'O': 'Щ', 'p': 'з', 'P': 'З', '[': 'х', '{': 'Х', ']': 'ъ', '}': 'Ъ', 'a': 'ф', 'A': 'Ф', 's': 'ы', 'S': 'Ы', 'd': 'в', 'D': 'В', 'f': 'а', 'F': 'А', 'g': 'п', 'G': 'П',
          'h': 'р', 'H': 'Р', 'j': 'о', 'J': 'О', 'k': 'л', 'K': 'Л', 'l': 'д', 'L': 'Д', ';': 'ж', ':': 'Ж', "'": 'э', '"': 'Э', 'z': 'я', 'Z': 'Я', 'x': 'ч', 'X': 'Ч', 'c': 'с', 'C': 'С', 'v': 'м',
           'V': 'М', 'b': 'и', 'B': 'И', 'n': 'т', 'N': 'Т', 'm': 'ь', 'M': 'Ь', ',': 'б', '<': 'Б', '.': 'ю', '>': 'Ю',
            "\n": "\n", '?': ',', " ": " "}

hot_key = ("ctrl + F9")

# Function to create a folder for storing the service file
def reate_a_folder():
    username = getpass.getuser()
    path = (f"C:/Users/{username}/.transly/")
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
    else:  
        try:
            shutil.move(path_to_file, f"{path}/img/favicon.ico") #move the picture to the working directory
            return(f"{path}/img/favicon.ico")
        except:
            return(f"{path}/img/favicon.ico")
file_icon_path = file_path("favicon.ico")

# Function to assemble text for JSON deserialization
shron = {}
def mergiing(nomber, text):
    global shron
    shron[nomber] = text

# Function to create json and encode text settings in it
def json_worker(nomber):
    try:
        with open(f"{path}/dictionary.json", "r") as write_file: #file opened only in the with open construct
            interlayer = {}
            interlayer = json.loads(write_file.read())
            return(interlayer[str(nomber)]) 
    
    except FileNotFoundError:
        with open(f"{path}/dictionary.json", "w") as write_file:
            json.dump(dict(shron), write_file)
            return(shron[nomber])

mergiing(1, alphabet_language) #call the text assembly for JSON deserialization with key 1 and value alphabet_language
mergiing(2, hot_key)           #call the text assembly for JSON deserialization with key 2 and value hot_key
dictionary = json_worker(1)    #call the dictionary text
hot_key = json_worker(2)       #call the hot-key text

switching_the_layout = False #variable for setting up the layout switch

# Function for copying, translating, assembling and pasting text
def fast_name():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # Ctrl down
    ctypes.windll.user32.keybd_event(0x43, 0, 0, 0)  # C down
    ctypes.windll.user32.keybd_event(0x43, 0, 2, 0)  # C up
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # Ctrl up
    ad = Tk().clipboard_get()
    re_print = ''
    
    #preparing the copied text
    for i in ad:
        try:
            re_print = str(re_print + dictionary[i])
        except:
            re_print = re_print + i

    clipboard.copy(re_print)  #add the finished text to the clipboard
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # Ctrl down
    ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)  # V down
    ctypes.windll.user32.keybd_event(0x56, 0, 2, 0)  # V up
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # Ctrl up
    
    if switching_the_layout == True: #condition for switching the layout
        ctypes.windll.user32.keybd_event(0x10, 0, 0, 0)  # Shift down
        ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # Alt down
        ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)  # Alt up
        ctypes.windll.user32.keybd_event(0x10, 0, 2, 0)  # Shift up

# Hot-key check
def check_hotkey():
    try:
        keyboard.add_hotkey(hot_key, lambda: fast_name())
    except:
        return

# Create an instance of the tkinter frame or window
win = Tk()
win.title("Transly")
win.iconbitmap(file_icon_path)
win.geometry("200x90")
win.option_add("*tearOff", FALSE)

# Define a function to exit the window / and by compatibility for exiting the entire program
def quit_window(icon):
   icon.stop()
   os.abort()

# A function for re-displaying the window
def show_window(icon):
    icon.stop()
    win.deiconify() #I'll probably leave it here <win.after(0,win.deiconify())>

# Hide the window and show it on the system taskbar
def hide_window():
   win.withdraw()
   image = Image.open(file_icon_path)
   menu = (item('Quit', lambda : quit_window(icon)), item('Show', lambda : show_window(icon)))
   icon = pystray.Icon("name", image, "Trans Translation", menu)
   icon.run()

# Add a toggle
def Simpletoggle():
    global switching_the_layout
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        switching_the_layout = False
    else:
        toggle_button.config(text='ON')
        switching_the_layout = True

# Function to open the directory where service files are stored
def os_srart():
    os.startfile(path)

# Add a separating border
frame = tk.Frame(master=win, relief=tk.RAISED, borderwidth=1)
frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# Add Header menu
main_menu = Menu()
file_menu = Menu()

# Initialize under the menu
file_menu.add_command(label="Open option", command = os_srart)
file_menu.add_separator()
file_menu.add_command(label="Quit", command = sys.exit)

# The menu itself is from one component
main_menu.add_cascade(label="File", menu=file_menu)
win.config(menu=main_menu)

# Add indentation
lbl1 = Label(frame, text="Changing the layout:").pack(side=TOP, pady=0)
lbl2 = Label(win, text="   ").pack(side=TOP, pady=0)

# Add a button to exit the program
btn = Button(text="Quit", bg='gray64', command = sys.exit)
btn.pack(side=TOP, padx=(10,10), pady=(0,20), ipadx=5, ipady=5)

# Specifically the toggle itself:
toggle_button = Button(frame, text="OFF", width=10, command=Simpletoggle)
toggle_button.pack(side=TOP)

# Initialize the tray icon
win.protocol('WM_DELETE_WINDOW', hide_window)

check_hotkey() #hot-key check

win.mainloop() #main loop