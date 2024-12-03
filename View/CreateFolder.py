import PySimpleGUI as sg
from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel
from ViewModel.СreateFolderViewModel import СreateFolderViewModel
class СreateFolder:
    def startCreateFolder(self,determine,folder_path = None):
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
                    [sg.Text('Введите путь к файлу:', size=(24, 1), justification='right',
                             key='-FILE_LABEL-'),
                            sg.InputText(key='-FILE_PATH-'), sg.FileBrowse(button_text='...',
                                                                           key='-BROWSE-')],
                    [sg.Button('Добавить', key='-ADD-')]
                 ]
        # Указываем параметр finalize=True для полной инициализации окна
        '''
        Добавлен параметр finalize=True в sg.Window. Это позволяет PySimpleGUI полностью инициализировать
        интерфейс до выполнения любых операций с элементами окна.
        '''
        window = sg.Window('Создать', layout, finalize=True)
        # Скрываем элементы для пути, если determine == True
        if determine:
            window['-FILE_LABEL-'].update(visible=False)
            window['-FILE_PATH-'].update(visible=False)
            window['-BROWSE-'].update(visible=False)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == '-ADD-':
                cfVM = СreateFolderViewModel()
                if determine:
                    #исполнение в другом модуле
                    cfVM.create_bookmark(values['-BUTTON_NAME-'],folder_path)
                else:
                    # исполнение в другом модуле
                    cfVM.create_button(values['-BUTTON_NAME-'],values['-FILE_PATH-'])
                    break  # Закрыть окно после добавления
        window.close()


