class StudyVo:
    def __init__(self, study_id: int | None, project_id: int | None) -> None:
        self.__study_id = study_id
        self.__project_id = project_id

    @property
    def study_id(self) -> int | None:
        return self.__study_id

    @property
    def project_id(self) -> int | None:
        return self.__project_id
