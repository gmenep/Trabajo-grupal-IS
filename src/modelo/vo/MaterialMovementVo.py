class MaterialMovementVo:
    def __init__(self, movement_id, material_id, storage_id, batch_number, user_id, quantity, movement_type, movement_date, notes):
        self.__movement_id = movement_id
        self.__material_id = material_id
        self.__storage_id = storage_id
        self.__batch_number = batch_number
        self.__user_id = user_id
        self.__quantity = quantity
        self.__movement_type = movement_type
        self.__movement_date = movement_date
        self.__notes = notes

    @property
    def movement_id(self):
        return self.__movement_id

    @property
    def material_id(self):
        return self.__material_id

    @property
    def storage_id(self):
        return self.__storage_id

    @property
    def batch_number(self):
        return self.__batch_number

    @property
    def user_id(self):
        return self.__user_id

    @property
    def quantity(self):
        return self.__quantity

    @property
    def movement_type(self):
        return self.__movement_type

    @property
    def movement_date(self):
        return self.__movement_date

    @property
    def notes(self):
        return self.__notes
