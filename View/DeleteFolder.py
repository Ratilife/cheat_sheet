import PySimpleGUI as sg
from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel

class DeleteFolder:
    def startDeleteFolder(self):
        sg.theme('LightBrown11')
        layout = [
                    [sg.Text('Введите имя кнопки:', size=(24, 1), ), sg.Input(key='-KEY_NAME-')],
                    [sg.Button('Удалить', key='-DEL-')]
                 ]
        window = sg.Window('Удалить кнопку', layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == '-DEL-':
                lbVM = launcher_bar_ViewModel()
                lbVM.delete_button(values['-KEY_NAME-'])
                break  # Закрыть окно после добавления
        window.close()


