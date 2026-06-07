class PanelEntryVo:
    def __init__(self, entry_id, project_id, study_id, user_id, title, content, created_at, project_title, study_label, author_name):
        self.__entry_id = entry_id
        self.__project_id = project_id
        self.__study_id = study_id
        self.__user_id = user_id
        self.__title = title
        self.__content = content
        self.__created_at = created_at
        self.__project_title = project_title
        self.__study_label = study_label
        self.__author_name = author_name

    @property
    def entry_id(self):
        return self.__entry_id

    @property
    def project_id(self):
        return self.__project_id

    @property
    def study_id(self):
        return self.__study_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    @property
    def created_at(self):
        return self.__created_at

    @property
    def project_title(self):
        return self.__project_title

    @property
    def study_label(self):
        return self.__study_label

    @property
    def author_name(self):
        return self.__author_name
