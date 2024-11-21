import PySimpleGUI as sg

def start_SettingMenu():
    sg.theme('LightBrown11')
    layout = [
                [sg.Text('Введите путь к папке:', size=(24, 1), auto_size_text=False, justification='right'),
                sg.InputText(key='-FOLDER-',enable_events=True), sg.FolderBrowse(button_text='...',key='-SAVE-')],
                [sg.Button('Создать закладку', key='-CREATE-')]
             ]
    window = sg.Window('Настройка шпаргалки', layout)
    folder_path = None  # Переменная для хранения пути к папке
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == '-SAVE-':
            folder_path = values['-FOLDER-']

    window.close()