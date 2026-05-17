from src.modelo.dao.LoginDaoJDBC import LoginDaoJDBC
from src.modelo.PasswordLogica import PasswordLogica
from src.modelo.vo.UsuarioVo import UsuarioVo


class LoginLogica:

    def __init__(self):
        self.__login_dao = LoginDaoJDBC()
        self.__password_logica = PasswordLogica()

    def login(self, login_vo):
        self.validar_login_vo(login_vo)

        usuario = self.__login_dao.select_by_login(login_vo.user)

        if usuario is None:
            return None

        password_correcta = self.__password_logica.verificar_password(
            login_vo.password,
            usuario.pass_hash
        )

        if not password_correcta:
            return None

        return self.usuario_sin_hash(usuario)

    def hacerLogin(self, login_vo):
        return self.login(login_vo)

    def validar_login_vo(self, login_vo):
        if login_vo is None:
            raise ValueError("Los datos de login no pueden estar vacios")

        if login_vo.user is None or login_vo.user.strip() == "":
            raise ValueError("El usuario no puede estar vacio")

        if login_vo.password is None or login_vo.password.strip() == "":
            raise ValueError("La contrasena no puede estar vacia")

    def usuario_sin_hash(self, usuario):
        return UsuarioVo(
            usuario.user_id,
            usuario.login,
            None,
            usuario.full_name,
            usuario.dni,
            usuario.state,
            usuario.studies
        )
