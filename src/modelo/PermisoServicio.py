class PermisoServicio:
    def __init__(self):
        self.__permisos_tecnico = ["maquinaria", "ayuda", "salir"]
        self.__permisos = {
            "inventario": ["Administrador", "Reponedor"],
            "maquinaria": ["Administrador", "Tecnico"],
            "proyectos": ["Administrador", "Investigador", "Director", "Auditor"],
            "panel": ["Investigador", "Director", "Administrador"],
            "administracion": ["Administrador"],
            "logs": ["Administrador", "Auditor", "Director"],
            "backup": ["Administrador"],
            "estadisticas": ["Administrador"],
            "ayuda": ["Administrador", "Director", "Investigador", "Auditor", "Tecnico", "Reponedor"],
            "solicitar_assets": ["Investigador", "Director"],
            "crear_proyecto": ["Director"],
            "ver_miembros_proyecto": ["Auditor", "Director"],
            "modificar_proyecto_usuarios": ["Director"],
            "finalizar_proyecto": ["Director"],
            "modificar_panel": ["Administrador", "Director"],
            "gestionar_usuarios": ["Administrador"],
            "salir": ["Administrador", "Director", "Investigador", "Auditor", "Tecnico", "Reponedor"]
        }

    def puede(self, sesion, permiso):
        if sesion is None:
            return False
        if "Tecnico" in sesion.roles and permiso not in self.__permisos_tecnico:
            return False
        roles_permitidos = self.__permisos.get(permiso, [])
        for rol in sesion.roles:
            if rol in roles_permitidos:
                return True
        return False

    def tiene_rol(self, sesion, role_name):
        if sesion is None:
            return False
        return role_name in sesion.roles

    def permisos_modulos(self, sesion):
        modulos = {}
        for permiso in self.__permisos:
            modulos[permiso] = self.puede(sesion, permiso)
        return modulos
