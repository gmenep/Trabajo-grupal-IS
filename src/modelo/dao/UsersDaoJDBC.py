from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UsuarioVo import UsuarioVo
class UsersDaoJDBC(Conexion):
    SQL_SELECT = "SELECT user_id, login, pass_hash, full_name, DNI, state, studies FROM users"
    SQL_INSERT = "INSERT INTO users(todo lo que se inserta)"
    SQL_CHECK_LOGIN = "SELECT user_id, login, pass_hash, full_name, DNI, state, studies FROM users WHERE full_name = ? AND pass_hash = ?"
    
    def checkLogin(self, loginVO):
        cursor = self.getCursor()
        try:
            row = cursor.execute(self.SQL_CHECK_LOGIN, (loginVO.full_name, loginVO.pass_hash))
            if row:
                user_id, login, pass_hash, full_name, DNI, state, studies = row
                Usuario = UsuarioVo(user_id, login, pass_hash, full_name, DNI, state, studies)
                return Usuario
            else:
                return None
        except Exception as e:
            print(e)

    def select(self):
        cursor = self.getCursor()
        usuarios = []

        try:
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                user_id, login, pass_hash, full_name, DNI, state, studies = row

                user = UsuarioVo(
                    user_id,
                    login,
                    pass_hash,
                    full_name,
                    DNI,
                    state,
                    studies
                )

                usuarios.append(user)
                print(user_id, login, full_name)

        except Exception as e:
            print(e)

        return usuarios

if __name__ == "__main__":
    print("Probando la conexión...")
    dao = UsersDaoJDBC()
    lista_usuarios = dao.select()
    print("Fin de la prueba.")