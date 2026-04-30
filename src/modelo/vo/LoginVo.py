class LoginVO:
    def __init__(self, user: str, password: str) -> None:
        self.__user = user
        self.__password = password

    @property
    def user(self) -> str:
        return self.__user
    
    @property
    def password(self) -> str:
        return self.__password