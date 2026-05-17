class StorageVo:
    def __init__(
        self,
        storage_id,
        name,
        specifications
    ):
        self.__storage_id = storage_id
        self.__name = name
        self.__specifications = specifications

    @property
    def storage_id(self):
        return self.__storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        self.__storage_id = storage_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def specifications(self):
        return self.__specifications

    @specifications.setter
    def specifications(self, specifications):
        self.__specifications = specifications
