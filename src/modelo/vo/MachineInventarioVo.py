class MachineInventarioVo:
    def __init__(self, machine_id, name, risk_level, state, last_revision_date, next_revision_date, description, storage_id, storage_name):
        self.__machine_id = machine_id
        self.__name = name
        self.__risk_level = risk_level
        self.__state = state
        self.__last_revision_date = last_revision_date
        self.__next_revision_date = next_revision_date
        self.__description = description
        self.__storage_id = storage_id
        self.__storage_name = storage_name

    @property
    def machine_id(self):
        return self.__machine_id

    @property
    def name(self):
        return self.__name

    @property
    def risk_level(self):
        return self.__risk_level

    @property
    def state(self):
        return self.__state

    @property
    def last_revision_date(self):
        return self.__last_revision_date

    @property
    def next_revision_date(self):
        return self.__next_revision_date

    @property
    def description(self):
        return self.__description

    @property
    def storage_id(self):
        return self.__storage_id

    @property
    def storage_name(self):
        return self.__storage_name
