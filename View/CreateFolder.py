import PySimpleGUI as sg


class СreateFolder:
    launcher_buttons = None
    def __сreateFolder(self,determine):
        # determine - определяет текст на форме True - закладки, False - кнопки
        bookmark = 'Введите название закладки'
        button_text = 'Введите название кнопки'

        text_field = None

        if determine:
            text_field = bookmark
        else:
            text_field = button_text

        sg.theme('LightBrown11')
        layout = [
                    [sg.Text(text_field, size=(24, 1), ), sg.Input(key='-BUTTON_NAME-')],
                    [sg.Text('Введите путь к папке:', size=(24, 1), auto_size_text=False, justification='right'),
                            sg.InputText(), sg.FolderBrowse(button_text='...')],
                    [sg.Button('Добавить', key='-ADD-')]
                 ]
        window = sg.Window('Создать', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == '-ADD-':
                pass
        window.close()


    def startCreateFolder(self,determine):
        __сreateFolder(determine)


    def startCreateFolder(self,determine, launcher_buttons):

        __сreateFolder(determine)
