import PySimpleGUI as sg
from View.CreateFolder import СreateFolder
from View.Setting_menu import SettingMenu
from View.DeleteFolder import DeleteFolder
from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel


sg.theme('LightBrown11')
#Этот код представляет собой изображение, закодированное в формате Base64
settings_icon    = b'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'
add_icon         = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABGlBMVEUAAABLr1BJr1BMr1BMsE9Nr1BUv0A4o1xMrlFOrlFNxDs/o1xKrVJMrVJKrlFLrlFMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BLsE9Mr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMrFNKr1BPrVJMr1BMr1BMr1BMr1BMr1BMr1BMr1BMr1BMsFBMr1BMr1BMr1BMr1BKrk5Lr09XtFqb0p2m16hLrk9huWXq9er///9Jrk1guGRiuWV0wXfs9+1ZtVzs9uz8/v3t9+2p2aul16e13re23rj4BlkrAAAAR3RSTlMAAAAAAAAAAAAAAAAAAAEBARtOdpWfoHdQAQItiNb5ijAReOPkeRIfrfyvIiC2uv17LuIvjdWBlgEBAYOMMX++sHrlARqXhMBzJJMAAAABYktHRFDjbky8AAAACXBIWXMAAhvvAAIb7wFJFxuDAAAAB3RJTUUH5AsCDR0Ggg9Q1AAAAWZJREFUOMuVk2lfgkAQxrGR7kNQisyjNMkrTVPLUjuNUIEVxczy+3+NhHVRRPzl84qd+bOzu/MMRa0nz+HRhlsOfAzrD3DHgROeOfU608GzUDgimoqEo+dBWMhfxOLinC4Tgo2Aq2RKtCmVzswRkL0WHcplLQKEpLhESVIF6FieBD8nIt/5G8AEFIrTkNRqdzrtljRdFm9NACBE/pEVFSFVkcm65DUIYMpuQJkxARa/jyTLXc0AtK4s4yoR1gT8GG/1FK2vI6T3NaU3wLHKBNiEAD5/+0tV9SFCQ11Vv0d4izvYorbvOQz8oDn94nNwOzTlqa4CHmhqd3WJvdWHfDRvwbtfk//fQ0HUDajt42bUiZmkwWg8Hg1Is+L1aTfphNVuiZQ32t3wEUMI6WWGSc9sCZmcM/9kM6XTtM8Zu62FF5vtXxvC4mAEC7XZ4JTqi4NjIG/vbKXJcc0PnvE509bwVg/WnPc/twitAU0YMzAAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjAtMTEtMDJUMTM6Mjk6MDYrMDA6MDDe1dIGAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIwLTExLTAyVDEzOjI5OjA2KzAwOjAwr4hqugAAACB0RVh0c29mdHdhcmUAaHR0cHM6Ly9pbWFnZW1hZ2ljay5vcme8zx2dAAAAGHRFWHRUaHVtYjo6RG9jdW1lbnQ6OlBhZ2VzADGn/7svAAAAGHRFWHRUaHVtYjo6SW1hZ2U6OkhlaWdodAA1MTKPjVOBAAAAF3RFWHRUaHVtYjo6SW1hZ2U6OldpZHRoADUxMhx8A9wAAAAZdEVYdFRodW1iOjpNaW1ldHlwZQBpbWFnZS9wbmc/slZOAAAAF3RFWHRUaHVtYjo6TVRpbWUAMTYwNDMyMzc0NpDho+QAAAATdEVYdFRodW1iOjpTaXplADEyMjIxQkKJ2jQ8AAAAQ3RFWHRUaHVtYjo6VVJJAGZpbGU6Ly8uL3VwbG9hZHMvNTYvWE5ySUZ0bS8yNjIxL2d1aV9hZGRfaWNvbl8xNTcyNTMucG5n14Vq2QAAAABJRU5ErkJggg=='
delete_icon      = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAVBQTFRFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////JIOtpgAAAG50Uk5TAAZkz/36xVEDd/HHfIHQ7GBDlxEart8rAhcfHhyb5Dwb8n0WBXbZ4/T45fzXazDpcnRzt+ovP/BMabyVmMPrBG/m6G6c3TEdOeeGmdh+AWJUWFJhCJqiCcSjur+gssBEODs6FZHgJu2laq3vSAfw2PoxAAAAAWJLR0RvVQhhgQAAAAlwSFlzAAAJjAAACYwBjmhrHAAAARhJREFUOMtjYEACjEzMLKxs7BwMOAAHJxc3Dy8fvwAuBYL8QsIMDCKiYuLoMhKSUtLS0jKycvIK0tIi7IpKQEpaSlkCJq+iqianDgQamiBSXUtbEUTJ6ejCHKOnL2pgCARGYNLQ0MAITBqbmEIVmJlbYHOSpaYZsQr09K2sbTCAta2dHlSBvYOjtpMWGnBi0XK2h5vm4urmLo0C3D08vZCs8/ZRRneBtJwvqQr8/NmBrIBAIBEULIFFQYhtKJAVZqzCwBBqG45FQXgEUIFfZBQjUEHEqAJaKgiJtgGyYmKBcWETF4ItNuMTgKzEJCCREO+HoSAZf3pISZVGV5DmqYrEs0jPyEQFulnZOUgKcnnM89BANk8uWAoAaO9yRh86jgcAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTktMDUtMDNUMDk6MjQ6NTkrMDE6MDBwhhvGAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE5LTA1LTAzVDA5OjI0OjU5KzAxOjAwAdujegAAAEZ0RVh0c29mdHdhcmUASW1hZ2VNYWdpY2sgNi43LjgtOSAyMDE5LTAyLTAxIFExNiBodHRwOi8vd3d3LmltYWdlbWFnaWNrLm9yZ0F74sgAAAAYdEVYdFRodW1iOjpEb2N1bWVudDo6UGFnZXMAMaf/uy8AAAAYdEVYdFRodW1iOjpJbWFnZTo6aGVpZ2h0ADUxMsDQUFEAAAAXdEVYdFRodW1iOjpJbWFnZTo6V2lkdGgANTEyHHwD3AAAABl0RVh0VGh1bWI6Ok1pbWV0eXBlAGltYWdlL3BuZz+yVk4AAAAXdEVYdFRodW1iOjpNVGltZQAxNTU2ODcxODk5UHATtQAAABN0RVh0VGh1bWI6OlNpemUANy4yN0tCQvCm3lIAAABEdEVYdFRodW1iOjpVUkkAZmlsZTovLy4vdXBsb2Fkcy81Ni9UbWVob2FKLzE5MTkvYmlnZ2FyYmFnZWJpbl8xMjE5ODAucG5n7bnnUwAAAABJRU5ErkJggg=='
cheat_sheet_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAADsAAAA7AF5KHG9AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA5FJREFUWIXtlk1sG1UQx3/Pu9g4TtLGxFUb0Zoio6pwgAOQpuKEpR6K2gCSeyAHql6scmyRaIAqwWpRD1S5tVgIISS4YATqAQQNUAmQKLeC+AqxROygILbEIa7rj816h4M/Ujdrx7YSJCT+l/WbnZn//82+eWNFt3j+whPKVnEAcUmU1577qJs0qivyyffcKrs4R7m8AwQ0fUH679rN5BFz0wSoExeLgKfBWLYqT01f9TNLcGMZ++2JtnLrTkZ5fWRcRE4D3ppNm3Vw1BzCFYBgX9wnt1gLComp49+ea0/AbeR1lMuVHbaCy9HqFdRpoD0BNfLFZz9HtDsqlvE3AWnivhY/jX1R/33/u48D9Dj5NRMAsEoOPHbvED/8sQj4WhKXbmTx9PW1LVQBLBw61KMVi6cQGQPu1ny227PbIn/2E5TeUmNTGKXKAbXFIvPVM3wf2ELG6zaB34F3+nO5cyf2JwpqfmTE6/b5rgDDa7I8+BDEYl2JMEoWtlh8bVzAKMw4uXzTn8uFdY/P96LAsNq1C3G7IZmEUAhlmsh311AffgCRI44kM38ucfmX9Br7gb1BBrb08uvyZ47kSrkQsUeyvr4XXAJjAOJ2oyYm4fAoamKyIgaQ6el64JlUhlfmFjmbytQytazCXO4qAAOeIWpXzn39j/DUzpPVeBnTgSEAkkkkkUBFo0g8XqkEgGHUE5al0gVW9Yk0dsWBvUH2bNtaCStZ5MtLAOwPPM2yaWAU5xgefJJL81O1kJ0uoFLDUAgViSDxOCoSgVCo4hII1Am06o712s7XqUCPNgDApwtv4PcM8ejgKJfmp8iuXK+5/KaMcHhclHrV8Qyk06jDoxCNtiRyglGyuJZ5n2T2St1W/fara+SUft3vPz+4tBSWdDpcf5NM1q8cyd/scmKBZRca1reSA9Oi3ZzSH0gkzB8jkYOBTOakKHUUCGq9tsez3SJ/z0EoFpsSrNcFlpgEe/exffZjZgd6ydzpLoFKAW/tMPXz0YcTK46bqw2Sv4592WA/k8pQFkFXipeCfmaMv7n8c6qpgBqqVzGu41fX8HV0w3TaBe3AeXY1Qadd0A46qsDLQX/Des+2rfUdd4uOKrAZ6G7UVbFeF2y4gNu74F8/A/93wX+mC+wO/rxuioBCuX0BLT/BirSfCMAWMG174wQsmeWOBHSDZgIKgLc2xTYIeSej4xlQSKxZQLfkSog5vfgHnhJ17oGtgnsAAAAASUVORK5CYII='
# Минимизированное изображение (в виде эмодзи).
MINIMIZED_IMAGE  = b'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'

