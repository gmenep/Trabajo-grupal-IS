from src.modelo.dao.LogDaoJDBC import LogDaoJDBC
from src.modelo.dao.UsersDaoJDBC import UsersDaoJDBC
from src.modelo.ServicioBase import ServicioBase


class LogServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__log_dao = LogDaoJDBC()
        self.__users_dao = UsersDaoJDBC()

    def listar_logs(self, sesion, user_id, event_type, fecha):
        self._verificar_permiso(sesion, "logs", "CONSULTAR_LOGS")
        self._registrar_log(sesion.user_id, "CONSULTAR_LOGS", None, "Consulta de logs")
        return self.__log_dao.select_filtrado(user_id, event_type, fecha)

    def listar_tipos(self, sesion):
        self._verificar_permiso(sesion, "logs", "CONSULTAR_TIPOS_LOG")
        return self.__log_dao.select_event_types()

    def listar_usuarios(self, sesion):
        self._verificar_permiso(sesion, "logs", "CONSULTAR_USUARIOS_LOG")
        return self.__users_dao.select()
