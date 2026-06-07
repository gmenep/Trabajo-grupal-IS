from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.UsuarioVo import UsuarioVo


class UsersDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = """
        SELECT user_id, login, pass_hash, full_name, DNI, state, studies
        FROM users
        ORDER BY user_id
    """
    SQL_SELECT_BY_ID = """
        SELECT user_id, login, pass_hash, full_name, DNI, state, studies
        FROM users
        WHERE user_id = ?
    """
    SQL_SELECT_BY_LOGIN = """
        SELECT user_id, login, pass_hash, full_name, DNI, state, studies
        FROM users
        WHERE login = ?
    """
    SQL_INSERT = """
        INSERT INTO users(login, pass_hash, full_name, DNI, state, studies)
        VALUES(?, ?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE users
        SET login = ?, pass_hash = ?, full_name = ?, DNI = ?, state = ?, studies = ?
        WHERE user_id = ?
    """
    SQL_DEACTIVATE = "UPDATE users SET state = ? WHERE user_id = ?"
    SQL_DELETE = "DELETE FROM users WHERE user_id = ?"

    def select(self):
        usuarios = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            usuarios.append(self.__row_to_vo(fila))
        return usuarios

    def select_by_id(self, user_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (user_id,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def select_by_login(self, login):
        fila = self._select_one(self.SQL_SELECT_BY_LOGIN, (login,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def insert(self, usuario):
        return self._insert_id(
            self.SQL_INSERT,
            (
                usuario.login,
                usuario.pass_hash,
                usuario.full_name,
                usuario.dni,
                usuario.state,
                usuario.studies
            )
        )

    def update(self, usuario):
        return self._write(
            self.SQL_UPDATE,
            (
                usuario.login,
                usuario.pass_hash,
                usuario.full_name,
                usuario.dni,
                usuario.state,
                usuario.studies,
                usuario.user_id
            )
        )

    def deactivate(self, user_id):
        return self._write(self.SQL_DEACTIVATE, ("Baja", user_id))

    def delete(self, user_id):
        return self._write(self.SQL_DELETE, (user_id,))

    def checkLogin(self, login_vo):
        return self.select_by_login(login_vo.user)

    def __row_to_vo(self, fila):
        return UsuarioVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
