class StorageVo:
    def __init__(
        self,
        storage_id: int | None,
        name: str,
        specifications: str
    ) -> None:
        self.__storage_id = storage_id
        self.__name = name
        self.__specifications = specifications

    @property
    def storage_id(self) -> int | None:
        return self.__storage_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def specifications(self) -> str:
        return self.__specifications