# Определяем пути к приложениям
launcher_buttons = {
    sg.SYMBOL_DOWN_ARROWHEAD: None,
    "cheat_sheet_icon": 'startCheatSheet',
    "add_icon": 'startCreateFolder',
    "delete_icon": 'startDeleteFolder',
    "settings_icon": 'start_SettingMenu',
    'Exit': None
}

deleteLauncherButton = False

def __checking_parameter(parameter):
    return sg.user_settings_get_entry(parameter)

def __delete_parameter(parameter):
    # Удаляем параметр parameter из настроек пользователя
    sg.user_settings_delete_entry(parameter)
    deleteLauncherButton = False
    #TODO - разработать функционал оновления формы

# Функция создания главного окна лаунчера.
def __make_window():
    global launcher_buttons  # Указываем, что это глобальная переменная


    if deleteLauncherButton:
        __delete_parameter('launcher_buttons')
    # Проверяем, есть ли сохранённые данные в параметре launcher_buttons
    #checking_launcher_buttons(launcher_buttons)
    # Проверяем, есть ли сохранённые данные
    saved_launcher_buttons = __checking_parameter('launcher_buttons')

    if saved_launcher_buttons is not None:
        # Если данные существуют, загружаем их
        launcher_buttons = saved_launcher_buttons
    # Формируем кнопки из словаря.
    button_row = []
    for item in launcher_buttons.keys():
        # Создаём кнопку с изображением, если ключ — это байтовые данные.
        tip ='Я не знаю что сдесь писать'
        '''
        старый код
        if isinstance(item, bytes):

            button = sg.Button(image_data=item, key=item, metadata=launcher_buttons[item],
                               border_width=0)

        else:
            button = sg.Button(item, key=item, metadata=launcher_buttons[item],
                               border_width=0)  # Кнопка с текстом.
        button_row.append(button)
        '''
        if item == "add_icon":
            button = sg.Button(image_data=add_icon, key=item, metadata=launcher_buttons[item],
                               border_width=0)
        elif item == "settings_icon":
            button = sg.Button(image_data=settings_icon, key=item, metadata=launcher_buttons[item],
                               border_width=0)
        elif item == "delete_icon":
            button = sg.Button(image_data=delete_icon, key=item, metadata=launcher_buttons[item],
                               border_width=0)
        elif item == "cheat_sheet_icon":
            button = sg.Button(image_data=cheat_sheet_icon, key=item, metadata=launcher_buttons[item],
                               border_width=0)
        else:
            # Кнопка с текстом.
            button = sg.Button(item, key=item, metadata=launcher_buttons[item],
                               border_width=0)
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
    location = screen_size[0] // 2, screen_size[1] - 200        # установите местоположение по умолчанию по центру и ближе к нижней части экрана

    location = sg.user_settings_get_entry('-window location-', location)  # Загружаем сохранённое местоположение.
    keep_on_top = sg.user_settings_get_entry('-keep on top-', True)  # Загружаем настройку "поверх всех окон".


    # Создаём главное окно.
    '''
    Создание окна с помощью PySimpleGUI с рядом параметров и настроек:

    - sg.Window('Window Title', layout, location=location, ...) - Создаёт окно с заголовком 'Window Title' и макетом layout.

    Параметры:

    1. **location=location**:
       - Указывает начальную позицию окна на экране, где `location` — это кортеж с координатами `(x, y)`. Например, `(0, 0)` поставит окно в левый верхний угол экрана.

    2. **keep_on_top=keep_on_top**:
       - Если установлено в `True`, окно будет всегда поверх других окон. Параметр `keep_on_top` может быть задан как `True` или `False`.

    3. **no_titlebar=True**:
       - Убирает заголовок окна, так что окно не будет иметь стандартную верхнюю панель с кнопками управления (свернуть, развернуть, закрыть).

    4. **grab_anywhere=True**:
       - Позволяет перемещать окно по экрану, просто щелкая по любому месту окна, а не только по его заголовку. Это полезно, если вы отключили заголовок окна с помощью `no_titlebar=True`.

    5. **background_color=screen_background_color**:
       - Устанавливает цвет фона окна. Параметр `screen_background_color` может быть строкой с названием цвета или кодом цвета (например, 'blue' или '#FFFFFF').

    6. **auto_size_buttons=False**:
       - Если установлено в `False`, кнопки в окне не будут автоматически изменять размер в зависимости от текста. Если установить в `True`, кнопки будут изменять размер в соответствии с их содержимым.

    7. **default_button_element_size=DEFAULT_BUTTON_SIZE**:
       - Устанавливает размер по умолчанию для кнопок. Параметр `DEFAULT_BUTTON_SIZE` может быть кортежем, например, `(10, 2)`, что указывает на ширину 10 и высоту 2 для кнопок.

    8. **right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT**:
       - Устанавливает меню правой кнопки мыши для окна. В данном случае используется предустановленное меню с опциями "Edit", "Settings" и "Exit".

    9. **enable_close_attempted_event=True**:
       - Включает событие, которое срабатывает при попытке закрыть окно (например, если пользователь нажал кнопку закрытия окна). Это полезно, если необходимо выполнить какие-либо действия или проверки перед закрытием окна.

    10. **use_default_focus=False**:
        - Отключает использование стандартного фокуса на первом элементе окна. По умолчанию PySimpleGUI фокусирует первый элемент окна, но с этим параметром можно избежать этого.

    В сумме, этот код создаёт окно с заданными параметрами, включая индивидуальные настройки для внешнего вида, расположения, а также поведения окна.
    '''

    window = sg.Window("Панель", layout,location=location,keep_on_top=keep_on_top,no_titlebar=True,grab_anywhere=True,finalize=True)

    return window

