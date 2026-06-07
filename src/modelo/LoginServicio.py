from src.modelo.dao.BelongsToDaoJDBC import BelongsToDaoJDBC
from src.modelo.dao.LoginDaoJDBC import LoginDaoJDBC
from src.modelo.dao.UserRoleDaoJDBC import UserRoleDaoJDBC
from src.modelo.PasswordService import PasswordService
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.UsuarioSesionVo import UsuarioSesionVo


class LoginServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__login_dao = LoginDaoJDBC()
        self.__user_role_dao = UserRoleDaoJDBC()
        self.__belongs_to_dao = BelongsToDaoJDBC()
        self.__password_service = PasswordService()

    def login(self, login, password):
        usuario = self.__login_dao.select_by_login(login)
        if usuario is None:
            self._registrar_log(None, "LOGIN_FALLIDO", None, "Usuario no encontrado: " + str(login))
            raise Exception("Usuario o contrasena incorrectos")

        if usuario.state != "Activo":
            self._registrar_log(usuario.user_id, "LOGIN_FALLIDO", usuario.user_id, "Usuario no activo")
            raise Exception("El usuario no esta activo")

        correcto = self.__password_service.verificar_password(password, usuario.pass_hash)
        if not correcto:
            self._registrar_log(usuario.user_id, "LOGIN_FALLIDO", usuario.user_id, "Contrasena incorrecta")
            raise Exception("Usuario o contrasena incorrectos")

        roles = self.__user_role_dao.select_role_names_by_user(usuario.user_id)
        if len(roles) == 0:
            self._registrar_log(usuario.user_id, "LOGIN_FALLIDO", usuario.user_id, "Usuario sin rol")
            raise Exception("El usuario no tiene roles asignados")

        project_ids = self.__belongs_to_dao.select_project_ids_by_user(usuario.user_id)
        sesion = UsuarioSesionVo(
            usuario.user_id,
            usuario.login,
            usuario.full_name,
            usuario.dni,
            usuario.state,
            usuario.studies,
            roles,
            project_ids
        )
        self._registrar_log(usuario.user_id, "LOGIN_CORRECTO", usuario.user_id, "Inicio de sesion correcto")
        return sesion
