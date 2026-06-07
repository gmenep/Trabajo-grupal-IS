from src.modelo.EstadisticaServicio import EstadisticaServicio


class EstadisticasController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = EstadisticaServicio()

    def cargar(self):
        datos = self.__servicio.obtener_estadisticas(self.__sesion)
        self.__view.mostrar_info(str(datos))
