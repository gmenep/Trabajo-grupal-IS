from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.PanelEntryVo import PanelEntryVo


class PanelEntryDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = """
        SELECT pe.entry_id, pe.project_id, pe.study_id, pe.user_id, pe.title, pe.content,
               pe.created_at, p.title, COALESCE(CONCAT('Estudio ', pe.study_id), ''),
               COALESCE(u.full_name, u.login)
        FROM panel_entries pe
        INNER JOIN projects p ON p.project_id = pe.project_id
        LEFT JOIN users u ON u.user_id = pe.user_id
        ORDER BY pe.created_at DESC
    """
    SQL_SELECT_BY_ID = """
        SELECT pe.entry_id, pe.project_id, pe.study_id, pe.user_id, pe.title, pe.content,
               pe.created_at, p.title, COALESCE(CONCAT('Estudio ', pe.study_id), ''),
               COALESCE(u.full_name, u.login)
        FROM panel_entries pe
        INNER JOIN projects p ON p.project_id = pe.project_id
        LEFT JOIN users u ON u.user_id = pe.user_id
        WHERE pe.entry_id = ?
    """
    SQL_INSERT = """
        INSERT INTO panel_entries(project_id, study_id, user_id, title, content)
        VALUES(?, ?, ?, ?, ?)
    """
    SQL_UPDATE = "UPDATE panel_entries SET title = ?, content = ? WHERE entry_id = ?"
    SQL_DELETE = "DELETE FROM panel_entries WHERE entry_id = ?"

    def select(self):
        return self.__rows_to_vo(self._select(self.SQL_SELECT, ()))

    def select_by_id(self, entry_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (entry_id,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def insert(self, entry):
        return self._insert_id(
            self.SQL_INSERT,
            (entry.project_id, entry.study_id, entry.user_id, entry.title, entry.content)
        )

    def update(self, entry):
        return self._write(self.SQL_UPDATE, (entry.title, entry.content, entry.entry_id))

    def delete(self, entry_id):
        return self._write(self.SQL_DELETE, (entry_id,))

    def __rows_to_vo(self, filas):
        entradas = []
        for fila in filas:
            entradas.append(self.__row_to_vo(fila))
        return entradas

    def __row_to_vo(self, fila):
        return PanelEntryVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9])
