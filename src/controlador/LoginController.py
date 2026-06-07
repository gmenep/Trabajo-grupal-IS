from src.modelo.LoginServicio import LoginServicio


class LoginController:
    def __init__(self, view, abrir_main_callback):
        self.__view = view
        self.__abrir_main_callback = abrir_main_callback
        self.__login_servicio = LoginServicio()
        self.__conectar_eventos()

    def show_login(self):
        self.__view.show()

    def login_desde_vista(self):
        self.login(self.__view.obtener_usuario(), self.__view.obtener_password())

    def login(self, username, password):
        try:
            sesion = self.__login_servicio.login(username, password)
            self.__view.hide()
            self.__abrir_main_callback(sesion)
        except Exception as error:
            self.__view.warning_message(str(error))

    def __conectar_eventos(self):
        self.__view.btn_login.clicked.connect(self.login_desde_vista)
        self.__view.input_pass.returnPressed.connect(self.login_desde_vista)
