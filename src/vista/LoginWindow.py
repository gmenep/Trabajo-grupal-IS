from src.vista.ui.UiLoginWindow import UiLoginWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class LoginWindow(QMainWindow, UiLoginWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.__controller = None

        
        self.btn_login.clicked.connect(self.login)

    @property
    def controlador(self):
        return self.__controller

    @controlador.setter
    def controlador(self, controller):
        self.__controller = controller

    def login(self):
        self.__controller.login(self.input_user.text(), self.input_pass.text())

    def warning_message(self, message):
        QMessageBox.warning(self, "Warning", message)
