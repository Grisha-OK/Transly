import pytest
import shutil
import getpass
import random
import os
from pathlib import Path
from Transly import TransJson, SwitchState
from constant import *

# Списки доступных значений для рандома
POSSIBLE_HOTKEYS = ["ctrl + alt", "ctrl + F10", "alt + shift", "ctrl + shift", "cmd + space"]
POSSIBLE_LANGUAGES = ["en", "fi", "de", "fr"]

fake_swof = SwitchState()

def shuffle_alphabet(alphabet_dict):
    """
    Перемешивает ключи и значения словаря. 
    Берет все ключи, перемешивает их, берет все значения, перемешивает их, 
    и создает новый рандомный маппинг.
    """
    keys = list(alphabet_dict.keys())
    values = list(alphabet_dict.values())
    
    random.shuffle(keys)
    random.shuffle(values)
    
    return dict(zip(keys, values))

def we_compiled():
    path_to_main_file = os.path.realpath(__file__)
    if "Temp" in path_to_main_file: #condition for checking if the file is compiled
        return(True)
    else:
        return(False)
    
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

@pytest.mark.parametrize("alphabet_language, hot_key_layout, hot_key_translation, language_en, language_ru, switch_off", [
    (ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF),
    
    (shuffle_alphabet(ALPHABET_LANGUAGE), random.choice(POSSIBLE_HOTKEYS),random.choice(POSSIBLE_HOTKEYS),
      random.choice(POSSIBLE_LANGUAGES), random.choice(POSSIBLE_LANGUAGES), not(SWITCH_OFF)),
    
    (shuffle_alphabet(ALPHABET_LANGUAGE), random.choice(POSSIBLE_HOTKEYS),random.choice(POSSIBLE_HOTKEYS),
      random.choice(POSSIBLE_LANGUAGES), random.choice(POSSIBLE_LANGUAGES), (SWITCH_OFF))
])
def test_master_json_config_text(temp_folder_env, alphabet_language, hot_key_layout, hot_key_translation, language_en, language_ru, switch_off):
    # Подготавливаем путь (добавляем слеш для вашей функции)
    folder_arg = Path("test", temp_folder_env).resolve()
    
    tjson = TransJson(alphabet_language, hot_key_layout, hot_key_translation,
                      language_en, language_ru, switch_off)
    
    # Используем путь из фикстуры
    icon_path = tjson.file_icon_path("favicon_test.ico", folder_arg)
    config_path = tjson.file_config_path("config_test.json", '', folder_arg)

    tjson.setting_attributes(fake_swof, icon_path, config_path)
    
    # Проверка
    assert (tjson.json_worker())["alphabet_language"] == alphabet_language
    assert (tjson.json_worker())["hot_key_layout"] == hot_key_layout
    assert (tjson.json_worker())["hot_key_translation"] == hot_key_translation
    assert (tjson.json_worker())["language_en"] == language_en
    assert (tjson.json_worker())["language_ru"] == language_ru
    assert (tjson.json_worker())["switch_off"] == switch_off

    # Как только функция закончится, pytest вернется в фикстуру и выполнит shutil.rmtree