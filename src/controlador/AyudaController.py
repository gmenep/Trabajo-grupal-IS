from src.modelo.AyudaServicio import AyudaServicio


class AyudaController:
    def __init__(self, view):
        self.__view = view
        self.__servicio = AyudaServicio()

    def cargar(self):
        self.__view.mostrar_ayuda(self.__servicio.secciones())
