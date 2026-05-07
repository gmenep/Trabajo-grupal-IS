from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.UserDaoJDBC import UserDaoJDBC
from src.modelo.vo.UserVO import UserVO

class Logica():

    def pruebainsert(self):
        user_dao = UserDaoJDBC()
        usuario1 = UserVO(4, "nom", "ap1", "ap2", "l@gmail.com")
        filas = user_dao.insert(usuario1)

    def pruebaselect(self):
        user_dao = UserDaoJDBC()
        usuarios = user_dao.select()
        # Mostrar los usuarios recuperados
        for usuario in usuarios:
            print(usuario)
            print(usuario.nombre)

    def hacerLogin(self, loginVO):
        login_dao = UserDaoJDBC()
        resultado = login_dao.checkLogin(loginVO)

        return resultado