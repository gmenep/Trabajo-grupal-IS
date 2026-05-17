class RoleVo:
    def __init__(
        self,
        role_id: int | None,
        role_name: str,
        permisos: str
    ) -> None:
        self.__role_id = role_id
        self.__role_name = role_name
        self.__permisos = permisos

    @property
    def role_id(self) -> int | None:
        return self.__role_id

    @property
    def role_name(self) -> str:
        return self.__role_name

    @property
    def permisos(self) -> str:
        return self.__permisos
