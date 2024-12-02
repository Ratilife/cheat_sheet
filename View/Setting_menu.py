import PySimpleGUI as sg
from View.CreateFolder import СreateFolder
from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel
from Model.WorkingWithFolders import WorkingWithFolders


class SettingMenu:

    def __clear_parameter(self,parameter):
        return sg.user_settings_set_entry(parameter, None)

    def __checking_parameter(self,parameter):
        return sg.user_settings_get_entry(parameter)
    def __make_window(self):
        sg.theme('LightBrown11')
        # Получаем ранее сохраненный путь к папке (если он существует)
        saved_folder_path = self.__checking_parameter('-saved_folder_path-')

        layout = [
                    [sg.Text('Введите путь к папке:', size=(24, 1), auto_size_text=False, justification='right'),
                        sg.InputText(default_text=saved_folder_path,key='-FOLDER-', enable_events=True),
                        sg.FolderBrowse(button_text='...', key='-SAVE-'),
                        sg.Button(button_text='X', key='-CLEAR-')],
                    [sg.Button('Создать шаргалку', key='-CREATE_CS-'),
                        sg.Button('Создать закладку', key='-CREATE-'),
                        sg.Button('Удалить все кнопки', key='-DEL-')]
                 ]
        window = sg.Window('Настройка шпаргалки', layout)
        return window
    def start_SettingMenu(self):
        folder_path = None  # Переменная для хранения пути к папке
        window = self.__make_window()
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == '-FOLDER-':
                folder_path = values['-FOLDER-']+'/cheat_sheet'
                # Обновляем значение поля ввода, чтобы пользователь видел полный путь
                window['-FOLDER-'].update(folder_path)
            if event == '-CREATE_CS-':
                #Сохраняем параметр
                sg.user_settings_set_entry('-saved_folder_path-', folder_path)
                wwf = WorkingWithFolders()
                wwf.check_and_create_folder(folder_path)
            if event == '-CLEAR-':
                # Очищаем параметр и поле ввода
                self.__clear_parameter('-saved_folder_path-')
                window['-FOLDER-'].update('')
            if event == '-CREATE-':
                cf = СreateFolder()
                cf.startCreateFolder(True)
            if event == '-DEL-':
                lbVM = launcher_bar_ViewModel()
                lbVM.delete_all_button()
        window.close()
