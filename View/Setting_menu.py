import PySimpleGUI as sg
from View.CreateFolder import СreateFolder
from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel


class SettingMenu:

    def start_SettingMenu(self):

        sg.theme('LightBrown11')
        # Получаем ранее сохраненный путь к папке (если он существует)
        saved_folder_path = sg.user_settings_get_entry('-saved_folder_path-', '')
        layout = [
        [sg.Text('Введите путь к папке:', size=(24, 1), auto_size_text=False, justification='right'),
         sg.InputText(key='-FOLDER-', enable_events=True), sg.FolderBrowse(button_text='...', key='-SAVE-')],
        [sg.Button('Создать закладку', key='-CREATE-'),sg.Button('Удалить все кнопки', key='-DEL-')]
        ]
        window = sg.Window('Настройка шпаргалки', layout)
        folder_path = None  # Переменная для хранения пути к папке
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == '-FOLDER-':
                folder_path = values['-FOLDER-']+'/cheat_sheet'
                sg.user_settings_set_entry('-saved_folder_path-', folder_path)
            if event == '-CREATE-':
                cf = СreateFolder()
                cf.startCreateFolder(True)
            if event == '-DEL-':
                lbVM = launcher_bar_ViewModel()
                lbVM.delete_all_button()
        window.close()
