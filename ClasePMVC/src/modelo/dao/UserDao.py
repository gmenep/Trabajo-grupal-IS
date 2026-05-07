from src.modelo.vo.UserVO import UserVO

class UserDao:
    def select(self) -> list[UserVO]:
        """
        Recupera todos los usuarios de la base de datos.
        
        Returns:
            list[UserVO]: Una lista de objetos UserVO.
        
        Raises:
            SQLException: Si hay un error al ejecutar la consulta.
            Exception: Para otros errores inesperados.
        """
        raise NotImplementedError("Método select() no implementado")

    def insert(self, usuarios: UserVO) -> int:
        """
        Inserta un nuevo usuario en la base de datos.

        Args:
            user (UserVO): El objeto UserVO a insertar.

        Returns:
            int: El ID del usuario insertado.

        Raises:
            SQLException: Si hay un error al ejecutar la inserción.
        """
        raise NotImplementedError("Método insert() no implementado")