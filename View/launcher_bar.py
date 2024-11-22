import PySimpleGUI as sg
from View.CreateFolder import startCreateFolder


settings_image_path = r'F:/Языки/Python/Partfolio/cheat_sheet/Image/settings.png'

# Определяем пути к приложениям
launcher_buttons = {

                    sg.SYMBOL_DOWN_ARROWHEAD : None,
                    'Exit': None,
                    'Настройка': {
                                'action':'startCreateFolder',
                                 'imageSetting':settings_image_path
                                 }
                   }
# Функция для открытия окна настроек.
def setting(window: sg.Window):
    pass


# Функция создания главного окна лаунчера.
def __make_window():

    # Создаем макет с кнопками для запуска приложений
    #layout = [[sg.Button(app, size=(20, 2)) for app in launcher_buttons.keys()]]
    layout = [
        [
            sg.Button(
                app if app not in launcher_buttons or not isinstance(launcher_buttons[app], dict) else '',
                # Если это "Настройка", отображаем картинку
                image_filename=launcher_buttons[app]['imageSetting']
                if isinstance(launcher_buttons[app], dict) and 'imageSetting' in launcher_buttons[app] else None,
                size=(None, None),  # Убираем фиксированный размер
                tooltip=app,        # Подсказка при наведении
                key=app             # Назначаем ключ для события
            ) for app in launcher_buttons.keys()
        ]
        ]
    # Создаем окно с указанным макетом
    window = sg.Window("Simple Launcher", layout)
    # Основной цикл обработки событий
    while True:
        event, values = window.read()
        # Если пользователь закрыл окно или нажал кнопку выхода, выходим из цикла
        if event == sg.WINDOW_CLOSED:
            break
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED):
            break
        # Если нажата одна из кнопок, выполняем соответствующее действие
        if event in launcher_buttons:
            action = launcher_buttons[event]
            if isinstance(action, dict) and action.get('action') == 'startCreateFolder': startCreateFolder(False)
        # Если нажата одна из кнопок, запускаем соответствующее приложение
        #if event in applications: sg.execute_command_subprocess(launcher_buttons[event])
        # Закрываем окно
    window.close()

# с этого метода все начинается
def start_launcher():
    __make_window()
