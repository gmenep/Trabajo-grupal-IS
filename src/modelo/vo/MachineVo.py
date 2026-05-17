class MachineVo:
    def __init__(
        self,
        machine_id,
        state,
        last_revision_date,
        next_revision_date,
        description
    ):
        self.__machine_id = machine_id
        self.__state = state
        self.__last_revision_date = last_revision_date
        self.__next_revision_date = next_revision_date
        self.__description = description

    @property
    def machine_id(self):
        return self.__machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        self.__machine_id = machine_id

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def last_revision_date(self):
        return self.__last_revision_date

    @last_revision_date.setter
    def last_revision_date(self, last_revision_date):
        self.__last_revision_date = last_revision_date

    @property
    def next_revision_date(self):
        return self.__next_revision_date

    @next_revision_date.setter
    def next_revision_date(self, next_revision_date):
        self.__next_revision_date = next_revision_date

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
