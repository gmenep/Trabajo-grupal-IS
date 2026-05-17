class StoredInVo:
    def __init__(
        self,
        material_id,
        storage_id,
        quantity,
        batch_number,
        exp_date
    ):
        self.__material_id = material_id
        self.__storage_id = storage_id
        self.__quantity = quantity
        self.__batch_number = batch_number
        self.__exp_date = exp_date

    @property
    def material_id(self):
        return self.__material_id

    @material_id.setter
    def material_id(self, material_id):
        self.__material_id = material_id

    @property
    def storage_id(self):
        return self.__storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        self.__storage_id = storage_id

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def batch_number(self):
        return self.__batch_number

    @batch_number.setter
    def batch_number(self, batch_number):
        self.__batch_number = batch_number

    @property
    def exp_date(self):
        return self.__exp_date

    @exp_date.setter
    def exp_date(self, exp_date):
        self.__exp_date = exp_date
