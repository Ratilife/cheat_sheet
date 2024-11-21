import PySimpleGUI as sg

def startCreateFolder():
    bookmark = 'Введите название закладки'
    button_text = 'Введите название кнопки'
    sg.theme('LightBrown11')
    layout = [
              [sg.Text('Введите название кнопки:',size=(24, 1),), sg.Input(key='-BUTTON_NAME-')],
              [sg.Text('Куда сохранить файл картинок', size=(24, 1), auto_size_text=False, justification='right'),
                sg.InputText(), sg.FolderBrowse(button_text='...')],
                [sg.Button('Добавить', key='-ADD-')]
             ]
    window = sg.Window('Создать',layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == '-ADD-':
            pass
    window.close()
