class RoleVo:
    def __init__(self, role_id, role_name, permisos):
        self.__role_id = role_id
        self.__role_name = role_name
        self.__permisos = permisos

    @property
    def role_id(self):
        return self.__role_id

    @property
    def role_name(self):
        return self.__role_name

    @property
    def permisos(self):
        return self.__permisos
