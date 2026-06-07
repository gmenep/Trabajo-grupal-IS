class LoginVo:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password


class LoginVO(LoginVo):
    pass
