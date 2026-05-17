class UsuarioVo:
    def __init__(
        self,
        user_id,
        login,
        pass_hash,
        full_name,
        dni,
        state,
        studies
    ):
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

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def pass_hash(self):
        return self.__pass_hash

    @pass_hash.setter
    def pass_hash(self, pass_hash):
        self.__pass_hash = pass_hash

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def studies(self):
        return self.__studies

    @studies.setter
    def studies(self, studies):
        self.__studies = studies
