class BelongsToVo:
    def __init__(self, project_id, user_id):
        self.__project_id = project_id
        self.__user_id = user_id

    @property
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, project_id):
        self.__project_id = project_id

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id
