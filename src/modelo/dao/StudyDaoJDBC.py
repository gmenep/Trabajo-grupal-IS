from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.StudyVo import StudyVo


class StudyDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = "SELECT study_id, project_id FROM studies ORDER BY study_id"
    SQL_SELECT_BY_PROJECT = "SELECT study_id, project_id FROM studies WHERE project_id = ? ORDER BY study_id"
    SQL_INSERT = "INSERT INTO studies(project_id) VALUES(?)"
    SQL_DELETE = "DELETE FROM studies WHERE study_id = ?"

    def select(self):
        return self.__rows_to_vo(self._select(self.SQL_SELECT, ()))

    def select_by_project(self, project_id):
        return self.__rows_to_vo(self._select(self.SQL_SELECT_BY_PROJECT, (project_id,)))

    def insert(self, study):
        return self._insert_id(self.SQL_INSERT, (study.project_id,))

    def delete(self, study_id):
        return self._write(self.SQL_DELETE, (study_id,))

    def __rows_to_vo(self, filas):
        estudios = []
        for fila in filas:
            estudios.append(StudyVo(fila[0], fila[1]))
        return estudios
