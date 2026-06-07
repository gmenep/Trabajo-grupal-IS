class ProyectoMiembroVo:
    def __init__(self, user_id, role_name, full_name, dni, state):
        self.__user_id = user_id
        self.__role_name = role_name
        self.__full_name = full_name
        self.__dni = dni
        self.__state = state

    @property
    def user_id(self):
        return self.__user_id

    @property
    def role_name(self):
        return self.__role_name

    @property
    def full_name(self):
        return self.__full_name

    @property
    def dni(self):
        return self.__dni

    @property
    def state(self):
        return self.__state
