class UsuarioVo:
    def __init__(
        self,
        user_id: int | None,
        login: str,
        pass_hash: str,
        full_name: str,
        dni: str,
        state: str,
        studies: str
    ) -> None:
        self.__user_id = user_id
        self.__login = login
        self.__pass_hash = pass_hash
        self.__full_name = full_name
        self.__dni = dni
        self.__state = state
        self.__studies = studies

    @property
    def user_id(self) -> int | None:
        return self.__user_id

    @property
    def login(self) -> str:
        return self.__login

    @property
    def pass_hash(self) -> str:
        return self.__pass_hash

    @property
    def full_name(self) -> str:
        return self.__full_name

    @property
    def dni(self) -> str:
        return self.__dni

    @property
    def state(self) -> str:
        return self.__state

    @property
    def studies(self) -> str:
        return self.__studies
