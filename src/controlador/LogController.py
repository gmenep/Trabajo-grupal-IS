from src.modelo.LogServicio import LogServicio


class LogController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = LogServicio()

    def cargar(self):
        logs = self.__servicio.listar_logs(self.__sesion, None, None, None)
        filas = []
        for log in logs:
            filas.append({
                "log_id": log.log_id,
                "timestamp": log.timestamp,
                "event_type": log.event_type,
                "reference_id": log.reference_id,
                "raw_data": log.raw_data,
                "user_id": log.user_id
            })
        self.__view.mostrar_logs(filas)
