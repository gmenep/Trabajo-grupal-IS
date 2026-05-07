from src.modelo.conexion.Conexion import Conexion


class LoginDaoJDBC(Conexion):
    SQL_CHECK_LOGIN = "SELECT user_id, login, full_name, DNI, state, studies FROM users WHERE login = ? AND pass_hash = ?"
    

    def check_login(self, login_vo):
        cursor = None

        try:
            cursor = self.getCursor()

            cursor.execute(
                self.SQL_CHECK_LOGIN,
                (
                    login_vo.user,
                    login_vo.password
                )
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return {
                "user_id": row[0],
                "login": row[1],
                "full_name": row[2],
                "DNI": row[3],
                "state": row[4],
                "studies": row[5]
            }

        except Exception as e:
            print("Error comprobando login:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()