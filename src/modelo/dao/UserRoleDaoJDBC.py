from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.UserRoleVo import UserRoleVo


class UserRoleDaoJDBC(BaseDaoJDBC):
    SQL_SELECT_BY_USER = "SELECT user_id, role_id FROM userrole WHERE user_id = ?"
    SQL_SELECT_ROLE_NAMES = """
        SELECT r.role_name
        FROM userrole ur
        INNER JOIN roles r ON r.role_id = ur.role_id
        WHERE ur.user_id = ?
        ORDER BY r.role_name
    """
    SQL_INSERT = "INSERT INTO userrole(user_id, role_id) VALUES(?, ?)"
    SQL_DELETE = "DELETE FROM userrole WHERE user_id = ? AND role_id = ?"
    SQL_DELETE_BY_USER = "DELETE FROM userrole WHERE user_id = ?"

    def select_by_user(self, user_id):
        relaciones = []
        filas = self._select(self.SQL_SELECT_BY_USER, (user_id,))
        for fila in filas:
            relaciones.append(UserRoleVo(fila[0], fila[1]))
        return relaciones

    def select_role_names_by_user(self, user_id):
        nombres = []
        filas = self._select(self.SQL_SELECT_ROLE_NAMES, (user_id,))
        for fila in filas:
            nombres.append(fila[0])
        return nombres

    def insert(self, user_role):
        return self._write(self.SQL_INSERT, (user_role.user_id, user_role.role_id))

    def delete(self, user_id, role_id):
        return self._write(self.SQL_DELETE, (user_id, role_id))

    def delete_by_user(self, user_id):
        return self._write(self.SQL_DELETE_BY_USER, (user_id,))
