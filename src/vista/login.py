from src.vista.ui.UiLoginWindow import UiLoginWindow
from PyQt5.QtWidgets import QMainWindow, QApplication

class VentanaPrincipal(QMainWindow, UiLoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        
        self.btn_login.clicked.connect(self.guardar_datos)

    def guardar_datos(self):
        u = self.input_user.text()
        p = self.input_pass.text()
        print(f"Usuario: {u}\nContraseña: {p}")