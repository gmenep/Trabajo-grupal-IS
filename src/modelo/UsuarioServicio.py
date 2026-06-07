from src.modelo.dao.RoleDaoJDBC import RoleDaoJDBC
from src.modelo.dao.UserRoleDaoJDBC import UserRoleDaoJDBC
from src.modelo.dao.UsersDaoJDBC import UsersDaoJDBC
from src.modelo.PasswordService import PasswordService
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.UserRoleVo import UserRoleVo
from src.modelo.vo.UsuarioVo import UsuarioVo


class UsuarioServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__users_dao = UsersDaoJDBC()
        self.__role_dao = RoleDaoJDBC()
        self.__user_role_dao = UserRoleDaoJDBC()
        self.__password_service = PasswordService()

    def listar_usuarios(self, sesion):
        self._verificar_permiso(sesion, "gestionar_usuarios", "CONSULTAR_USUARIOS")
        return self.__users_dao.select()

    def listar_roles(self, sesion):
        self._verificar_permiso(sesion, "gestionar_usuarios", "CONSULTAR_ROLES")
        return self.__role_dao.select()

    def crear_usuario(self, sesion, login, password, full_name, dni, state, studies, roles):
        self._verificar_permiso(sesion, "gestionar_usuarios", "CREAR_USUARIO")
        existente = self.__users_dao.select_by_login(login)
        if existente is not None:
            raise Exception("Ya existe un usuario con ese login")
        pass_hash = self.__password_service.hash_password(password)
        usuario = UsuarioVo(None, login, pass_hash, full_name, dni, state, studies)
        user_id = self.__users_dao.insert(usuario)
        self.__asignar_roles(user_id, roles)
        self._registrar_log(sesion.user_id, "CREAR_USUARIO", user_id, login)
        return user_id

    def modificar_usuario(self, sesion, user_id, login, full_name, dni, state, studies):
        self._verificar_permiso(sesion, "gestionar_usuarios", "MODIFICAR_USUARIO")
        actual = self.__users_dao.select_by_id(user_id)
        if actual is None:
            raise Exception("El usuario no existe")
        usuario = UsuarioVo(user_id, login, actual.pass_hash, full_name, dni, state, studies)
        self.__users_dao.update(usuario)
        self._registrar_log(sesion.user_id, "MODIFICAR_USUARIO", user_id, login)
        return True

    def dar_baja_usuario(self, sesion, user_id):
        self._verificar_permiso(sesion, "gestionar_usuarios", "ELIMINAR_USUARIO")
        self.__users_dao.deactivate(user_id)
        self._registrar_log(sesion.user_id, "ELIMINAR_USUARIO", user_id, "Usuario dado de baja")
        return True

    def resetear_password(self, sesion, user_id, password):
        self._verificar_permiso(sesion, "gestionar_usuarios", "RESETEAR_PASSWORD")
        actual = self.__users_dao.select_by_id(user_id)
        if actual is None:
            raise Exception("El usuario no existe")
        pass_hash = self.__password_service.hash_password(password)
        usuario = UsuarioVo(actual.user_id, actual.login, pass_hash, actual.full_name, actual.dni, actual.state, actual.studies)
        self.__users_dao.update(usuario)
        self._registrar_log(sesion.user_id, "RESETEAR_PASSWORD", user_id, "Cambio de hash")
        return True

    def asignar_rol(self, sesion, user_id, role_name):
        self._verificar_permiso(sesion, "gestionar_usuarios", "ASIGNAR_ROL")
        self.__asignar_roles(user_id, [role_name])
        self._registrar_log(sesion.user_id, "ASIGNAR_ROL", user_id, role_name)
        return True

    def quitar_rol(self, sesion, user_id, role_id):
        self._verificar_permiso(sesion, "gestionar_usuarios", "QUITAR_ROL")
        self.__user_role_dao.delete(user_id, role_id)
        self._registrar_log(sesion.user_id, "QUITAR_ROL", user_id, str(role_id))
        return True

    def __asignar_roles(self, user_id, roles):
        for role_name in roles:
            role = self.__role_dao.select_by_name(role_name)
            if role is not None:
                existe = False
                actuales = self.__user_role_dao.select_by_user(user_id)
                for relacion in actuales:
                    if relacion.role_id == role.role_id:
                        existe = True
                if not existe:
                    self.__user_role_dao.insert(UserRoleVo(user_id, role.role_id))
