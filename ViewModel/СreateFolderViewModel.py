from ViewModel.launcher_bar_ViewModel import launcher_bar_ViewModel

class СreateFolderViewModel:

    def create_button(self, launcher_buttons,name_button,path_folder ):
        lbVM = launcher_bar_ViewModel()
        lb = lbVM.add_button(launcher_buttons, name_button, path_folder)
        return lb


    def create_bookmark(self,name_button,path_folder):
        pass