class SujetoAuditoria:
    def __init__(self):
        self.__observadores = []

    def agregar_observador(self, observador):
        self.__observadores.append(observador)

    def eliminar_observador(self, observador):
        if observador in self.__observadores:
            self.__observadores.remove(observador)

    def notificar(self, log_vo):
        for observador in self.__observadores:
            observador.actualizar(log_vo)
