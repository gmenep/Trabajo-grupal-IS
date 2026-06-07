class LogVo:
    def __init__(self, log_id, timestamp, event_type, reference_id, raw_data, user_id):
        self.__log_id = log_id
        self.__timestamp = timestamp
        self.__event_type = event_type
        self.__reference_id = reference_id
        self.__raw_data = raw_data
        self.__user_id = user_id

    @property
    def log_id(self):
        return self.__log_id

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def event_type(self):
        return self.__event_type

    @property
    def reference_id(self):
        return self.__reference_id

    @property
    def raw_data(self):
        return self.__raw_data

    @property
    def user_id(self):
        return self.__user_id
