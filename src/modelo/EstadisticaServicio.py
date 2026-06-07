from src.modelo.dao.LogDaoJDBC import LogDaoJDBC
from src.modelo.dao.MachineDaoJDBC import MachineDaoJDBC
from src.modelo.dao.MaterialDaoJDBC import MaterialDaoJDBC
from src.modelo.dao.MaterialMovementDaoJDBC import MaterialMovementDaoJDBC
from src.modelo.ServicioBase import ServicioBase


class EstadisticaServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__material_dao = MaterialDaoJDBC()
        self.__machine_dao = MachineDaoJDBC()
        self.__log_dao = LogDaoJDBC()
        self.__movement_dao = MaterialMovementDaoJDBC()

    def obtener_estadisticas(self, sesion):
        self._verificar_permiso(sesion, "estadisticas", "CONSULTAR_ESTADISTICAS")
        datos = {
            "total_materiales": self.__material_dao.count(),
            "total_maquinas": self.__machine_dao.count(),
            "materiales_por_almacen": self.__material_dao.select_por_almacen(),
            "maquinas_por_estado": self.__machine_dao.select_by_state_count(),
            "stock_bajo": self.__material_dao.select_stock_bajo(),
            "proximos_caducar": self.__material_dao.select_proximos_caducar(),
            "revisiones_proximas": self.__machine_dao.select_revisiones_proximas(),
            "logs_por_tipo": self.__log_dao.logs_by_type(),
            "uso_materiales": self.__movement_dao.select_usage()
        }
        self._registrar_log(sesion.user_id, "CONSULTAR_ESTADISTICAS", None, "Consulta estadisticas")
        return datos
