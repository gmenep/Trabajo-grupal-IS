from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.StoredInVo import StoredInVo


class StoredInDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = """
        SELECT material_id, storage_id, quantity, batch_number, exp_date
        FROM storedin
        ORDER BY material_id, storage_id, batch_number
    """
    SQL_SELECT_ONE = """
        SELECT material_id, storage_id, quantity, batch_number, exp_date
        FROM storedin
        WHERE material_id = ? AND storage_id = ? AND batch_number = ?
    """
    SQL_SELECT_BY_MATERIAL = """
        SELECT material_id, storage_id, quantity, batch_number, exp_date
        FROM storedin
        WHERE material_id = ? AND quantity > 0
        ORDER BY exp_date IS NULL, exp_date, storage_id, batch_number
    """
    SQL_INSERT = """
        INSERT INTO storedin(material_id, storage_id, quantity, batch_number, exp_date)
        VALUES(?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE storedin
        SET quantity = ?, exp_date = ?
        WHERE material_id = ? AND storage_id = ? AND batch_number = ?
    """
    SQL_UPDATE_QUANTITY = """
        UPDATE storedin
        SET quantity = ?
        WHERE material_id = ? AND storage_id = ? AND batch_number = ?
    """
    SQL_DELETE = "DELETE FROM storedin WHERE material_id = ? AND storage_id = ? AND batch_number = ?"
    SQL_DELETE_MATERIAL = "DELETE FROM storedin WHERE material_id = ?"
    SQL_TOTAL = "SELECT COALESCE(SUM(quantity), 0) FROM storedin WHERE material_id = ?"

    def select(self):
        return self.__rows_to_vo(self._select(self.SQL_SELECT, ()))

    def select_one(self, material_id, storage_id, batch_number):
        fila = self._select_one(self.SQL_SELECT_ONE, (material_id, storage_id, batch_number))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def select_by_material(self, material_id):
        return self.__rows_to_vo(self._select(self.SQL_SELECT_BY_MATERIAL, (material_id,)))

    def insert(self, stored_in):
        return self._write(
            self.SQL_INSERT,
            (stored_in.material_id, stored_in.storage_id, stored_in.quantity, stored_in.batch_number, stored_in.exp_date)
        )

    def update(self, stored_in):
        return self._write(
            self.SQL_UPDATE,
            (stored_in.quantity, stored_in.exp_date, stored_in.material_id, stored_in.storage_id, stored_in.batch_number)
        )

    def update_quantity(self, material_id, storage_id, batch_number, quantity):
        return self._write(self.SQL_UPDATE_QUANTITY, (quantity, material_id, storage_id, batch_number))

    def delete(self, material_id, storage_id, batch_number):
        return self._write(self.SQL_DELETE, (material_id, storage_id, batch_number))

    def delete_by_material(self, material_id):
        return self._write(self.SQL_DELETE_MATERIAL, (material_id,))

    def total_by_material(self, material_id):
        fila = self._select_one(self.SQL_TOTAL, (material_id,))
        if fila is None:
            return 0
        return fila[0]

    def __rows_to_vo(self, filas):
        datos = []
        for fila in filas:
            datos.append(self.__row_to_vo(fila))
        return datos

    def __row_to_vo(self, fila):
        return StoredInVo(fila[0], fila[1], fila[2], fila[3], fila[4])
