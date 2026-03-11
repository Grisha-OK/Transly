from Transly import TransLayout, SwitchState
import clipboard  # Оставляем импорт

AIL_ALPHABET_LANGUAGE = {
    # ... твой огромный словарь (без изменений) ...
}
dictionary = AIL_ALPHABET_LANGUAGE

# ... переменные HOT_KEY и fake_swof ...
HOT_KEY_LAYOUT = ("ctrl + F9")
hot_key_n1 = HOT_KEY_LAYOUT

HOT_KEY_TRANSLATION = ("ctrl + F8")
hot_key_n2 = HOT_KEY_TRANSLATION

LANGUAGE_EN = ("en")
LANGUAGE_RU = ("ru")

fake_swof = SwitchState()

fake_tjson = type('TransJson', (object,), {
    "hot_key_n1": hot_key_n1, 
    "hot_key_n2": hot_key_n2, 
    "dictionary": dictionary, 
    "baf_state": fake_swof,
    "language_1" : LANGUAGE_EN,
    "language_2" : LANGUAGE_RU
})()

# Оставляем эти тесты, которые были в HEAD
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