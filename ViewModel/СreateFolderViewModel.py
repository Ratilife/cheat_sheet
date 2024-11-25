from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel

class СreateFolderViewModel:

    def create_button(self,name_button,path_folder ):
        lbVM = launcher_bar_ViewModel()
        lbVM.add_button(name_button, path_folder)



    def create_bookmark(self,name_button,path_folder):
        pass