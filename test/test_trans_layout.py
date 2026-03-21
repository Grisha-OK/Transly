from Transly import TransLayout, SwitchState
from constant import *
import clipboard

dictionary = ALPHABET_LANGUAGE
hot_key_n1 = HOT_KEY_LAYOUT
hot_key_n2 = HOT_KEY_TRANSLATION
lan_en = LANGUAGE_EN
lan_ru = LANGUAGE_RU

fake_swof = SwitchState()

fake_tjson = type('TransJson', (object,), {
    "hot_key_n1": hot_key_n1, 
    "hot_key_n2": hot_key_n2, 
    "dictionary": dictionary, 
    "baf_state": fake_swof,
    "language_1" : lan_en,
    "language_2" : lan_ru
})()


def test_master_keyboard_worker():
    tl = TransLayout(fake_tjson)
    assert tl.master_keyboard_worker("Hello World", False) == "Руддщ Цщкдв"

def test_master_keyboard_worker_with_hotkey():
    tl = TransLayout(fake_tjson)
    clipboard.copy("Hello World!")
    assert tl.master_keyboard_worker(tl.selecting_text(), False) == "Руддщ Цщкдв!"

def test_master_transly_worker():
    tl = TransLayout(fake_tjson)
    assert tl.master_transly_worker("Hello World", False) == "Привет, мир"