class LoginVO:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