def start_launcher_bar():
    global launcher_buttons  # Указываем, что это глобальная переменная

    window = __make_window()  # Создаём главное окно.
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED):  # Если нажали выход.
            if event != sg.WIN_CLOSED:
                sg.user_settings_set_entry('launcher_buttons', launcher_buttons)
                if sg.user_settings_get_entry('-auto save location-', True):  # Сохраняем позицию окна при выходе.
                    sg.user_settings_set_entry('-window location-', window.current_location())

            break
        if event in launcher_buttons:
             action = launcher_buttons[event]
             if isinstance(action, str):
                if action == 'start_SettingMenu':               # Если действие связано с меню настроек
                    sm = SettingMenu()
                    sm.start_SettingMenu()                      # Вызов метода для открытия меню настроек
                    window.close()
                elif action == 'startCreateFolder':             # Если действие связано с созданием папки
                    # Вызов метода для создания кнопки и Обновляем словарь
                    cf = СreateFolder()
                    # Проверяем, есть ли сохранённые данные
                    saved_launcher_buttons = __checking_parameter('launcher_buttons')

                    if saved_launcher_buttons is not None:
                        # Если данные существуют, загружаем их
                        launcher_buttons = saved_launcher_buttons

                    cf.startCreateFolder(False)

                    window.close()
                    lbVM = launcher_bar_ViewModel()
                    lbVM.refresh_launcher()
                    #sg.user_settings_set_entry('launcher_buttons', launcher_buttons)

                    # Создаём новую кнопку
                    #new_button = sg.Button(button_name, key=button_name, metadata=file_path)
                    # Обновляем макет окна
                    #window.extend_layout(window['-BUTTON COL-'], [[new_button]])

                elif action.endswith(('.py', '.pyw')):  # Если файл Python.
                    sg.execute_py_file(action)
                elif action == 'startDeleteFolder':
                    df = DeleteFolder()
                    df.startDeleteFolder()
                    window.close()
                    lbVM = launcher_bar_ViewModel()
                    lbVM.refresh_launcher()

                # Проверяем, если action - это функция
                else:
                    sg.execute_command_subprocess(action)   # Запускаем приложение.
             elif callable(action):
                action()                                    # Выполнить функцию
        if event == sg.SYMBOL_DOWN_ARROWHEAD:               # Минимизировать окно.
            window['-BUTTON COL-'].update(visible=False)
            window['-MINIMIZED COL-'].update(visible=True)
        elif event == '-MINIMIZED IMAGE-':  # Развернуть окно.
            window['-BUTTON COL-'].update(visible=True)
            window['-MINIMIZED COL-'].update(visible=False)
    window.close()
