import ctypes
import PySimpleGUI as sg
class SheatSheelPanel:

    # Создание данных для дерева
    def __сreation_tree_data(self):
        tree_data = sg.TreeData()
        #Проверка Наличия папок для закладок
        return tree_data


    def __make_window(self):
        tree_data = self.__сreation_tree_data()
        # Создание макета окна с указанием растягиваемости
        layout = [
            [sg.Text('Шаблоны текста', size=(30, 1), expand_x=True)],
            [sg.Tree(data=tree_data,
                     headings=['Actions'],
                     auto_size_columns=True,
                     num_rows=20,
                     col0_width=30,
                     key='-TREE-',
                     show_expanded=True,
                     enable_events=True,
                     expand_x=True,
                     expand_y=True)]
        ]

        # Создание окна с возможностью изменения размера
        window = sg.Window('Панель задач', layout, resizable=True, finalize=True, element_justification='left',
                           no_titlebar=True, keep_on_top=True, grab_anywhere=True)

        # Получение размеров экрана
        screen_width, screen_height = sg.Window.get_screen_size()

        # Установка размеров и позиции окна
        window.set_size((screen_width // 4, screen_height))  # Окно будет занимать четверть ширины экрана и всю высоту
        window.move(screen_width - (screen_width // 4), 0)  # Перемещение окна вправо

        # Сделать окно всегда поверх всех окон
        HWND_TOPMOST = -1
        SWP_NOMOVE = 0x0002
        SWP_NOSIZE = 0x0001
        SWP_SHOWWINDOW = 0x0040

        ctypes.windll.user32.SetWindowPos(
            window.TKroot.winfo_id(), HWND_TOPMOST, 0, 0, 0, 0,
            SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW
        )

        return window

    def start_cheatSheet_panel(self):
        window = self.__make_window()
        # Обработка событий окна
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

        window.close()
