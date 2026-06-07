from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.ProjectVo import ProjectVo


class ProjectDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = """
        SELECT project_id, title, description, start_date, end_date, state
        FROM projects
        ORDER BY title
    """
    SQL_SELECT_BY_ID = """
        SELECT project_id, title, description, start_date, end_date, state
        FROM projects
        WHERE project_id = ?
    """
    SQL_SELECT_BY_TITLE = """
        SELECT project_id, title, description, start_date, end_date, state
        FROM projects
        WHERE title = ?
    """
    SQL_INSERT = """
        INSERT INTO projects(title, description, start_date, end_date, state)
        VALUES(?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE projects
        SET title = ?, description = ?, start_date = ?, end_date = ?, state = ?
        WHERE project_id = ?
    """
    SQL_FINALIZAR = """
        UPDATE projects
        SET end_date = CURDATE(), state = ?
        WHERE project_id = ?
    """
    SQL_DELETE = "DELETE FROM projects WHERE project_id = ?"

    def select(self):
        proyectos = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            proyectos.append(self.__row_to_vo(fila))
        return proyectos

    def select_by_id(self, project_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (project_id,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def select_by_title(self, title):
        fila = self._select_one(self.SQL_SELECT_BY_TITLE, (title,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def insert(self, project):
        return self._insert_id(self.SQL_INSERT, (project.title, project.description, project.start_date, project.end_date, project.state))

    def update(self, project):
        return self._write(self.SQL_UPDATE, (project.title, project.description, project.start_date, project.end_date, project.state, project.project_id))

    def finalizar(self, project_id):
        return self._write(self.SQL_FINALIZAR, ("Finalizado", project_id))

    def delete(self, project_id):
        return self._write(self.SQL_DELETE, (project_id,))

    def insert_if_not_exists(self, project):
        existente = self.select_by_title(project.title)
        if existente is not None:
            return existente.project_id
        return self.insert(project)

    def __row_to_vo(self, fila):
        return ProjectVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
