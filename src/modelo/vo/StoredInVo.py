class StoredInVo:
    def __init__(
        self,
        material_id: int,
        storage_id: int,
        quantity,
        batch_number: str,
        exp_date
    ) -> None:
        self.__material_id = material_id
        self.__storage_id = storage_id
        self.__quantity = quantity
        self.__batch_number = batch_number
        self.__exp_date = exp_date

    @property
    def material_id(self) -> int:
        return self.__material_id

    @property
    def storage_id(self) -> int:
        return self.__storage_id

    @property
    def quantity(self):
        return self.__quantity

    @property
    def batch_number(self) -> str:
        return self.__batch_number

    @property
    def exp_date(self):
        return self.__exp_date
