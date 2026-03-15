import pytest
import shutil
import getpass
import os
from Transly import TransJson, SwitchState


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

fake_swof = SwitchState()

def we_compiled():
    path_to_main_file = os.path.realpath(__file__)
    if "Temp" in path_to_main_file: #condition for checking if the file is compiled
        return(True)
    else:
        return(False)

def file_icon_path(file, folder_path = None):
    name_file = os.path.basename(__file__)
    if we_compiled(): #condition for checking if the file is compiled
        path_to_icon_config = (os.path.realpath(__file__).replace(name_file, file))
        return(path_to_icon_config)
    else:
        path_to_icon_config = (os.path.realpath(__file__).replace(name_file, folder_path+file))
        return(path_to_icon_config)
    
def file_config_path(file, folder_path = ''):
    '''
    Function to find the path to the file config directory, which is used to store the settings of the program
    file - the name of the config file
    #folder_path - the path to the folder where the config file is stored
    '''
    name_file = os.path.basename(__file__)
    if we_compiled(): #condition for checking if the file is compiled
        return((f"C:/Users/{getpass.getuser()}/.transly")+file)
    else:
        path_to_json_config = (os.path.realpath(__file__).replace(name_file, folder_path))
        return((path_to_json_config)+(file))
    


@pytest.fixture
def temp_folder_env():
    """Фикстура для создания и автоматической очистки тестовой папки."""
    print("Создаю временную папку для теста...")
    folder_name = "temp_test_folder"
    # Путь относительно папки с тестом
    base_path = os.path.join(os.path.dirname(__file__), folder_name)
    
    # Код до yield — выполняется ПЕРЕД тестом
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    yield folder_name  # Передаем имя папки в тест
    
    print("Тест завершен. Удаляю временную папку...")
    # Код после yield — выполняется ПОСЛЕ теста (даже если тест упал)
    full_path = os.path.join(os.path.dirname(__file__), folder_name)
    if os.path.exists(full_path):
        shutil.rmtree(full_path)

def test_master_json_icon(temp_folder_env):
    # Подготавливаем путь (добавляем слеш для вашей функции)
    folder_arg = f"{temp_folder_env}\\"
    
    tjson = TransJson(ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, 
                      LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF)
    
    # Используем путь из фикстуры
    icon_path = tjson.file_icon_path("favicon_test.ico", f"test\\{folder_arg}")
    config_path = tjson.file_config_path("config_test.json", f"test\\{folder_arg}")
    
    tjson.setting_attributes(fake_swof, icon_path, config_path)
    
    # Проверка
    file_test_folder_ico = file_icon_path("favicon_test.ico", folder_arg)
    
    assert os.path.exists(file_test_folder_ico) is True
    # Как только функция закончится, pytest вернется в фикстуру и выполнит shutil.rmtree

def test_master_json_config(temp_folder_env):
    # Подготавливаем путь (добавляем слеш для вашей функции)
    folder_arg = f"{temp_folder_env}\\"
    
    tjson = TransJson(ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, 
                      LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF)
    
    # Используем путь из фикстуры
    icon_path = tjson.file_icon_path("favicon_test.ico", f"test\\{folder_arg}")
    config_path = tjson.file_config_path("config_test.json", f"test\\{folder_arg}")
    
    tjson.setting_attributes(fake_swof, icon_path, config_path)
    
    # Проверка
    file_test_folder_json = file_config_path("config_test.json", folder_arg)
    
    assert os.path.exists(file_test_folder_json) is True
    # Как только функция закончится, pytest вернется в фикстуру и выполнит shutil.rmtree