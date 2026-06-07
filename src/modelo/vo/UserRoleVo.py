class UserRoleVo:
    def __init__(self, user_id, role_id):
        self.__user_id = user_id
        self.__role_id = role_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def role_id(self):
        return self.__role_id
