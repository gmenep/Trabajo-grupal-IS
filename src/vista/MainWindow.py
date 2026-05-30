from src.vista.ui.UiMainWindow import UiMainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class LoginWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.__controller = None

    @property
    def controlador(self):
        return self.__controller

    @controlador.setter
    def controlador(self, controller):
        self.__controller = controller

    def setup(self, btn_list):
        '''
        Configura los botones que el usuario puede utilizar de la ventana principal y desactiva el resto.
        '''
        pass
