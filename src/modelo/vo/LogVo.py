class LogVo:
    def __init__(
        self,
        log_id: int | None,
        timestamp,
        event_type: str,
        reference_id: int | None,
        raw_data: str,
        user_id: int | None
    ) -> None:
        self.__log_id = log_id
        self.__timestamp = timestamp
        self.__event_type = event_type
        self.__reference_id = reference_id
        self.__raw_data = raw_data
        self.__user_id = user_id

    @property
    def log_id(self) -> int | None:
        return self.__log_id

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def event_type(self) -> str:
        return self.__event_type

    @property
    def reference_id(self) -> int | None:
        return self.__reference_id

    @property
    def raw_data(self) -> str:
        return self.__raw_data

    @property
    def user_id(self) -> int | None:
        return self.__user_id
