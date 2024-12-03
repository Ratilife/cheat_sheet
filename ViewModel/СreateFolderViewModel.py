from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel
from Model.WorkingWithFolders import WorkingWithFolders
class СreateFolderViewModel:

    def create_button(self,name_button,path_folder ):
        lbVM = launcher_bar_ViewModel()
        lbVM.add_button(name_button, path_folder)



    def create_bookmark(self,name_bookmark,path_folder):
        # создать папку
        wwf = WorkingWithFolders()
        wwf.check_and_create_bookmark(path_folder,name_bookmark)
        # создать закладку
        pass
