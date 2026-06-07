class MachineUsageVo:
    def __init__(self, usage_id, machine_id, user_id, project_id, start_date, end_date, state):
        self.__usage_id = usage_id
        self.__machine_id = machine_id
        self.__user_id = user_id
        self.__project_id = project_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__state = state

    @property
    def usage_id(self):
        return self.__usage_id

    @property
    def machine_id(self):
        return self.__machine_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def project_id(self):
        return self.__project_id

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @property
    def state(self):
        return self.__state
