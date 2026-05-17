from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.StudyVo import StudyVo


class StudyDaoJDBC(Conexion):
    SQL_SELECT = "SELECT study_id, project_id FROM studies"
    SQL_SELECT_BY_ID = """
        SELECT study_id, project_id
        FROM studies
        WHERE study_id = ?
    """
    SQL_INSERT = "INSERT INTO studies(study_id, project_id) VALUES(?, ?)"
    SQL_UPDATE = "UPDATE studies SET project_id = ? WHERE study_id = ?"
    SQL_DELETE = "DELETE FROM studies WHERE study_id = ?"

    def select(self):
        cursor = None
        studies = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                studies.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Study:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return studies

    def select_by_id(self, study_id):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (study_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Study:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, study):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_INSERT, (study.study_id, study.project_id))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Study:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, study):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_UPDATE, (study.project_id, study.study_id))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Study:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, study_id):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (study_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Study:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row):
        study_id, project_id = row
        return StudyVo(study_id, project_id)

    def __commit(self):
        if self.conexion is not None:
            self.conexion.commit()
