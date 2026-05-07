from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/Ui/VistaLogin.ui")

class MiVentana(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        self.controlador = None
        # Conectar el botón a la función
        self.BotonAceptar.clicked.connect(self.on_button_click)


    def on_button_click(self):
        print("Botón presionado")
        texto_nombre = self.UsuarioEdit.text() #Obtenet el texto del campo nombre
        texto_contrasena = self.ContrasenaEdit.text()
        self.controlador.comprobarLogin(texto_nombre, texto_contrasena)

    def lanzaraviso(self):
        QMessageBox.information(self, "Info", "Login incorrecto")
        
    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, ref_controlador):
        self._controlador = ref_controlador