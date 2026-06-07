from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.BelongsToVo import BelongsToVo
from src.modelo.vo.UsuarioVo import UsuarioVo


class BelongsToDaoJDBC(BaseDaoJDBC):
    SQL_SELECT_BY_PROJECT = "SELECT project_id, user_id FROM belongsto WHERE project_id = ?"
    SQL_SELECT_PROJECTS_BY_USER = "SELECT project_id FROM belongsto WHERE user_id = ? ORDER BY project_id"
    SQL_SELECT_MEMBERS = """
        SELECT u.user_id, u.login, u.pass_hash, u.full_name, u.DNI, u.state, u.studies
        FROM belongsto b
        INNER JOIN users u ON u.user_id = b.user_id
        WHERE b.project_id = ?
        ORDER BY u.full_name
    """
    SQL_INSERT = "INSERT INTO belongsto(project_id, user_id) VALUES(?, ?)"
    SQL_DELETE = "DELETE FROM belongsto WHERE project_id = ? AND user_id = ?"

    def select_by_project(self, project_id):
        relaciones = []
        filas = self._select(self.SQL_SELECT_BY_PROJECT, (project_id,))
        for fila in filas:
            relaciones.append(BelongsToVo(fila[0], fila[1]))
        return relaciones

    def select_project_ids_by_user(self, user_id):
        ids = []
        filas = self._select(self.SQL_SELECT_PROJECTS_BY_USER, (user_id,))
        for fila in filas:
            ids.append(fila[0])
        return ids

    def select_members_by_project(self, project_id):
        usuarios = []
        filas = self._select(self.SQL_SELECT_MEMBERS, (project_id,))
        for fila in filas:
            usuarios.append(UsuarioVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))
        return usuarios

    def insert(self, belongs_to):
        return self._write(self.SQL_INSERT, (belongs_to.project_id, belongs_to.user_id))

    def delete(self, project_id, user_id):
        return self._write(self.SQL_DELETE, (project_id, user_id))
