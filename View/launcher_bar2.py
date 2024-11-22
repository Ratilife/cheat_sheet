import PySimpleGUI as sg
from View.CreateFolder import startCreateFolder
from View.Setting_menu import start_SettingMenu
#Этот код представляет собой изображение, закодированное в формате Base64
settings_icon = b'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'
add_icon =     b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABGlBMVEUAAABLr1BJr1BMr1BMsE9Nr1BUv0A4o1xMrlFOrlFNxDs/o1xKrVJMrVJKrlFLrlFMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BLsE9Mr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMrFNKr1BPrVJMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMsFBMr1BMr1BMr1BMr1BKrk5Lr09XtFqb0p2m16hLrk9huWXq9er///9Jrk1guGRiuWV0wXfs9+1ZtVzs9uz8/v3t9+2p2aul16e13re23rj4BlkrAAAAR3RSTlMAAAAAAAAAAAAAAAAAAAEBARtOdpWfoHdQAQItiNb5ijAReOPkeRIfrfyvIiC2uv17LuIvjdWBlgEBAYOMMX++sHrlARqXhMBzJJMAAAABYktHRFDjbky8AAAACXBIWXMAAhvvAAIb7wFJFxuDAAAAB3RJTUUH5AsCDR0Ggg9Q1AAAAWZJREFUOMuVk2lfgkAQxrGR7kNQisyjNMkrTVPLUjuNUIEVxczy+3+NhHVRRPzl84qd+bOzu/MMRa0nz+HRhlsOfAzrD3DHgROeOfU608GzUDgimoqEo+dBWMhfxOLinC4Tgo2Aq2RKtCmVzswRkL0WHcplLQKEpLhESVIF6FieBD8nIt/5G8AEFIrTkNRqdzrtljRdFm9NACBE/pEVFSFVkcm65DUIYMpuQJkxARa/jyTLXc0AtK4s4yoR1gT8GG/1FK2vI6T3NaU3wLHKBNiEAD5/+0tV9SFCQ11Vv0d4izvYorbvOQz8oDn94nNwOzTlqa4CHmhqd3WJvdWHfDRvwbtfk//fQ0HUDajt42bUiZmkwWg8Hg1Is+L1aTfphNVuiZQ32t3wEUMI6WWGSc9sCZmcM/9kM6XTtM8Zu62FF5vtXxvC4mAEC7XZ4JTqi4NjIG/vbKXJcc0PnvE509bwVg/WnPc/twitAU0YMzAAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjAtMTEtMDJUMTM6Mjk6MDYrMDA6MDDe1dIGAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIwLTExLTAyVDEzOjI5OjA2KzAwOjAwr4hqugAAACB0RVh0c29mdHdhcmUAaHR0cHM6Ly9pbWFnZW1hZ2ljay5vcme8zx2dAAAAGHRFWHRUaHVtYjo6RG9jdW1lbnQ6OlBhZ2VzADGn/7svAAAAGHRFWHRUaHVtYjo6SW1hZ2U6OkhlaWdodAA1MTKPjVOBAAAAF3RFWHRUaHVtYjo6SW1hZ2U6OldpZHRoADUxMhx8A9wAAAAZdEVYdFRodW1iOjpNaW1ldHlwZQBpbWFnZS9wbmc/slZOAAAAF3RFWHRUaHVtYjo6TVRpbWUAMTYwNDMyMzc0NpDho+QAAAATdEVYdFRodW1iOjpTaXplADEyMjIxQkKJ2jQ8AAAAQ3RFWHRUaHVtYjo6VVJJAGZpbGU6Ly8uL3VwbG9hZHMvNTYvWE5ySUZ0bS8yNjIxL2d1aV9hZGRfaWNvbl8xNTcyNTMucG5n14Vq2QAAAABJRU5ErkJggg=='
MINIMIZED_IMAGE = sg.EMOJI_BASE64_HAPPY_THUMBS_UP # Минимизированное изображение (в виде эмодзи).

# Определяем пути к приложениям
launcher_buttons = {

                    sg.SYMBOL_DOWN_ARROWHEAD : None,
                    add_icon:'startCreateFolder',
                    settings_icon: 'start_SettingMenu',
                    'Exit': None
                   }
# Функция создания главного окна лаунчера.
def __make_window():


    # Формируем кнопки из словаря.
    button_row = []
    for item in launcher_buttons.keys():
        # Создаём кнопку с изображением, если ключ — это байтовые данные.
        tip ='Я не знаю что сдесь писать'
        if isinstance(item, bytes):

            button = sg.Button(image_data=item, key=item, metadata=launcher_buttons[item],
                               border_width=0)

        else:
            button = sg.Button(item, key=item, metadata=launcher_buttons[item],
                               border_width=0)  # Кнопка с текстом.
        button_row.append(button)
    # Создаём колонки для кнопок и для минимизированного состояния.
    col_buttons = sg.Column([button_row], p=0, k='-BUTTON COL-')  # Основная колонка с кнопками.
    # Колонка для минимизированного вида.
    col_minimized = sg.Column([[sg.Button(image_data=MINIMIZED_IMAGE, k='-MINIMIZED IMAGE-',
                                              button_color=sg.theme_background_color(), border_width=0)]],
                                  visible=False, k='-MINIMIZED COL-')
    # Основной макет окна.
    layout = [[sg.pin(col_minimized), sg.pin(col_buttons)]]

    # Определяем местоположение окна: по центру, ближе к нижней части экрана.
    screen_size = sg.Window.get_screen_size()
    location = screen_size[0] // 2, screen_size[1] - 200  # установите местоположение по умолчанию по центру и ближе к нижней части экрана
    location = sg.user_settings_get_entry('-window location-', location)  # Загружаем сохранённое местоположение.
    keep_on_top = sg.user_settings_get_entry('-keep on top-', True)  # Загружаем настройку "поверх всех окон".


    # Создаём главное окно.
    window = sg.Window("Панель", layout,location=location,keep_on_top=keep_on_top)
    return window

def start_launcher_bar():
    window = __make_window()  # Создаём главное окно.
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED):  # Если нажали выход.
            if event != sg.WIN_CLOSED:
                if sg.user_settings_get_entry('-auto save location-', True):  # Сохраняем позицию окна при выходе.
                    print('saving locatoin', window.current_location())
                    sg.user_settings_set_entry('-window location-', window.current_location())
            break
        if event in launcher_buttons:
             action = launcher_buttons[event]
             if isinstance(action, str):
                if action == 'start_SettingMenu':               # Если действие связано с меню настроек
                    start_SettingMenu()                         # Вызов метода для открытия меню настроек
                elif action == 'startCreateFolder':               # Если действие связано с созданием папки
                    startCreateFolder(False)                    # Вызов метода для создания папки
        # Проверяем, если action - это функция
        elif callable(action):
                    action()                                    # Выполнить функцию

    window.close()