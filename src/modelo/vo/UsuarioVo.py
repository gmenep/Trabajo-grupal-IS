class UsuarioVo:
    def __init__(self, user_id, login, pass_hash, full_name, DNI, state, studies):
        self.__id = user_id
        self.__login = login
        self.__pass = pass_hash
        self.__name = full_name
        self.__dni = DNI
        self.__state = state
        self.__studies = studies