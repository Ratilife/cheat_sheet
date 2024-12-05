import PySimpleGUI as sg
from View.CreateFolder import СreateFolder
from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel
from Model.WorkingWithFolders import WorkingWithFolders
from Model.Constants import Constants
#TODO - при загрузке проверять константу TOP_WINDOW
class SettingMenu:
    # очистить константу
    def __clear_parameter(self,parameter):
        return Constants.delete_value(parameter)

    def __checking_parameter(self,parameter):
        return sg.user_settings_get_entry(parameter)
    def __make_window(self):
        sg.theme('LightBrown11')
        # Получаем ранее сохраненный путь к папке (если он существует)
        saved_folder_path = Constants.DATA_PATH
        saved_topWindow = Constants.TOP_WINDOW
        layout = [
                    [sg.Text('Введите путь к папке:', size=(24, 1), auto_size_text=False, justification='right'),
                        sg.InputText(default_text=saved_folder_path,key='-FOLDER-', enable_events=True),
                        sg.FolderBrowse(button_text='...', key='-SAVE-'),
                        sg.Button(button_text='X', key='-CLEAR-')],
                    [sg.Checkbox('Разместить поверх окон', key = '-TOP_WINDOW-')],
                    [sg.Button('Создать шаргалку', key='-CREATE_CS-'),
                        sg.Button('Создать закладку', key='-CREATE-'),
                        sg.Button('Удалить все кнопки', key='-DEL-')]
                 ]
        window = sg.Window('Настройка шпаргалки', layout)
        if saved_topWindow:
            # Установка значения чекбокса сразу после создания окна
            window['-TOP_WINDOW-'].update(value=True)
        else:
            window['-TOP_WINDOW-'].update(value=False)
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
            #Создать шпаргалку
            if event == '-CREATE_CS-':
                #Сохраняем константу

                Constants.set_value('DATA_PATH',folder_path)
                wwf = WorkingWithFolders()
                wwf.check_and_create_folder(folder_path)
            #Очистить путь
            if event == '-CLEAR-':
                # Очищаем константу и поле ввода
                self.__clear_parameter('DATA_PATH')
                window['-FOLDER-'].update('')
            # Создать закладку
            if event == '-CREATE-':

                saved_folder_path = Constants.DATA_PATH
                if saved_folder_path is not None:
                    folder_path = saved_folder_path
                else:
                    # установить константу
                    folder_path = values['-FOLDER-']
                    Constants.set_value('DATA_PATH',folder_path)
                cf = СreateFolder()

                cf.startCreateFolder(True)
            #Удалить все кнопки
            if event == '-DEL-':
                lbVM = launcher_bar_ViewModel()
                lbVM.delete_all_button()
            #поверх окон
            if event == '-TOP_WINDOW-':
                Constants.set_value('TOP_WINDOW', values['-TOP_WINDOW-'])

        window.close()
