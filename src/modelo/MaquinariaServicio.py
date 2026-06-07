from src.modelo.dao.AssetDaoJDBC import AssetDaoJDBC
from src.modelo.dao.MachineDaoJDBC import MachineDaoJDBC
from src.modelo.dao.MachineLocationDaoJDBC import MachineLocationDaoJDBC
from src.modelo.dao.MachineUsageDaoJDBC import MachineUsageDaoJDBC
from src.modelo.dao.StorageDaoJDBC import StorageDaoJDBC
from src.modelo.FechaServicio import FechaServicio
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.AssetVo import AssetVo
from src.modelo.vo.MachineLocationVo import MachineLocationVo
from src.modelo.vo.MachineUsageVo import MachineUsageVo
from src.modelo.vo.MachineVo import MachineVo


class MaquinariaServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__asset_dao = AssetDaoJDBC()
        self.__machine_dao = MachineDaoJDBC()
        self.__location_dao = MachineLocationDaoJDBC()
        self.__usage_dao = MachineUsageDaoJDBC()
        self.__storage_dao = StorageDaoJDBC()
        self.__fecha_servicio = FechaServicio()

    def listar_maquinaria(self, sesion, nombre, filtro):
        self._verificar_permiso(sesion, "maquinaria", "CONSULTAR_MAQUINARIA")
        self._registrar_log(sesion.user_id, "CONSULTAR_MAQUINARIA", None, "Consulta de maquinaria")
        return self.__machine_dao.select_inventario(nombre, filtro)

    def listar_disponibles(self, sesion):
        self._verificar_permiso(sesion, "solicitar_assets", "CONSULTAR_MAQUINAS_DISPONIBLES")
        return self.__machine_dao.select_disponibles()

    def listar_almacenes(self):
        return self.__storage_dao.select()

    def agregar_maquina(self, sesion, name, risk_level, state, last_revision_date, next_revision_date, description, storage_id):
        self._verificar_permiso(sesion, "maquinaria", "ANADIR_MAQUINA")
        self.__validar_riesgo(risk_level)
        ultima = self.__fecha_servicio.normalizar_fecha(last_revision_date, "La ultima revision")
        proxima = self.__fecha_servicio.normalizar_fecha(next_revision_date, "La proxima revision")
        self.__fecha_servicio.validar_orden(ultima, proxima, "la ultima revision", "la proxima revision")
        asset_id = self.__asset_dao.insert(AssetVo(None, name, "machine", risk_level))
        if asset_id is None:
            raise Exception("No se pudo crear el activo de la maquina")
        self.__machine_dao.insert(MachineVo(asset_id, state, ultima, proxima, description))
        if storage_id is not None:
            self.__location_dao.upsert(MachineLocationVo(asset_id, storage_id))
        self._registrar_log(sesion.user_id, "ANADIR_MAQUINA", asset_id, name)
        return asset_id

    def modificar_maquina(self, sesion, machine_id, name, risk_level, state, last_revision_date, next_revision_date, description):
        self._verificar_permiso(sesion, "maquinaria", "MODIFICAR_MAQUINA")
        self.__validar_riesgo(risk_level)
        ultima = self.__fecha_servicio.normalizar_fecha(last_revision_date, "La ultima revision")
        proxima = self.__fecha_servicio.normalizar_fecha(next_revision_date, "La proxima revision")
        self.__fecha_servicio.validar_orden(ultima, proxima, "la ultima revision", "la proxima revision")
        asset = self.__asset_dao.select_by_id(machine_id)
        if asset is None:
            raise Exception("La maquina no existe")
        self.__asset_dao.update(AssetVo(machine_id, name, "machine", risk_level))
        self.__machine_dao.update(MachineVo(machine_id, state, ultima, proxima, description))
        self._registrar_log(sesion.user_id, "MODIFICAR_MAQUINA", machine_id, name)
        return True

    def mover_maquina(self, sesion, machine_id, storage_id):
        self._verificar_permiso(sesion, "maquinaria", "MOVER_MAQUINA")
        self.__location_dao.upsert(MachineLocationVo(machine_id, storage_id))
        self._registrar_log(sesion.user_id, "MOVER_MAQUINA", machine_id, "Nuevo almacen " + str(storage_id))
        return True

    def eliminar_maquina(self, sesion, machine_id):
        self._verificar_permiso(sesion, "maquinaria", "ELIMINAR_MAQUINA")
        activos = self.__usage_dao.select_active_by_machine(machine_id)
        if len(activos) > 0:
            raise Exception("No se puede eliminar una maquina con uso activo")
        self.__location_dao.delete(machine_id)
        rows_machine = self.__machine_dao.delete(machine_id)
        rows_asset = self.__asset_dao.delete(machine_id)
        if rows_machine == 0 or rows_asset == 0:
            self.__machine_dao.update_state(machine_id, "Retirada")
        self._registrar_log(sesion.user_id, "ELIMINAR_MAQUINA", machine_id, "Maquina eliminada o retirada")
        return True

    def mantenimiento(self, sesion, machine_id, last_revision_date, next_revision_date, description):
        self._verificar_permiso(sesion, "maquinaria", "MANTENIMIENTO_MAQUINA")
        ultima = self.__fecha_servicio.normalizar_fecha(last_revision_date, "La ultima revision")
        proxima = self.__fecha_servicio.normalizar_fecha(next_revision_date, "La proxima revision")
        self.__fecha_servicio.validar_orden(ultima, proxima, "la ultima revision", "la proxima revision")
        maquina = self.__machine_dao.select_by_id(machine_id)
        if maquina is None:
            raise Exception("La maquina no existe")
        nueva = MachineVo(machine_id, "Mantenimiento", ultima, proxima, description)
        self.__machine_dao.update(nueva)
        self._registrar_log(sesion.user_id, "MANTENIMIENTO_MAQUINA", machine_id, description)
        return True

    def solicitar_maquina(self, sesion, machine_id, project_id):
        self._verificar_permiso(sesion, "solicitar_assets", "SOLICITAR_MAQUINA")
        if project_id is None:
            raise Exception("Selecciona un proyecto para usar la maquina")
        if project_id not in sesion.project_ids:
            raise Exception("No puedes solicitar maquinaria para un proyecto al que no perteneces")
        maquina = self.__machine_dao.select_by_id(machine_id)
        if maquina is None:
            raise Exception("La maquina no existe")
        if maquina.state != "Operativa":
            raise Exception("La maquina no esta operativa")
        activos = self.__usage_dao.select_active_by_machine(machine_id)
        if len(activos) > 0:
            raise Exception("La maquina ya esta en uso")
        self.__machine_dao.update_state(machine_id, "En uso")
        self.__usage_dao.insert(MachineUsageVo(None, machine_id, sesion.user_id, project_id, None, None, "ACTIVO"))
        self._registrar_log(sesion.user_id, "SOLICITAR_MAQUINA", machine_id, "Uso activo en proyecto " + str(project_id))
        return True

    def listar_usos_activos_usuario(self, sesion):
        self._verificar_permiso(sesion, "solicitar_assets", "CONSULTAR_USOS_MAQUINA")
        return self.__usage_dao.select_active_by_user(sesion.user_id)

    def finalizar_uso(self, sesion, usage_id):
        self._verificar_permiso(sesion, "solicitar_assets", "FINALIZAR_USO_MAQUINA")
        usos = self.__usage_dao.select_active_by_user(sesion.user_id)
        if len(usos) == 0:
            raise Exception("No estas utilizando maquinas en este momento.")
        uso_elegido = None
        for uso in usos:
            if usage_id is None or uso.usage_id == usage_id:
                uso_elegido = uso
                break
        if uso_elegido is None:
            raise Exception("Solo puedes finalizar tus propias maquinas")
        self.__usage_dao.finish(uso_elegido.usage_id, sesion.user_id)
        self.__machine_dao.update_state(uso_elegido.machine_id, "Operativa")
        self._registrar_log(sesion.user_id, "FINALIZAR_USO_MAQUINA", uso_elegido.machine_id, "Uso finalizado")
        return True

    def __validar_riesgo(self, risk_level):
        if risk_level not in ("Bajo", "Medio", "Alto"):
            raise Exception("El riesgo debe ser Bajo, Medio o Alto")
