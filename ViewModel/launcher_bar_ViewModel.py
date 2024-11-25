import View.launcher_bar

class launcher_bar_ViewModel:

    def __refresh_launcher(self):
        """
        Перезапускает окно лаунчера, применяя изменения в конфигурации.
        """
        View.launcher_bar.start_launcher_bar()  # Перезапуск основного окна лаунчера

    def refresh_launcher(self):
        self.__refresh_launcher()
    def add_button(self,key,value):
        # Преобразуем словарь в список пар ключ-значение
        items = list(View.launcher_bar.launcher_buttons.items())
        # Определяем индекс для вставки: перед последним элементом
        insert_index = max(0, len(items) - 1)  # Если словарь пуст, индекс будет 0
        # Вставляем новую пару на предпоследнюю позицию
        items.insert(insert_index, (key, value))
        # Преобразуем список обратно в словарь
        View.launcher_bar.launcher_buttons = dict(items)


    def delete_button(self,key):
        View.launcher_bar.launcher_buttons = launcher_buttons.pop(key, None)
        self.__refresh_launcher()

    def delete_all_button(self):
        View.launcher_bar.deleteLauncherButton = True
        self.__refresh_launcher()
