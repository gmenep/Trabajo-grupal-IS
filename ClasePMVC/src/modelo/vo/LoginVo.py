class LoginVO:
    def __init__(self, nombre, contrasena):
        self._nombre = nombre
        self._contrasena = contrasena

    @property
    def contrasena(self):
        return self._contrasena


    @property
    def nombre(self):
        return self._nombre


