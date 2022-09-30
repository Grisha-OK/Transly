# Импортируем модули для пере-трансляции и кравиатуры
from time import time
from unittest.util import strclass
import pandas as pd
from tkinter import Tk  
import keyboard
# Импортируем модули для добавления иконки в системном трее
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

# Алфавит для перевода
alphabet_language = {
    "ё": "`", "Ё": "~", "й": "q", "Й": "Q", "ц": "w", "Ц": "W", "у": "e", "У": "E", "к": "r", "К": "R", "е": "t", "Е": "T", "н": "y", "Н": "Y", "г": "u", "Г": "U", "ш": "i",
     "Ш": "I", "щ": "o", "Щ": "O", "з": "p", "З": "P", "х": "[", "Х": "{", "ъ": "]", "Ъ": "}", "ф": "a", "Ф": "A", "ы": "s", "Ы": "S", "в": "d", "В": "D", "а": "f", "А": "F", "п": "g", "П": "G",
      "р": "h", "Р": "H", "о": "j", "О": "J", "л": "k", "Л": "K", "д": "l", "Д": "L", "ж": ";", "Ж": ":", "э": "'", "Э": '"', "я": "z", "Я": "Z", "ч": "x", "Ч": "X", "с": "c", "С": "C", "м": "v",
       "М": "V", "и": "b", "И": "B", "т": "n", "Т": "N", "ь": "m", "Ь": "M", "б": ",", "Б": "<", "ю": ".", "Ю": ">", 
        '`': 'ё', '~': 'Ё', 'q': 'й', 'Q': 'Й', 'w': 'ц', 'W': 'Ц', 'e': 'у', 'E': 'У', 'r': 'к', 'R': 'К', 't': 'е', 'T': 'Е', 'y': 'н', 'Y': 'Н', 'u': 'г', 'U': 'Г', 'i': 'ш',
         'I': 'Ш', 'o': 'щ', 'O': 'Щ', 'p': 'з', 'P': 'З', '[': 'х', '{': 'Х', ']': 'ъ', '}': 'Ъ', 'a': 'ф', 'A': 'Ф', 's': 'ы', 'S': 'Ы', 'd': 'в', 'D': 'В', 'f': 'а', 'F': 'А', 'g': 'п', 'G': 'П',
          'h': 'р', 'H': 'Р', 'j': 'о', 'J': 'О', 'k': 'л', 'K': 'Л', 'l': 'д', 'L': 'Д', ';': 'ж', ':': 'Ж', "'": 'э', '"': 'Э', 'z': 'я', 'Z': 'Я', 'x': 'ч', 'X': 'Ч', 'c': 'с', 'C': 'С', 'v': 'м',
           'V': 'М', 'b': 'и', 'B': 'И', 'n': 'т', 'N': 'Т', 'm': 'ь', 'M': 'Ь', ',': 'б', '<': 'Б', '.': 'ю', '>': 'Ю',
            '\n': '\n', '?': ',', ' ': ' '}

# Функцыя для копирования, пере-трансляции, сбоки и вставляния текста
def fast_name():
    time: (50)
    keyboard.send("ctrl+c")
    time: (50)
    ad = Tk().clipboard_get()
    re_print = ''
    for i in ad:
        re_print = str(re_print + alphabet_language[i])

    df=pd.DataFrame([re_print])
    df.to_clipboard(index=False,header=False)
    keyboard.send("ctrl+v")

# Проверка хот-кея
keyboard.add_hotkey("ctrl + y", lambda: fast_name())

# Создайте экземпляр фрейма или окна tkinter
win=Tk()
win.title("Trans Translation")

# Установите размер окна
win.geometry("200x50")

# Определите функцию для выхода из окна
def quit_window(icon, item):
   icon.stop()
   win.destroy()
   exit()

# Определите функцию для повторного отображения окна
def show_window(icon, item):
   icon.stop()
   win.after(0,win.deiconify())

# Скройте окно и покажите на системной панели задач
def hide_window():
   win.withdraw()
   image=Image.open("favicon.ico")
   menu=(item('Quit', quit_window), item('Show', show_window))
   icon=pystray.Icon("name", image, "My System Tray Icon", menu)
   icon.run()

win.protocol('WM_DELETE_WINDOW', hide_window)

win.mainloop()

keyboard.add_hotkey("ctrl + y", lambda: fast_name())
keyboard.wait()

