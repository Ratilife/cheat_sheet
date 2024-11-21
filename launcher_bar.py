import PySimpleGUI as sg


# Определяем пути к приложениям
launcher_buttons = {
                    sg.SYMBOL_DOWN_ARROWHEAD : None,
                    'Exit': None
                   }
# Функция для открытия окна настроек.
def setting(window: sg.Window):
    pass


# Функция создания главного окна лаунчера.
def __make_window():
    pass

# с этого метода все начинается
def start_launcher():
    # Создаем макет с кнопками для запуска приложений
    layout = [[sg.Button(app, size=(20, 2)) for app in launcher_buttons.keys()]]
    # Создаем окно с указанным макетом
    window = sg.Window("Simple Launcher", layout)
    # Основной цикл обработки событий
    while True:
        event, values = window.read()
        # Если пользователь закрыл окно или нажал кнопку выхода, выходим из цикла
        if event == sg.WINDOW_CLOSED:
            break

        # Если нажата одна из кнопок, запускаем соответствующее приложение
        if event in applications: sg.execute_command_subprocess(launcher_buttons[event])
        # Закрываем окно
    window.close()
