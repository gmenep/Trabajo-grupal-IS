from src.modelo.UsuarioServicio import UsuarioServicio


class AdministracionController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = UsuarioServicio()

    def iniciar(self):
        self.recargar()

    def recargar(self):
        try:
            self.__view.mostrar_usuarios(self.__servicio.listar_usuarios(self.__sesion))
        except Exception as error:
            self.__view.mostrar_error(str(error))
