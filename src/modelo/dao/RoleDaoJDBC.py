from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.RoleVo import RoleVo


class RoleDaoJDBC(Conexion):
    SQL_SELECT = "SELECT role_id, role_name, permisos FROM roles"
    SQL_SELECT_BY_ID = """
        SELECT role_id, role_name, permisos
        FROM roles
        WHERE role_id = ?
    """
    SQL_INSERT = """
        INSERT INTO roles(role_id, role_name, permisos)
        VALUES(?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE roles
        SET role_name = ?, permisos = ?
        WHERE role_id = ?
    """
    SQL_DELETE = "DELETE FROM roles WHERE role_id = ?"

    def select(self) -> list[RoleVo]:
        cursor = None
        roles = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                roles.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Role:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return roles

    def select_by_id(self, role_id: int) -> RoleVo | None:
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (role_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Role:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, role: RoleVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (role.role_id, role.role_name, role.permisos)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Role:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, role: RoleVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (role.role_name, role.permisos, role.role_id)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Role:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, role_id: int) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (role_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Role:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row) -> RoleVo:
        role_id, role_name, permisos = row
        return RoleVo(role_id, role_name, permisos)

    def __commit(self) -> None:
        if self.conexion is not None:
            self.conexion.commit()
