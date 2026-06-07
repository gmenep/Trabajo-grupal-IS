from src.modelo.observer.LogObserver import LogObserver
from src.modelo.observer.SujetoAuditoria import SujetoAuditoria
from src.modelo.PermisoServicio import PermisoServicio
from src.modelo.vo.LogVo import LogVo


class ServicioBase:
    def __init__(self):
        self._permiso_servicio = PermisoServicio()
        self._sujeto_auditoria = SujetoAuditoria()
        self._sujeto_auditoria.agregar_observador(LogObserver())

    def _registrar_log(self, user_id, event_type, reference_id, raw_data):
        try:
            log = LogVo(None, None, event_type, reference_id, raw_data, user_id)
            self._sujeto_auditoria.notificar(log)
        except Exception as error:
            print("No se pudo registrar log:", error)

    def _verificar_permiso(self, sesion, permiso, event_type):
        if not self._permiso_servicio.puede(sesion, permiso):
            user_id = None
            if sesion is not None:
                user_id = sesion.user_id
            self._registrar_log(user_id, "ACCION_NO_AUTORIZADA", None, event_type)
            raise Exception("Accion no autorizada")
