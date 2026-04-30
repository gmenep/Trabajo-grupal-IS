import sys
from PyQt5.QtWidgets import QApplication


from src.vista.LoginWindow import LoginWindow
from src.controlador.ControllerLogin import ControllerLogin


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = LoginWindow() 
    controller_login = ControllerLogin(ventana, None)

    ventana.controlador = controller_login
    
    controller_login.show_login ()
    
    sys.exit(app.exec_())