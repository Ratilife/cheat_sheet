

class Constants:
    DATA_PATH = None
    @staticmethod
    def set_value( key, value):
        """
        Устанавливает значение для указанного атрибута класса.
        :param key: Имя атрибута
        :param value: Значение, которое нужно установить
        """
        if hasattr(Constants, key):
            setattr(Constants, key, value)
        else:
            print(f"Атрибут '{key}' не существует.")

    @staticmethod
    def delete_value( key):
        """
        Удаляет значение для указанного атрибута класса (устанавливает None).
        :param key: Имя атрибута
        """
        if hasattr(Constants, key):
            setattr(Constants, key, None)
        else:
            print(f"Атрибут '{key}' не существует.")

    @staticmethod
    def get_value(key):
        """
        Возвращает значение указанного атрибута класса.
        :param key: Имя атрибута
        :return: Значение атрибута, если он существует, иначе None
        """
        if hasattr(Constants, key):
            return getattr(Constants, key)
        else:
            print(f"Атрибут '{key}' не существует.")
            return None
