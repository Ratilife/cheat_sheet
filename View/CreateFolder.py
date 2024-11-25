import PySimpleGUI as sg
from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel
from ViewModel.СreateFolderViewModel import СreateFolderViewModel
class СreateFolder:
    def startCreateFolder(self,determine):
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
                    [sg.Text('Введите путь к файлу:', size=(24, 1), justification='right'),
                            sg.InputText(key='-FILE_PATH-'), sg.FileBrowse(button_text='...')],
                    [sg.Button('Добавить', key='-ADD-')]
                 ]
        window = sg.Window('Создать', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == '-ADD-':
                cfVM = СreateFolderViewModel()
                if determine:
                    #исполнение в другом модуле
                    cfVM.create_bookmark(values['-BUTTON_NAME-'],values['-FILE_PATH-'])
                else:
                    # исполнение в другом модуле
                    cfVM.create_button(values['-BUTTON_NAME-'],values['-FILE_PATH-'])
                    break  # Закрыть окно после добавления
        window.close()


