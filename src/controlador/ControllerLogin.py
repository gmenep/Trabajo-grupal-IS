from src.modelo.vo.LoginVo import LoginVO

class ControllerLogin:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def show_login(self):
        self.__view.show()

    def login(self, username, password):
        login_vo = LoginVO(username, password)

        self.__view.warning_message("Login incorrecto")
        
        return self.__model.login(login_vo)
    