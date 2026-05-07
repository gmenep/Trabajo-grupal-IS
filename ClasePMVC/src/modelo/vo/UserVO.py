class UserVO:
    def __init__(self, iduser, nombre, apellido1, apellido2, email):
        self._idUser = iduser
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._email = email

    @property
    def id_user(self):
        return self._idUser

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido1(self):
        return self._apellido1

    @property
    def apellido2(self):
        return self._apellido2

    @property
    def email(self):
        return self._email
