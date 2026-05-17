from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.BelongsToVo import BelongsToVo


class BelongsToDaoJDBC(Conexion):
    SQL_SELECT = "SELECT project_id, user_id FROM belongsto"
    SQL_SELECT_BY_ID = """
        SELECT project_id, user_id
        FROM belongsto
        WHERE project_id = ? AND user_id = ?
    """
    SQL_INSERT = "INSERT INTO belongsto(project_id, user_id) VALUES(?, ?)"
    SQL_DELETE = "DELETE FROM belongsto WHERE project_id = ? AND user_id = ?"

    def select(self):
        cursor = None
        belongsto_items = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                belongsto_items.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de BelongsTo:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return belongsto_items

    # Clave primaria compuesta: project_id, user_id.
    def select_by_id(self, project_id, user_id):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (project_id, user_id))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de BelongsTo:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, belongsto):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (belongsto.project_id, belongsto.user_id)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de BelongsTo:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, project_id, user_id):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (project_id, user_id))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de BelongsTo:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row):
        project_id, user_id = row
        return BelongsToVo(project_id, user_id)

    def __commit(self):
        if self.conexion is not None:
            self.conexion.commit()
