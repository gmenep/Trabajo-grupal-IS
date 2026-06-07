class MachineLocationVo:
    def __init__(self, machine_id, storage_id):
        self.__machine_id = machine_id
        self.__storage_id = storage_id

    @property
    def machine_id(self):
        return self.__machine_id

    @property
    def storage_id(self):
        return self.__storage_id
