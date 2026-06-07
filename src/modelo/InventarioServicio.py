from src.modelo.dao.AssetDaoJDBC import AssetDaoJDBC
from src.modelo.dao.MaterialDaoJDBC import MaterialDaoJDBC
from src.modelo.dao.MaterialMovementDaoJDBC import MaterialMovementDaoJDBC
from src.modelo.dao.StorageDaoJDBC import StorageDaoJDBC
from src.modelo.dao.StoredInDaoJDBC import StoredInDaoJDBC
from src.modelo.FechaServicio import FechaServicio
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.AssetVo import AssetVo
from src.modelo.vo.MaterialMovementVo import MaterialMovementVo
from src.modelo.vo.MaterialVo import MaterialVo
from src.modelo.vo.StoredInVo import StoredInVo


class InventarioServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__asset_dao = AssetDaoJDBC()
        self.__material_dao = MaterialDaoJDBC()
        self.__storage_dao = StorageDaoJDBC()
        self.__storedin_dao = StoredInDaoJDBC()
        self.__movement_dao = MaterialMovementDaoJDBC()
        self.__fecha_servicio = FechaServicio()

    def listar_inventario(self, sesion, nombre, storage_id):
        self._verificar_permiso(sesion, "inventario", "CONSULTAR_INVENTARIO")
        self._registrar_log(sesion.user_id, "CONSULTAR_INVENTARIO", None, "Consulta de inventario")
        return self.__material_dao.select_inventario(nombre, storage_id)

    def listar_materiales_agrupados(self, sesion):
        self._verificar_permiso(sesion, "solicitar_assets", "CONSULTAR_MATERIALES_DISPONIBLES")
        return self.__material_dao.select_agrupado()

    def listar_materiales(self):
        return self.__material_dao.select()

    def listar_almacenes(self):
        return self.__storage_dao.select()

    def agregar_material(self, sesion, name, risk_level, specifications, formula, measure_unit):
        self._verificar_permiso(sesion, "inventario", "ANADIR_MATERIAL")
        if name is None or name.strip() == "":
            raise Exception("El nombre del material es obligatorio")
        self.__validar_riesgo(risk_level)
        asset_id = self.__asset_dao.insert(AssetVo(None, name.strip(), "material", risk_level))
        if asset_id is None:
            raise Exception("No se pudo crear el activo del material")
        material = MaterialVo(asset_id, specifications, formula, measure_unit)
        self.__material_dao.insert(material)
        self._registrar_log(sesion.user_id, "ANADIR_MATERIAL", asset_id, name)
        return asset_id

    def agregar_lote(self, sesion, material_id, storage_id, batch_number, quantity, exp_date):
        self._verificar_permiso(sesion, "inventario", "ANADIR_LOTE")
        cantidad = self.__validar_cantidad(quantity)
        fecha_caducidad = self.__fecha_servicio.normalizar_fecha(exp_date, "La fecha de caducidad")
        existente = self.__storedin_dao.select_one(material_id, storage_id, batch_number)
        if existente is not None:
            cantidad = cantidad + float(existente.quantity)
            lote = StoredInVo(material_id, storage_id, cantidad, batch_number, fecha_caducidad)
            self.__storedin_dao.update(lote)
        else:
            lote = StoredInVo(material_id, storage_id, cantidad, batch_number, fecha_caducidad)
            self.__storedin_dao.insert(lote)
        self.__registrar_movimiento(material_id, storage_id, batch_number, sesion.user_id, quantity, "ENTRADA", "Alta de lote")
        self._registrar_log(sesion.user_id, "ANADIR_LOTE", material_id, batch_number)
        return True

    def modificar_lote(self, sesion, material_id, storage_id, batch_number, quantity, exp_date):
        self._verificar_permiso(sesion, "inventario", "MODIFICAR_LOTE")
        cantidad = float(quantity)
        if cantidad < 0:
            raise Exception("La cantidad no puede ser negativa")
        fecha_caducidad = self.__fecha_servicio.normalizar_fecha(exp_date, "La fecha de caducidad")
        existente = self.__storedin_dao.select_one(material_id, storage_id, batch_number)
        if existente is None:
            raise Exception("El lote no existe")
        if cantidad == 0:
            self.__storedin_dao.delete(material_id, storage_id, batch_number)
        else:
            self.__storedin_dao.update(StoredInVo(material_id, storage_id, cantidad, batch_number, fecha_caducidad))
        self.__registrar_movimiento(material_id, storage_id, batch_number, sesion.user_id, cantidad, "MOVIMIENTO", "Modificacion de lote")
        self._registrar_log(sesion.user_id, "MODIFICAR_LOTE", material_id, batch_number)
        return True

    def mover_lote(self, sesion, material_id, storage_origen_id, storage_destino_id, batch_number, quantity):
        self._verificar_permiso(sesion, "inventario", "MOVER_LOTE")
        cantidad = self.__validar_cantidad(quantity)
        if storage_origen_id == storage_destino_id:
            raise Exception("El almacen de origen y destino debe ser distinto")
        origen = self.__storedin_dao.select_one(material_id, storage_origen_id, batch_number)
        if origen is None:
            raise Exception("El lote de origen no existe")
        if float(origen.quantity) < cantidad:
            raise Exception("Cantidad insuficiente en el lote de origen")
        restante = float(origen.quantity) - cantidad
        if restante == 0:
            self.__storedin_dao.delete(material_id, storage_origen_id, batch_number)
        else:
            self.__storedin_dao.update_quantity(material_id, storage_origen_id, batch_number, restante)

        destino = self.__storedin_dao.select_one(material_id, storage_destino_id, batch_number)
        if destino is None:
            self.__storedin_dao.insert(StoredInVo(material_id, storage_destino_id, cantidad, batch_number, origen.exp_date))
        else:
            nueva_cantidad = float(destino.quantity) + cantidad
            self.__storedin_dao.update_quantity(material_id, storage_destino_id, batch_number, nueva_cantidad)
        self.__registrar_movimiento(material_id, storage_origen_id, batch_number, sesion.user_id, cantidad, "SALIDA", "Movimiento a otro almacen")
        self.__registrar_movimiento(material_id, storage_destino_id, batch_number, sesion.user_id, cantidad, "ENTRADA", "Movimiento desde otro almacen")
        self._registrar_log(sesion.user_id, "MOVER_LOTE", material_id, batch_number)
        return True

    def eliminar_lote(self, sesion, material_id, storage_id, batch_number):
        self._verificar_permiso(sesion, "inventario", "ELIMINAR_LOTE")
        self.__storedin_dao.delete(material_id, storage_id, batch_number)
        self._registrar_log(sesion.user_id, "ELIMINAR_LOTE", material_id, batch_number)
        return True

    def eliminar_material(self, sesion, material_id):
        self._verificar_permiso(sesion, "inventario", "ELIMINAR_MATERIAL")
        self.__storedin_dao.delete_by_material(material_id)
        self.__material_dao.delete(material_id)
        self.__asset_dao.delete(material_id)
        self._registrar_log(sesion.user_id, "ELIMINAR_MATERIAL", material_id, "Material eliminado")
        return True

    def solicitar_material(self, sesion, material_id, quantity):
        self._verificar_permiso(sesion, "solicitar_assets", "SOLICITAR_MATERIAL")
        cantidad = self.__validar_cantidad(quantity)
        total = float(self.__storedin_dao.total_by_material(material_id))
        if total < cantidad:
            raise Exception("No hay cantidad suficiente disponible")
        lotes = self.__storedin_dao.select_by_material(material_id)
        restante = cantidad
        for lote in lotes:
            if restante <= 0:
                break
            disponible = float(lote.quantity)
            usado = restante
            if disponible < usado:
                usado = disponible
            nueva_cantidad = disponible - usado
            if nueva_cantidad == 0:
                self.__storedin_dao.delete(lote.material_id, lote.storage_id, lote.batch_number)
            else:
                self.__storedin_dao.update_quantity(lote.material_id, lote.storage_id, lote.batch_number, nueva_cantidad)
            self.__registrar_movimiento(lote.material_id, lote.storage_id, lote.batch_number, sesion.user_id, usado, "SOLICITUD", "Solicitud de material")
            restante = restante - usado
        self._registrar_log(sesion.user_id, "SOLICITAR_MATERIAL", material_id, "Cantidad " + str(quantity))
        return True

    def devolver_material(self, sesion, material_id, storage_id, batch_number, quantity, exp_date):
        self._verificar_permiso(sesion, "solicitar_assets", "DEVOLVER_MATERIAL")
        cantidad = self.__validar_cantidad(quantity)
        fecha_caducidad = self.__fecha_servicio.normalizar_fecha(exp_date, "La fecha de caducidad")
        existente = self.__storedin_dao.select_one(material_id, storage_id, batch_number)
        if existente is None:
            self.__storedin_dao.insert(StoredInVo(material_id, storage_id, cantidad, batch_number, fecha_caducidad))
        else:
            self.__storedin_dao.update_quantity(material_id, storage_id, batch_number, float(existente.quantity) + cantidad)
        self.__registrar_movimiento(material_id, storage_id, batch_number, sesion.user_id, cantidad, "DEVOLUCION", "Devolucion de material")
        self._registrar_log(sesion.user_id, "DEVOLVER_MATERIAL", material_id, "Cantidad " + str(quantity))
        return True

    def __validar_cantidad(self, quantity):
        cantidad = float(quantity)
        if cantidad <= 0:
            raise Exception("La cantidad debe ser mayor que cero")
        return cantidad

    def __validar_riesgo(self, risk_level):
        if risk_level not in ("Bajo", "Medio", "Alto"):
            raise Exception("El riesgo debe ser Bajo, Medio o Alto")

    def __registrar_movimiento(self, material_id, storage_id, batch_number, user_id, quantity, movement_type, notes):
        movimiento = MaterialMovementVo(None, material_id, storage_id, batch_number, user_id, quantity, movement_type, None, notes)
        self.__movement_dao.insert(movimiento)
