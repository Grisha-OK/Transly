import pytest
import shutil
import os
from pathlib import Path
from Transly import TransJson, SwitchState
from constant import *

fake_swof = SwitchState()

def source_img(file):
    # Путь к текущему файлу (test_work_data.py)
    current_file = Path(__file__).resolve()
    # 1. Поднимаемся на уровень выше (в папку Transly)
    project_root = current_file.parent.parent 
    # 2. Заходим в соседнюю папку img
    target_folder = project_root / "img"
    # 3. Полный путь к файлу
    file_path = target_folder / file
    return str(file_path)

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
    folder_arg = Path("test", temp_folder_env).resolve()
    
    tjson = TransJson(ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, 
                      LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF)
    
    # Используем путь из фикстуры
    icon_path = tjson.file_icon_path("favicon_test.ico", folder_arg)
    config_path = tjson.file_config_path("config_test.json", '' ,folder_arg)

    tjson.setting_attributes(fake_swof, icon_path, config_path)
    
    # Проверка
    file_test_folder_ico = tjson.file_icon_path("favicon_test.ico", folder_arg)
    
    assert os.path.exists(file_test_folder_ico) is True
    # Как только функция закончится, pytest вернется в фикстуру и выполнит shutil.rmtree

def test_master_json_copy_icon(temp_folder_env):
    # Подготавливаем путь (добавляем слеш для вашей функции)
    folder_arg = Path("test", temp_folder_env).resolve()

    # Копируем файл в тестовую папку
    test_icon_path = Path(f"{folder_arg}\\favicon_test.ico")
    shutil.copy(source_img("favicon.ico"), test_icon_path)

    tjson = TransJson(ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, 
                  LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF)
    
    # Используем путь из фикстуры
    icon_path = tjson.file_icon_path("favicon_test.ico", folder_arg)
    config_path = tjson.file_config_path("config_test.json", '' ,folder_arg)

    tjson.setting_attributes(fake_swof, icon_path, config_path)

    # Проверка
    file_test_folder_ico = tjson.file_icon_path("favicon_test.ico", folder_arg)
    
    assert os.path.exists(file_test_folder_ico) is True
    # Как только функция закончится, pytest вернется в фикстуру и выполнит shutil.rmtree

def test_master_json_config(temp_folder_env):
    # Подготавливаем путь (добавляем слеш для вашей функции)
    folder_arg = Path("test", temp_folder_env).resolve()

    tjson = TransJson(ALPHABET_LANGUAGE, HOT_KEY_LAYOUT, HOT_KEY_TRANSLATION, 
                      LANGUAGE_EN, LANGUAGE_RU, SWITCH_OFF)
    
    # Используем путь из фикстуры
    icon_path = tjson.file_icon_path("favicon_test.ico", folder_arg)
    config_path = tjson.file_config_path("config_test.json", '' ,folder_arg)

    tjson.setting_attributes(fake_swof, icon_path, config_path)
    
    # Проверка
    file_test_folder_json = tjson.file_config_path("config_test.json", '' ,folder_arg)
    
    assert os.path.exists(file_test_folder_json) is True
    # Как только функция закончится, pytest вернется в фикстуру и выполнит shutil.rmtree