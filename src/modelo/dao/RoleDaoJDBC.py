from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.RoleVo import RoleVo


class RoleDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = "SELECT role_id, role_name, permisos FROM roles ORDER BY role_name"
    SQL_SELECT_BY_ID = "SELECT role_id, role_name, permisos FROM roles WHERE role_id = ?"
    SQL_SELECT_BY_NAME = "SELECT role_id, role_name, permisos FROM roles WHERE role_name = ?"
    SQL_INSERT = "INSERT INTO roles(role_name, permisos) VALUES(?, ?)"
    SQL_UPDATE = "UPDATE roles SET role_name = ?, permisos = ? WHERE role_id = ?"
    SQL_DELETE = "DELETE FROM roles WHERE role_id = ?"

    def select(self):
        roles = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            roles.append(self.__row_to_vo(fila))
        return roles

    def select_by_id(self, role_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (role_id,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def select_by_name(self, role_name):
        fila = self._select_one(self.SQL_SELECT_BY_NAME, (role_name,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def insert(self, role):
        return self._insert_id(self.SQL_INSERT, (role.role_name, role.permisos))

    def update(self, role):
        return self._write(self.SQL_UPDATE, (role.role_name, role.permisos, role.role_id))

    def delete(self, role_id):
        return self._write(self.SQL_DELETE, (role_id,))

    def insert_if_not_exists(self, role):
        existente = self.select_by_name(role.role_name)
        if existente is not None:
            return existente.role_id
        return self.insert(role)

    def __row_to_vo(self, fila):
        return RoleVo(fila[0], fila[1], fila[2])
