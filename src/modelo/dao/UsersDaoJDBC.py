from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UsuarioVo import UsuarioVo


class UsersDaoJDBC(Conexion):
    SQL_SELECT = """
        SELECT user_id, login, pass_hash, full_name, DNI, state, studies
        FROM users
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
        INSERT INTO users(user_id, login, pass_hash, full_name, DNI, state, studies)
        VALUES(?, ?, ?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE users
        SET login = ?, pass_hash = ?, full_name = ?, DNI = ?, state = ?, studies = ?
        WHERE user_id = ?
    """
    SQL_DELETE = "DELETE FROM users WHERE user_id = ?"

    def select(self):
        cursor = None
        usuarios = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                usuarios.append(self.__map_row(row))

        except Exception as e:
            print("Error al seleccionar usuarios:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return usuarios

    def select_by_id(self, user_id):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (user_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error al seleccionar usuario por id:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

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
            print("Error al seleccionar usuario por login:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, usuario):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (
                    usuario.user_id,
                    usuario.login,
                    usuario.pass_hash,
                    usuario.full_name,
                    usuario.dni,
                    usuario.state,
                    usuario.studies
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error al insertar usuario:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, usuario):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
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
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error al actualizar usuario:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, user_id):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (user_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error al eliminar usuario:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def checkLogin(self, login_vo):
        return self.select_by_login(login_vo.user)

    def __map_row(self, row):
        user_id, login, pass_hash, full_name, dni, state, studies = row
        return UsuarioVo(user_id, login, pass_hash, full_name, dni, state, studies)

    def __commit(self):
        if self.conexion is not None:
            self.conexion.commit()
