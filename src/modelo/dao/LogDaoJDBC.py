from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.LogVo import LogVo


class LogDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = """
        SELECT log_id, timestamp, event_type, reference_id, raw_data, user_id
        FROM logs
        ORDER BY timestamp DESC
    """
    SQL_INSERT = """
        INSERT INTO logs(event_type, reference_id, raw_data, user_id)
        VALUES(?, ?, ?, ?)
    """
    SQL_EVENT_TYPES = "SELECT DISTINCT event_type FROM logs WHERE event_type IS NOT NULL ORDER BY event_type"

    def select(self):
        return self.__rows_to_vo(self._select(self.SQL_SELECT, ()))

    def select_filtrado(self, user_id, event_type, fecha):
        sql = """
            SELECT log_id, timestamp, event_type, reference_id, raw_data, user_id
            FROM logs
            WHERE 1 = 1
        """
        valores = []
        if user_id is not None:
            sql = sql + " AND user_id = ?"
            valores.append(user_id)
        if event_type is not None and event_type != "":
            sql = sql + " AND event_type = ?"
            valores.append(event_type)
        if fecha is not None and fecha != "":
            sql = sql + " AND DATE(timestamp) = ?"
            valores.append(fecha)
        sql = sql + " ORDER BY timestamp DESC"
        return self.__rows_to_vo(self._select(sql, tuple(valores)))

    def insert(self, log):
        return self._insert_id(
            self.SQL_INSERT,
            (log.event_type, log.reference_id, log.raw_data, log.user_id)
        )

    def select_event_types(self):
        tipos = []
        filas = self._select(self.SQL_EVENT_TYPES, ())
        for fila in filas:
            tipos.append(fila[0])
        return tipos

    def logs_by_type(self):
        return self._select("SELECT event_type, COUNT(*) FROM logs GROUP BY event_type ORDER BY event_type", ())

    def __rows_to_vo(self, filas):
        logs = []
        for fila in filas:
            logs.append(LogVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
        return logs
