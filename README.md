# Тестовое приложение PyQt5

Небольшое настольное приложение: введите имя и нажмите «Поздороваться»
или Enter. Окно покажет приветствие и число нажатий. Если имя пустое,
приложение поприветствует мир.

## Запуск

Требуется Python 3.9 или новее и графическая среда рабочего стола.

```bash
python -m venv .venv
```

Активируйте окружение:

- Linux/macOS: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

```bash
python -m pip install -r requirements.txt
python main.py
```

В Linux при ошибке загрузки платформенного плагина `xcb` установите
системные библиотеки Qt/X11 для вашего дистрибутива.

В среде без дисплея можно проверить запуск командой
`QT_QPA_PLATFORM=offscreen python main.py`; видимого окна при этом не будет.
