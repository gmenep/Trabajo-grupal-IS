from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UserRoleVo import UserRoleVo


class UserRoleDaoJDBC(Conexion):
    SQL_SELECT = "SELECT user_id, role_id FROM userrole"
    SQL_SELECT_BY_ID = """
        SELECT user_id, role_id
        FROM userrole
        WHERE user_id = ? AND role_id = ?
    """
    SQL_INSERT = "INSERT INTO userrole(user_id, role_id) VALUES(?, ?)"
    SQL_DELETE = "DELETE FROM userrole WHERE user_id = ? AND role_id = ?"

    def select(self):
        cursor = None
        user_roles = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                user_roles.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de UserRole:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return user_roles

    # Clave primaria compuesta: user_id, role_id.
    def select_by_id(self, user_id, role_id):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (user_id, role_id))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de UserRole:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, user_role):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (user_role.user_id, user_role.role_id)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de UserRole:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, user_id, role_id):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (user_id, role_id))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de UserRole:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row):
        user_id, role_id = row
        return UserRoleVo(user_id, role_id)

    def __commit(self):
        if self.conexion is not None:
            self.conexion.commit()
