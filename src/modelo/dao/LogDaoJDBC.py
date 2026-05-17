from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.LogVo import LogVo


class LogDaoJDBC(Conexion):
    SQL_SELECT = """
        SELECT log_id, timestamp, event_type, reference_id, raw_data, user_id
        FROM logs
    """
    SQL_SELECT_BY_ID = """
        SELECT log_id, timestamp, event_type, reference_id, raw_data, user_id
        FROM logs
        WHERE log_id = ?
    """
    SQL_INSERT = """
        INSERT INTO logs(log_id, timestamp, event_type, reference_id, raw_data, user_id)
        VALUES(?, ?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE logs
        SET timestamp = ?, event_type = ?, reference_id = ?, raw_data = ?, user_id = ?
        WHERE log_id = ?
    """
    SQL_DELETE = "DELETE FROM logs WHERE log_id = ?"

    def select(self):
        cursor = None
        logs = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                logs.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Log:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return logs

    def select_by_id(self, log_id):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (log_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Log:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, log):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (
                    log.log_id,
                    log.timestamp,
                    log.event_type,
                    log.reference_id,
                    log.raw_data,
                    log.user_id
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Log:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, log):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (
                    log.timestamp,
                    log.event_type,
                    log.reference_id,
                    log.raw_data,
                    log.user_id,
                    log.log_id
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Log:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, log_id):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (log_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Log:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row):
        log_id, timestamp, event_type, reference_id, raw_data, user_id = row
        return LogVo(log_id, timestamp, event_type, reference_id, raw_data, user_id)

    def __commit(self):
        if self.conexion is not None:
            self.conexion.commit()
