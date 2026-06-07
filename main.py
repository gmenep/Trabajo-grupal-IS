import sys
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from PyQt5.QtWidgets import QApplication

from src.controlador.LoginController import LoginController
from src.controlador.MainController import MainController
from src.modelo.conexion.Conexion import Conexion
from src.vista.LoginWindow import LoginWindow
from src.vista.MainWindow import MainWindow


class LabTrackApp:
    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__login_view = None
        self.__main_window = None
        self.__controladores = []

    def ejecutar(self):
        self.mostrar_login()
        resultado = self.__app.exec_()
        Conexion().closeConnection()
        sys.exit(resultado)

    def mostrar_login(self):
        self.__login_view = LoginWindow()
        controller = LoginController(self.__login_view, self.abrir_main)
        self.__controladores = [controller]
        controller.show_login()

    def abrir_main(self, sesion):
        self.__main_window = MainWindow()
        self.__main_window.configurar_sesion(sesion)
        controller = MainController(self.__main_window, sesion, self.mostrar_login)
        self.__controladores = [controller]
        self.__main_window.resize(1200, 700)
        self.__main_window.show()


if __name__ == "__main__":
    os.environ["JAVA_HOME"] = r"c:\Users\lmomf\anaconda3\envs\labtrack"
    LabTrackApp().ejecutar()
