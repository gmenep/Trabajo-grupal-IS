class ProyectoAsignacionVo:
    def __init__(self, project_id, machine_id, machine_name, user_id, user_name):
        self.__project_id = project_id
        self.__machine_id = machine_id
        self.__machine_name = machine_name
        self.__user_id = user_id
        self.__user_name = user_name

    @property
    def project_id(self):
        return self.__project_id

    @property
    def machine_id(self):
        return self.__machine_id

    @property
    def machine_name(self):
        return self.__machine_name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_name(self):
        return self.__user_name
