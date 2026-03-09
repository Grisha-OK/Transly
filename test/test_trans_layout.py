from Transly import TransLayout, SwitchState
<<<<<<< HEAD
import clipboard
=======
>>>>>>> f4100de (Add requirement files and prepare test_trans_layout.py for writing unit tests)

AIL_ALPHABET_LANGUAGE = {
    "ё": "`", "Ё": "~", "й": "q", "Й": "Q", "ц": "w", "Ц": "W", "у": "e", "У": "E", "к": "r", "К": "R", "е": "t", "Е": "T", "н": "y", "Н": "Y", "г": "u", "Г": "U", "ш": "i",
     "Ш": "I", "щ": "o", "Щ": "O", "з": "p", "З": "P", "х": "[", "Х": "{", "ъ": "]", "Ъ": "}", "ф": "a", "Ф": "A", "ы": "s", "Ы": "S", "в": "d", "В": "D", "а": "f", "А": "F", "п": "g", "П": "G",
      "р": "h", "Р": "H", "о": "j", "О": "J", "л": "k", "Л": "K", "д": "l", "Д": "L", "ж": ";", "Ж": ":", "э": "'", "Э": '"', "я": "z", "Я": "Z", "ч": "x", "Ч": "X", "с": "c", "С": "C", "м": "v",
       "М": "V", "и": "b", "И": "B", "т": "n", "Т": "N", "ь": "m", "Ь": "M", "б": ",", "Б": "<", "ю": ".", "Ю": ">", 
        '`': 'ё', '~': 'Ё', 'q': 'й', 'Q': 'Й', 'w': 'ц', 'W': 'Ц', 'e': 'у', 'E': 'У', 'r': 'к', 'R': 'К', 't': 'е', 'T': 'Е', 'y': 'н', 'Y': 'Н', 'u': 'г', 'U': 'Г', 'i': 'ш',
         'I': 'Ш', 'o': 'щ', 'O': 'Щ', 'p': 'з', 'P': 'З', '[': 'х', '{': 'Х', ']': 'ъ', '}': 'Ъ', 'a': 'ф', 'A': 'Ф', 's': 'ы', 'S': 'Ы', 'd': 'в', 'D': 'В', 'f': 'а', 'F': 'А', 'g': 'п', 'G': 'П',
          'h': 'р', 'H': 'Р', 'j': 'о', 'J': 'О', 'k': 'л', 'K': 'Л', 'l': 'д', 'L': 'Д', ';': 'ж', ':': 'Ж', "'": 'э', '"': 'Э', 'z': 'я', 'Z': 'Я', 'x': 'ч', 'X': 'Ч', 'c': 'с', 'C': 'С', 'v': 'м',
           'V': 'М', 'b': 'и', 'B': 'И', 'n': 'т', 'N': 'Т', 'm': 'ь', 'M': 'Ь', ',': 'б', '<': 'Б', '.': 'ю', '>': 'Ю',
            "\n": "\n", '?': ',', " ": " "}
dictionary = AIL_ALPHABET_LANGUAGE

HOT_KEY_LAYOUT = ("ctrl + F9")
hot_key_n1 = HOT_KEY_LAYOUT

HOT_KEY_TRANSLATION = ("ctrl + F8")
hot_key_n2 = HOT_KEY_TRANSLATION


fake_swof = SwitchState()

fake_tjson = type('TransJson', (object,), {
    "hot_key_n1": hot_key_n1, 
    "hot_key_n2": hot_key_n2, 
    "dictionary": dictionary, 
    "baf_state": fake_swof
<<<<<<< HEAD
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
=======
})()
>>>>>>> f4100de (Add requirement files and prepare test_trans_layout.py for writing unit tests)
