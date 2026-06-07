class UsuarioVo:
    def __init__(self, user_id, login, pass_hash, full_name, dni, state, studies):
        self.__user_id = user_id
        self.__login = login
        self.__pass_hash = pass_hash
        self.__full_name = full_name
        self.__dni = dni
        self.__state = state
        self.__studies = studies

    @property
    def user_id(self):
        return self.__user_id

    @property
    def login(self):
        return self.__login

    @property
    def pass_hash(self):
        return self.__pass_hash

    @property
    def full_name(self):
        return self.__full_name

    @property
    def dni(self):
        return self.__dni

    @property
    def state(self):
        return self.__state

    @property
    def studies(self):
        return self.__studies
