import os
from pathlib import Path

import jaydebeapi


class Conexion:
    __instancia = None
    __inicializada = False

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = object.__new__(cls)
        return cls.__instancia

    def __init__(self):
        if self.__inicializada:
            return

        self.__host = os.getenv("LABTRACK_DB_HOST", "localhost")
        self.__database = os.getenv("LABTRACK_DB_NAME", "labtrack")
        self.__user = os.getenv("LABTRACK_DB_USER", "root")
        self.__password = os.getenv("LABTRACK_DB_PASSWORD", "changeme")
        self.conexion = None
        self.__inicializada = True

    def createConnection(self):
        if self.conexion is not None:
            return self.conexion

        jdbc_driver = "com.mysql.cj.jdbc.Driver"
        ruta_proyecto = Path(__file__).resolve().parents[3]
        jar_file = ruta_proyecto / "lib" / "mysql-connector-j-9.6.0.jar"
        jdbc_url = (
            "jdbc:mysql://"
            + self.__host
            + ":3306/"
            + self.__database
            + "?serverTimezone=UTC&useSSL=false&allowPublicKeyRetrieval=true"
        )

        try:
            self.conexion = jaydebeapi.connect(
                jdbc_driver,
                jdbc_url,
                [self.__user, self.__password],
                str(jar_file)
            )
            try:
                self.conexion.jconn.setAutoCommit(False)
            except Exception:
                pass
            return self.conexion
        except Exception as error:
            print("Error creando conexion:", error)
            self.conexion = None
            return None

    def getCursor(self):
        if self.conexion is None:
            self.createConnection()

        if self.conexion is None:
            raise Exception("No se pudo crear la conexion con la base de datos")

        return self.conexion.cursor()

    def commit(self):
        if self.conexion is not None:
            self.conexion.commit()

    def rollback(self):
        if self.conexion is not None:
            self.conexion.rollback()

    def closeConnection(self):
        try:
            if self.conexion is not None:
                self.conexion.close()
        except Exception as error:
            print("Error cerrando conexion:", error)
        finally:
            self.conexion = None
