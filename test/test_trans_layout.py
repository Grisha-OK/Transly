from Transly import TransLayout, BacupsShron
from constant import *
import clipboard

VALUE_LIST = {
        "hot_key_layout": HOT_KEY_LAYOUT,
        "hot_key_translate": HOT_KEY_TRANSLATION,
        "language_en": LANGUAGE_EN,
        "language_ru": LANGUAGE_RU,
        "simvol_alphabet_language": ALPHABET_LANGUAGE,
        "switch_shift_alt_config": SWITCH_SIFT_ALT
    }
fake_shron = BacupsShron()
fake_shron.atribute_arow(VALUE_LIST)

def test_master_keyboard_worker():
    tl = TransLayout(fake_shron)
    assert tl.master_keyboard_worker("Hello World", False) == "Руддщ Цщкдв"

def test_master_keyboard_worker_with_hotkey():
    tl = TransLayout(fake_shron)
    clipboard.copy("Hello World!")
    assert tl.master_keyboard_worker(tl.selecting_text(), False) == "Руддщ Цщкдв!"

def test_master_transly_worker():
    tl = TransLayout(fake_shron)
    assert tl.master_transly_worker("Hello World", False) == "Привет, мир"