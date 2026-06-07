class ProjectVo:
    def __init__(self, project_id, title, description, start_date, end_date, state):
        self.__project_id = project_id
        self.__title = title
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date
        self.__state = state

    @property
    def project_id(self):
        return self.__project_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @property
    def state(self):
        return self.__state
