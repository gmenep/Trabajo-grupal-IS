from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UserVO import UserVO
from src.modelo.dao.UserDao import UserDao

class UserDaoJDBC(UserDao, Conexion): #También puede abrir solo una conexion cuando se inicia la app
    SQL_SELECT = "SELECT DNI, nombre, primer_apellido, segundo_apellido, email FROM Usuarios"
    SQL_INSERT = "INSERT INTO Usuarios(DNI, nombre, primer_apellido, segundo_apellido, email) VALUES(?, ?, ?, ?, ?)"
    SQL_CHECK_LOGIN = "SELECT DNI, nombre, primer_apellido, segundo_apellido, email FROM Usuarios WHERE nombre = ? AND Contraseña = ?"

    def checkLogin(self, loginVO):
        cursor = self.getCursor()
        try:
            cursor.execute(self.SQL_CHECK_LOGIN, (loginVO.nombre, loginVO.contrasena))
            row = cursor.fetchone()

            if row:
                idUser, nombre, apellido1, apellido2, email = row
                usuario = UserVO(idUser, nombre, apellido1, apellido2, email)
                return usuario
            else:
                return None

        except Exception as e:
            print(e)

    def select(self) -> list[UserVO]:
        cursor = self.getCursor()
        usuarios = []

        try:
            cursor.execute(self.SQL_SELECT) #Lanza una instrucción SQL.
            rows = cursor.fetchall() #Recupera todas las filas devueltas por esa instrucción.

            for row in rows:
                idUser, nombre, apellido1, apellido2, email = row
                usuario = UserVO(idUser, nombre, apellido1, apellido2, email)
                usuarios.append(usuario)

        except Exception as e:
            print("Error al seleccionar usuarios:", e)

        finally:
            if cursor:
                cursor.close()
            self.closeConnection()


        return usuarios

    def insert(self, usuario: UserVO) -> int:
        cursor = self.getCursor()
        rows = 0

        try:
            cursor.execute(
                self.SQL_INSERT,
                (usuario._idUser, usuario._nombre, usuario._apellido1, usuario._apellido2, usuario._email)
            )
            rows = cursor.rowcount

        except Exception as e:
            print("Error al insertar usuario:", e)

        finally:
            if cursor:
                cursor.close()
            self.closeConnection()

        return rows