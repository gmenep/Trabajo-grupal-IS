class ProjectVo:
    def __init__(
        self,
        project_id,
        title,
        description,
        start_date,
        end_date,
        state
    ):
        self.__project_id = project_id
        self.__title = title
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date
        self.__state = state

    @property
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, project_id):
        self.__project_id = project_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        self.__end_date = end_date

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
