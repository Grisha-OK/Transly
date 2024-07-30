<br>

<div align="center">

  <h1 align="center">Transly</h1>
  
  <p align="center">
    <strong>Transly — инструмент для смены раскладки уже написанного текста.</strong>
  </p>

[![build](https://img.shields.io/badge/download-v1.3.exe-blue)](https://github.com/Grisha-OK/Transly/releases/download/Transly/Transly.v1.3exe.zip)
[![build](https://img.shields.io/badge/download-v1.3.py-green)](https://github.com/Grisha-OK/Transly/releases/download/Transly/Transly.v1.3py.zip)


   <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExenVvajBzN29pOG80Y3NhcG8yenZjdGQ0bGx3Z2toN3YzZHNhc3gyOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hU4XTtZIVDH1x3oAWp/giphy.gif" width="300" height="200"/>
   
</div>

<br>

## About

Программа Transly поможет вам при смене раскладки уже написанного текста.
Для этого вам следует выделить текст, который нуждается в смене раскладки, можно также воспользоваться комбинацией **< ctrl + a >**, для выделения всего текста в строке ввода,
далее чтобы Trans Translation выполнила свою главную функцию вам следует нажать комбинацию **< ctrl + F9 >** после чего программа сменит раскладку выделенного вами текста.

Также по этому пути: C:\Users\User\\\.transly создаётся файл настройки, в котором можно настроить комбинацию клавиш для работы программы,
а также если заморочиться можно заменить язык смены раскладки.

## Installation
1. __Скачать архив со скомпилированным exe файлом:__ [download](https://github.com/Grisha-OK/trans_translation/releases/tag/Trans)
   - Разархивируйте скачанный архив
   - Готово, запускайте и пользуйтесь

2. __Скачать архив с исходным Python файлом:__ [download](https://github.com/Grisha-OK/trans_translation/releases/tag/Trans)
   - Убедитесь, что на вашем компьютере установлен Python 3.12. Вы можете установить его с сайта [python.org](https://www.python.org/downloads/release/python-3913/).
   - Установить необходимые [библиотеки](#libraries) через командную строку cmd
   - Разархивируйте скачанный архив
   - Один раз запустить pyhon файл в папке с картинкой, командой **"C:\\\>python Transly.py"** через cmd в нужной директории или **через правую кнопку мышь > открыть с помощью > Python**
   - Программа готова к использованию

## Libraries
Кроссплатформенная библиотека операций с буфером обмена Python.
```bash
pip install clipboard
```
Эта библиотека позволяет создать значок в системном трее.
```bash
pip install pystray
```
Модуль для работы с клавиатурой Python.
```bash
pip install keyboard
```