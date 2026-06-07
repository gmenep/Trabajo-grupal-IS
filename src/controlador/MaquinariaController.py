from src.modelo.MaquinariaServicio import MaquinariaServicio


class MaquinariaController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = MaquinariaServicio()

    def cargar(self):
        almacenes = self.__servicio.listar_almacenes()
        self.__view.cargar_filtros_maquinaria(almacenes)
        nombre = self.__view.obtener_busqueda_maquinaria()
        filtro = self.__view.obtener_filtro_maquinaria()
        datos = self.__servicio.listar_maquinaria(self.__sesion, nombre, filtro)
        filas = []
        for maquina in datos:
            filas.append(self.__maquina_a_fila(maquina))
        self.__view.mostrar_maquinaria(filas)

    def buscar(self):
        self.cargar()

    def crear_maquina(self):
        datos = self.__view.pedir_maquina(self.__servicio.listar_almacenes(), None)
        if datos is None:
            return
        self.__servicio.agregar_maquina(
            self.__sesion,
            datos.get("name"),
            datos.get("risk_level"),
            datos.get("state"),
            datos.get("last_revision_date"),
            datos.get("next_revision_date"),
            datos.get("description"),
            datos.get("storage_id")
        )
        self.__view.mostrar_info("Maquina creada")
        self.cargar()

    def modificar_maquina(self):
        actual = self.__view.obtener_maquina_seleccionada()
        if actual is None:
            self.__view.mostrar_error("Selecciona una maquina")
            return
        datos = self.__view.pedir_maquina(self.__servicio.listar_almacenes(), actual)
        if datos is None:
            return
        self.__servicio.modificar_maquina(
            self.__sesion,
            actual.get("machine_id"),
            datos.get("name"),
            datos.get("risk_level"),
            datos.get("state"),
            datos.get("last_revision_date"),
            datos.get("next_revision_date"),
            datos.get("description")
        )
        self.__view.mostrar_info("Maquina modificada")
        self.cargar()

    def mover_maquina(self):
        actual = self.__view.obtener_maquina_seleccionada()
        if actual is None:
            self.__view.mostrar_error("Selecciona una maquina")
            return
        datos = self.__view.pedir_movimiento_maquina(self.__servicio.listar_almacenes())
        if datos is None:
            return
        self.__servicio.mover_maquina(self.__sesion, actual.get("machine_id"), datos.get("storage_id"))
        self.__view.mostrar_info("Maquina movida")
        self.cargar()

    def eliminar_maquina(self):
        actual = self.__view.obtener_maquina_seleccionada()
        if actual is None:
            self.__view.mostrar_error("Selecciona una maquina")
            return
        if not self.__view.confirmar("Eliminar maquina seleccionada?"):
            return
        self.__servicio.eliminar_maquina(self.__sesion, actual.get("machine_id"))
        self.__view.mostrar_info("Maquina eliminada")
        self.cargar()

    def mantenimiento(self):
        actual = self.__view.obtener_maquina_seleccionada()
        if actual is None:
            self.__view.mostrar_error("Selecciona una maquina")
            return
        datos = self.__view.pedir_maquina(self.__servicio.listar_almacenes(), actual)
        if datos is None:
            return
        self.__servicio.mantenimiento(
            self.__sesion,
            actual.get("machine_id"),
            datos.get("last_revision_date"),
            datos.get("next_revision_date"),
            datos.get("description")
        )
        self.__view.mostrar_info("Mantenimiento registrado")
        self.cargar()

    def solicitar_maquina(self):
        proyecto = self.__view.obtener_proyecto_seleccionado()
        if proyecto is None or proyecto.get("project_id") is None:
            self.__view.mostrar_error("Selecciona primero un proyecto en la tabla de proyectos")
            return
        datos = self.__view.pedir_solicitud_maquina(self.__servicio.listar_disponibles(self.__sesion))
        if datos is None:
            return
        self.__servicio.solicitar_maquina(self.__sesion, datos.get("machine_id"), proyecto.get("project_id"))
        self.__view.mostrar_info("Maquina solicitada")

    def finalizar_uso(self):
        usos = self.__servicio.listar_usos_activos_usuario(self.__sesion)
        if len(usos) == 0:
            self.__view.mostrar_error("No estas utilizando maquinas en este momento")
            return
        datos = self.__view.pedir_finalizar_uso(usos)
        if datos is None:
            return
        self.__servicio.finalizar_uso(self.__sesion, datos.get("usage_id"))
        self.__view.mostrar_info("Uso finalizado")

    def __maquina_a_fila(self, maquina):
        return {
            "machine_id": maquina.machine_id,
            "name": maquina.name,
            "risk_level": maquina.risk_level,
            "state": maquina.state,
            "last_revision_date": maquina.last_revision_date,
            "next_revision_date": maquina.next_revision_date,
            "description": maquina.description,
            "storage_id": maquina.storage_id,
            "storage_name": maquina.storage_name
        }
