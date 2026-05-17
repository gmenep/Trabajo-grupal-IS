from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.ProjectVo import ProjectVo


class ProjectDaoJDBC(Conexion):
    SQL_SELECT = """
        SELECT project_id, title, description, start_date, end_date, state
        FROM projects
    """
    SQL_SELECT_BY_ID = """
        SELECT project_id, title, description, start_date, end_date, state
        FROM projects
        WHERE project_id = ?
    """
    SQL_INSERT = """
        INSERT INTO projects(project_id, title, description, start_date, end_date, state)
        VALUES(?, ?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE projects
        SET title = ?, description = ?, start_date = ?, end_date = ?, state = ?
        WHERE project_id = ?
    """
    SQL_DELETE = "DELETE FROM projects WHERE project_id = ?"

    def select(self):
        cursor = None
        projects = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                projects.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Project:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return projects

    def select_by_id(self, project_id):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (project_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Project:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, project):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (
                    project.project_id,
                    project.title,
                    project.description,
                    project.start_date,
                    project.end_date,
                    project.state
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Project:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, project):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (
                    project.title,
                    project.description,
                    project.start_date,
                    project.end_date,
                    project.state,
                    project.project_id
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Project:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, project_id):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (project_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Project:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row):
        project_id, title, description, start_date, end_date, state = row
        return ProjectVo(project_id, title, description, start_date, end_date, state)

    def __commit(self):
        if self.conexion is not None:
            self.conexion.commit()
