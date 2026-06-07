from src.modelo.InventarioServicio import InventarioServicio


class InventarioController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = InventarioServicio()
        self.__almacenes = []

    def cargar(self):
        self.__almacenes = self.__servicio.listar_almacenes()
        self.__view.cargar_almacenes(self.__almacenes)
        nombre = self.__view.obtener_busqueda_inventario()
        storage_id = self.__view.obtener_almacen_inventario()
        datos = self.__servicio.listar_inventario(self.__sesion, nombre, storage_id)
        filas = []
        for material in datos:
            filas.append(self.__material_a_fila(material))
        self.__view.mostrar_inventario(filas)

    def buscar(self):
        self.cargar()

    def crear_material(self):
        datos = self.__view.pedir_material()
        if datos is None:
            return
        self.__servicio.agregar_material(
            self.__sesion,
            datos.get("name"),
            datos.get("risk_level"),
            datos.get("specifications"),
            datos.get("formula"),
            datos.get("measure_unit")
        )
        self.__view.mostrar_info("Material creado")
        self.cargar()

    def crear_lote(self):
        datos = self.__view.pedir_lote(self.__servicio.listar_materiales(), self.__servicio.listar_almacenes(), None)
        if datos is None:
            return
        self.__servicio.agregar_lote(
            self.__sesion,
            datos.get("material_id"),
            datos.get("storage_id"),
            datos.get("batch_number"),
            datos.get("quantity"),
            datos.get("exp_date")
        )
        self.__view.mostrar_info("Lote creado")
        self.cargar()

    def modificar_lote(self):
        actual = self.__view.obtener_material_seleccionado()
        if actual is None:
            self.__view.mostrar_error("Selecciona una fila")
            return
        datos = self.__view.pedir_lote(self.__servicio.listar_materiales(), self.__servicio.listar_almacenes(), actual)
        if datos is None:
            return
        self.__servicio.modificar_lote(
            self.__sesion,
            datos.get("material_id"),
            datos.get("storage_id"),
            datos.get("batch_number"),
            datos.get("quantity"),
            datos.get("exp_date")
        )
        self.__view.mostrar_info("Lote modificado")
        self.cargar()

    def mover_lote(self):
        actual = self.__view.obtener_material_seleccionado()
        if actual is None:
            self.__view.mostrar_error("Selecciona un lote")
            return
        if actual.get("storage_id") is None or actual.get("batch_number") in (None, ""):
            self.__view.mostrar_error("Selecciona un lote almacenado")
            return
        datos = self.__view.pedir_movimiento_lote(self.__servicio.listar_almacenes(), actual)
        if datos is None:
            return
        self.__servicio.mover_lote(
            self.__sesion,
            datos.get("material_id"),
            datos.get("storage_origen_id"),
            datos.get("storage_destino_id"),
            datos.get("batch_number"),
            datos.get("quantity")
        )
        self.__view.mostrar_info("Lote movido")
        self.cargar()

    def eliminar(self):
        actual = self.__view.obtener_material_seleccionado()
        if actual is None:
            self.__view.mostrar_error("Selecciona una fila")
            return
        if not self.__view.confirmar("Eliminar seleccion?"):
            return
        if actual.get("batch_number") in (None, ""):
            self.__servicio.eliminar_material(self.__sesion, actual.get("material_id"))
        else:
            self.__servicio.eliminar_lote(
                self.__sesion,
                actual.get("material_id"),
                actual.get("storage_id"),
                actual.get("batch_number")
            )
        self.__view.mostrar_info("Eliminado")
        self.cargar()

    def solicitar_material(self):
        materiales = self.__servicio.listar_materiales_agrupados(self.__sesion)
        datos = self.__view.pedir_solicitud_material(materiales)
        if datos is None:
            return
        self.__servicio.solicitar_material(self.__sesion, datos.get("material_id"), datos.get("quantity"))
        self.__view.mostrar_info("Material solicitado")

    def __material_a_fila(self, material):
        return {
            "material_id": material.material_id,
            "name": material.name,
            "storage_id": material.storage_id,
            "storage_name": material.storage_name,
            "batch_number": material.batch_number,
            "risk_level": material.risk_level,
            "formula": material.formula,
            "measure_unit": material.measure_unit,
            "quantity": material.quantity,
            "exp_date": material.exp_date
        }
