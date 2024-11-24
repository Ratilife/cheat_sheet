

class launcher_bar_ViewModel:

    def add_button(self,launcher_buttons,key,value):
        # Преобразуем словарь в список пар ключ-значение
        items = list(launcher_buttons.items())
        # Определяем индекс для вставки: перед последним элементом
        insert_index = max(0, len(items) - 1)  # Если словарь пуст, индекс будет 0
        # Вставляем новую пару на предпоследнюю позицию
        items.insert(insert_index, (key, value))
        # Преобразуем список обратно в словарь
        return dict(items)

    def delete_button(self,launcher_buttons,key):
        removed_value = launcher_buttons.pop(key, None)
        return removed_value