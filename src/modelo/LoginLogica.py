from src.modelo.LoginServicio import LoginServicio


class LoginLogica:
    def __init__(self):
        self.__login_servicio = LoginServicio()

    def login(self, login_vo):
        return self.__login_servicio.login(login_vo.user, login_vo.password)

    def hacerLogin(self, login_vo):
        return self.login(login_vo)
