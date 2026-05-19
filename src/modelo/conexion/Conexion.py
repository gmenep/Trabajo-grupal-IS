import jaydebeapi

class Conexion:
    __instancia = None
    __inicializado = False

    def __new__(cls, *args, **kwargs):
        if cls.__instancia is None:
            cls.__instancia = super(Conexion, cls).__new__(cls)
        return cls.__instancia

    def __init__(self, host='localhost', database='labtrack', user='root', password='changeme'):
        if self.__inicializado:
            return

        self._host = host
        self._database = database
        self._user = user
        self._password = password
        self.conexion = self.createConnection()
        self.__inicializado = True

    def createConnection(self):
        try:
            jdbc_driver = "com.mysql.cj.jdbc.Driver"
            jar_file = "C:/Users/guill/Documents/GitHub/Trabajo-grupal-IS/lib/mysql-connector-j-9.6.0.jar"
            self.conexion = jaydebeapi.connect(
                jdbc_driver,
                f"jdbc:mysql://{self._host}/{self._database}",
                [self._user, self._password],
                jar_file
            )
            return self.conexion
        except Exception as e:
            print("Error creando conexión:", e)
            return None

    def getCursor(self):
        if self.conexion is None:
            self.createConnection()
        return self.conexion.cursor()

    def closeConnection(self):
        try:
            if self.conexion:
                self.conexion.close()
                self.conexion = None
        except Exception as e:
            print("Error cerrando conexión:", e)

