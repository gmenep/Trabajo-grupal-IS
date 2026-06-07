from src.modelo.ProyectoServicio import ProyectoServicio


class ProyectoController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = ProyectoServicio()
        self.__project_id_actual = None

    def cargar(self):
        proyectos = self.__servicio.listar_resumen_proyectos(self.__sesion)
        filas = []
        for proyecto in proyectos:
            filas.append({
                "project_id": proyecto.project_id,
                "title": proyecto.title,
                "description": proyecto.description,
                "start_date": proyecto.start_date,
                "end_date": proyecto.end_date,
                "state": proyecto.state,
                "asignaciones": proyecto.asignaciones
            })
        self.__view.mostrar_proyectos(filas)

    def cargar_miembros(self):
        actual = self.__view.obtener_proyecto_seleccionado()
        if actual is not None and actual.get("project_id") is not None:
            self.__project_id_actual = actual.get("project_id")
        if self.__project_id_actual is None:
            self.__view.mostrar_error("Selecciona un proyecto")
            return
        miembros = self.__servicio.listar_miembros(self.__sesion, self.__project_id_actual)
        filas = []
        for usuario in miembros:
            filas.append({
                "user_id": usuario.user_id,
                "login": usuario.login,
                "full_name": usuario.full_name,
                "dni": usuario.dni,
                "state": usuario.state
            })
        self.__view.mostrar_miembros(filas)

    def agregar_usuario(self):
        if self.__project_id_actual is None:
            actual = self.__view.obtener_proyecto_seleccionado()
            if actual is not None:
                self.__project_id_actual = actual.get("project_id")
        if self.__project_id_actual is None:
            self.__view.mostrar_error("Selecciona un proyecto")
            return
        datos = self.__view.pedir_usuario_proyecto()
        if datos is None:
            return
        self.__servicio.agregar_usuario_proyecto(
            self.__sesion,
            self.__project_id_actual,
            datos.get("user_id"),
            datos.get("role")
        )
        self.__view.mostrar_info("Usuario anadido al proyecto")
        self.cargar_miembros()

    def eliminar_usuario(self):
        if self.__project_id_actual is None:
            self.__view.mostrar_error("Selecciona un proyecto")
            return
        usuario = self.__view.obtener_proyecto_seleccionado()
        if usuario is None or usuario.get("user_id") is None:
            self.__view.mostrar_error("Selecciona un usuario del proyecto")
            return
        if not self.__view.confirmar("Eliminar usuario del proyecto?"):
            return
        self.__servicio.eliminar_usuario_proyecto(self.__sesion, self.__project_id_actual, usuario.get("user_id"))
        self.__view.mostrar_info("Usuario eliminado del proyecto")
        self.cargar_miembros()
