from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.vista.ui.UiLoginWindow import UiLoginWindow


class LoginWindow(QMainWindow, UiLoginWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("LabTrack - Login")
        self.setWindowIcon(QIcon(str(Path(__file__).resolve().parent / "images" / "icono.png")))

    def obtener_usuario(self):
        return self.input_user.text()

    def obtener_password(self):
        return self.input_pass.text()

    def warning_message(self, message):
        self.mostrar_error(message)

    def mostrar_error(self, message):
        QMessageBox.warning(self, "LabTrack", message)

    def mostrar_info(self, message):
        QMessageBox.information(self, "LabTrack", message)
