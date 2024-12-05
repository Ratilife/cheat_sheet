import os

class WorkingWithFolders:
    def check_folder_exists(self,folder_path):
        """
        Проверяет, существует ли указанная папка.
        :param folder_path: Путь к папке
        :return: True, если папка существует, иначе False
        """
        return os.path.exists(folder_path)


    def create_folder(self,folder_path):
        """
        Создает указанную папку.
        :param folder_path: Путь к папке
        """
        os.makedirs(folder_path)
        print(f"Папка '{folder_path}' создана.")


    # Пример использования (функционал возможно перенести в другой модуль)
    def check_and_create_folder(self,folder_path):
        #full_path = os.path.join(folder_path, 'cheat_sheet')

        if not self.check_folder_exists(folder_path):
            self.create_folder(folder_path)
        else:
            print(f"Папка '{folder_path}' уже существует.")


    def check_and_create_bookmark(self,folder_path,nameBookmark):
        full_path = os.path.join(folder_path, nameBookmark)
        if not self.check_folder_exists(full_path):
            self.create_folder(full_path)
