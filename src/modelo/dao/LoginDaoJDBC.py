from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.UsuarioVo import UsuarioVo


class LoginDaoJDBC(BaseDaoJDBC):
    SQL_SELECT_BY_LOGIN = """
        SELECT user_id, login, pass_hash, full_name, DNI, state, studies
        FROM users
        WHERE login = ?
    """

    def select_by_login(self, login):
        fila = self._select_one(self.SQL_SELECT_BY_LOGIN, (login,))
        if fila is None:
            return None
        return UsuarioVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
