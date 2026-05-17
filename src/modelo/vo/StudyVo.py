class StudyVo:
    def __init__(self, study_id, project_id):
        self.__study_id = study_id
        self.__project_id = project_id

    @property
    def study_id(self):
        return self.__study_id

    @study_id.setter
    def study_id(self, study_id):
        self.__study_id = study_id

    @property
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, project_id):
        self.__project_id = project_id
