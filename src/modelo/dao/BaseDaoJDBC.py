from src.modelo.conexion.Conexion import Conexion


class BaseDaoJDBC:
    def __init__(self):
        self._conexion = Conexion()

    def _select(self, sql, valores):
        cursor = None
        filas = []
        try:
            cursor = self._conexion.getCursor()
            cursor.execute(sql, valores)
            filas = cursor.fetchall()
        except Exception as error:
            raise Exception("Error en consulta: " + str(error))
        finally:
            if cursor is not None:
                cursor.close()
        return filas

    def _select_one(self, sql, valores):
        cursor = None
        fila = None
        try:
            cursor = self._conexion.getCursor()
            cursor.execute(sql, valores)
            fila = cursor.fetchone()
        except Exception as error:
            raise Exception("Error en consulta: " + str(error))
        finally:
            if cursor is not None:
                cursor.close()
        return fila

    def _write(self, sql, valores):
        cursor = None
        rows = 0
        try:
            cursor = self._conexion.getCursor()
            cursor.execute(sql, valores)
            rows = cursor.rowcount
            self._conexion.commit()
        except Exception as error:
            self._conexion.rollback()
            raise Exception("Error en escritura: " + str(error))
        finally:
            if cursor is not None:
                cursor.close()
        return rows

    def _insert_id(self, sql, valores):
        cursor = None
        nuevo_id = None
        try:
            cursor = self._conexion.getCursor()
            cursor.execute(sql, valores)
            cursor.execute("SELECT LAST_INSERT_ID()")
            fila = cursor.fetchone()
            if fila is not None:
                nuevo_id = fila[0]
            self._conexion.commit()
        except Exception as error:
            self._conexion.rollback()
            raise Exception("Error en insercion: " + str(error))
        finally:
            if cursor is not None:
                cursor.close()
        return nuevo_id
