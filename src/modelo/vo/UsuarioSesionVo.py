class UsuarioSesionVo:
    def __init__(self, user_id, login, full_name, dni, state, studies, roles, project_ids):
        self.__user_id = user_id
        self.__login = login
        self.__full_name = full_name
        self.__dni = dni
        self.__state = state
        self.__studies = studies
        self.__roles = roles
        self.__project_ids = project_ids

    @property
    def user_id(self):
        return self.__user_id

    @property
    def login(self):
        return self.__login

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

    @property
    def roles(self):
        return self.__roles

    @property
    def project_ids(self):
        return self.__project_ids
