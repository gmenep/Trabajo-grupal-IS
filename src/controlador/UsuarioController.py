from src.modelo.UsuarioServicio import UsuarioServicio


class UsuarioController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = UsuarioServicio()

    def cargar(self):
        usuarios = self.__servicio.listar_usuarios(self.__sesion)
        filas = []
        for usuario in usuarios:
            filas.append({
                "user_id": usuario.user_id,
                "login": usuario.login,
                "full_name": usuario.full_name,
                "dni": usuario.dni,
                "state": usuario.state,
                "studies": usuario.studies
            })
        self.__view.mostrar_usuarios(filas)

    def crear(self):
        datos = self.__view.pedir_usuario(self.__servicio.listar_roles(self.__sesion), None, True)
        if datos is None:
            return
        self.__servicio.crear_usuario(
            self.__sesion,
            datos.get("login"),
            datos.get("password"),
            datos.get("full_name"),
            datos.get("dni"),
            datos.get("state"),
            datos.get("studies"),
            [datos.get("role")]
        )
        self.__view.mostrar_info("Usuario creado")
        self.cargar()

    def modificar(self):
        actual = self.__view.obtener_usuario_seleccionado()
        if actual is None:
            self.__view.mostrar_error("Selecciona un usuario")
            return
        datos = self.__view.pedir_usuario(self.__servicio.listar_roles(self.__sesion), actual, False)
        if datos is None:
            return
        self.__servicio.modificar_usuario(
            self.__sesion,
            actual.get("user_id"),
            datos.get("login"),
            datos.get("full_name"),
            datos.get("dni"),
            datos.get("state"),
            datos.get("studies")
        )
        if datos.get("role") is not None:
            self.__servicio.asignar_rol(self.__sesion, actual.get("user_id"), datos.get("role"))
        self.__view.mostrar_info("Usuario modificado")
        self.cargar()

    def baja(self):
        actual = self.__view.obtener_usuario_seleccionado()
        if actual is None:
            self.__view.mostrar_error("Selecciona un usuario")
            return
        if not self.__view.confirmar("Dar de baja el usuario seleccionado?"):
            return
        self.__servicio.dar_baja_usuario(self.__sesion, actual.get("user_id"))
        self.__view.mostrar_info("Usuario dado de baja")
        self.cargar()
