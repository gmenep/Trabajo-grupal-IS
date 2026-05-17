class BelongsToVo:
    def __init__(self, project_id: int, user_id: int) -> None:
        self.__project_id = project_id
        self.__user_id = user_id

    @property
    def project_id(self) -> int:
        return self.__project_id

    @property
    def user_id(self) -> int:
        return self.__user_id
