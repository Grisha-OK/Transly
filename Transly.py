"""                                 
Прошу прощение за данное обращение :D
                                    
"""                                  
# pip install ...
import clipboard
import pystray
import keyboard
from pystray import MenuItem as item

# Импортируем стандартные модули python 
from PIL import Image
from tkinter import Tk, Button, Label, NORMAL, DISABLED, TOP
import json
import os
import sys
import getpass
import shutil

# Так называемый алфавит
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

# Функцыя для выхода из программы
def Functions_abort():
    os.abort()

# Функция бля создания папки хранения служебного файла 
def reate_a_folder():
    username = getpass.getuser()
    path = (f"C:/Users/{username}/AppData/Roaming/Transly/")
    try:
        os.makedirs(path)
        return(path)
    except:
        return(path)
path = reate_a_folder()

# Функцыя для поиска пути к дериктории файла
def file_path(tild):
    name_file = os.path.basename(__file__)
    path_to_file = os.path.realpath(__file__).replace(name_file, tild)
    if "Temp" in path_to_file: #условие для проверки скомпелированности файла
        return(path_to_file)
    else:  
        try:
            shutil.move(path_to_file, f"{path}/favicon.ico") #перемещение картинки в рабочую дерикторию
            return(f"{path}/favicon.ico")
        except:
            return(f"{path}/favicon.ico")

file_path = file_path("favicon.ico")
# Функция сборки текста для десериализации JSON
shron = {}
def mergiing(nomber, text):
    global shron
    shron[nomber] = text

# Функция для создания json и кодирования в него текста настроек
def json_worker(nomber):
    try:
        with open(f"{path}/dictionary.json", "r") as write_file: #фаил открыт только в конструкции with open
            interlayer = {}
            interlayer = json.loads(write_file.read())
            
            return(interlayer[str(nomber)]) 
    except FileNotFoundError:
        with open(f"{path}/dictionary.json", "w") as write_file:
            json.dump(dict(shron), write_file)
            return(shron[nomber])

mergiing(1, alphabet_language) 
mergiing(2, hot_key)        #вызов сборки текста для десериализации JSON
dictionary = json_worker(1) #вызов текста словаря
hot_key = json_worker(2)    #вызов текста hot-key

switching_the_layout = False #переменная для настройки переключения раскладки

# Функцыя для копирования, пере-трансляции, сбоки и вставляния текста
def fast_name():
    keyboard.send("ctrl+c")
    ad = Tk().clipboard_get()
    re_print = ''
    for i in ad:
        try:
            re_print = str(re_print + dictionary[i])
        except:
            re_print = re_print + i

    clipboard.copy(re_print)
    keyboard.send("ctrl+v")
    
    # Условие для переключения раскладки
    if switching_the_layout == True:
        keyboard.send("shift+alt")



# Проверка hot-key
def check_hotkey():
    try:
        keyboard.add_hotkey(hot_key, lambda: fast_name())
    except:
        return

# Создайте экземпляр фрейма или окна tkinter
win=Tk()
win.title("Transly")
win.iconbitmap(file_path)
win.geometry("204x90")

# Определите функцию для выхода из окна / и по совместительвству для выхода из всей программы
def quit_window(icon):
   icon.stop()
   Functions_abort()

# Определите функцию для повторного отображения окна
def show_window(icon):
    icon.stop()
    win.deiconify() #я пожалуй оставлю это здесь <win.after(0,win.deiconify())>

# Скройте окно и покажите на системной панели задач
def hide_window():
   win.withdraw()
   image = Image.open(file_path)
   menu = (item('Quit', lambda : quit_window(icon)), item('Show', lambda : show_window(icon)))
   icon = pystray.Icon("name", image, "Trans Translation", menu)
   icon.run()

# Добовление кнопки для выхода из программы
btn = Button(win, text="Закрыть программу", command = sys.exit)
btn.pack(side=TOP)

# Добавление отступа
lbl1 = Label(text="   ")  
lbl1.pack(side=TOP)
lbl2 = Label(text="Переключать раскладку")  
lbl2.pack(side=TOP)

# Добавление тумблера
def Simpletoggle():
    global switching_the_layout
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        switching_the_layout = False
    else:
        toggle_button.config(text='ON')
        switching_the_layout = True

# Конкретно сам тумблер:
toggle_button = Button(text="OFF", width=10, command=Simpletoggle)
toggle_button.pack(side=TOP)

# Иницилизация иконки трэя
win.protocol('WM_DELETE_WINDOW', hide_window)

check_hotkey() #провкрка хот-кея

win.mainloop() #главный цикл
