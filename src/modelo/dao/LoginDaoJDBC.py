from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UsuarioVo import UsuarioVo


class LoginDaoJDBC(Conexion):
    SQL_SELECT_BY_LOGIN = """
        SELECT user_id, login, pass_hash, full_name, DNI, state, studies
        FROM users
        WHERE login = ?
    """

    def check_login(self, login_vo):
        return self.select_by_login(login_vo.user)

    def select_by_login(self, login):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_LOGIN, (login,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error seleccionando login:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def __map_row(self, row):
        user_id, login, pass_hash, full_name, dni, state, studies = row
        return UsuarioVo(user_id, login, pass_hash, full_name, dni, state, studies)
