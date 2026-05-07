from src.modelo.dao.LoginDaoJDBC import LoginDaoJDBC
from src.modelo.vo.LoginVo import LoginVO


class LoginLogica:

    def __init__(self):
        self.__login_dao = LoginDaoJDBC()

    def hacerLogin(self, user, password):
        if user is None or user.strip() == "":
            raise ValueError("El usuario no puede estar vacío")

        if password is None or password.strip() == "":
            raise ValueError("La contraseña no puede estar vacía")

        login_vo = LoginVO(user, password)

        resultado = self.__login_dao.check_login(login_vo)

        return resultado