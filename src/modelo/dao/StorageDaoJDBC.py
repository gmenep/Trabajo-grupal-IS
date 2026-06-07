from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.StorageVo import StorageVo


class StorageDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = "SELECT storage_id, name, specifications FROM storage ORDER BY name"
    SQL_SELECT_BY_ID = "SELECT storage_id, name, specifications FROM storage WHERE storage_id = ?"
    SQL_SELECT_BY_NAME = "SELECT storage_id, name, specifications FROM storage WHERE name = ?"
    SQL_INSERT = "INSERT INTO storage(name, specifications) VALUES(?, ?)"
    SQL_UPDATE = "UPDATE storage SET name = ?, specifications = ? WHERE storage_id = ?"
    SQL_DELETE = "DELETE FROM storage WHERE storage_id = ?"

    def select(self):
        almacenes = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            almacenes.append(self.__row_to_vo(fila))
        return almacenes

    def select_by_id(self, storage_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (storage_id,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def select_by_name(self, name):
        fila = self._select_one(self.SQL_SELECT_BY_NAME, (name,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def insert(self, storage):
        return self._insert_id(self.SQL_INSERT, (storage.name, storage.specifications))

    def update(self, storage):
        return self._write(self.SQL_UPDATE, (storage.name, storage.specifications, storage.storage_id))

    def delete(self, storage_id):
        return self._write(self.SQL_DELETE, (storage_id,))

    def insert_if_not_exists(self, storage):
        existente = self.select_by_name(storage.name)
        if existente is not None:
            return existente.storage_id
        return self.insert(storage)

    def __row_to_vo(self, fila):
        return StorageVo(fila[0], fila[1], fila[2])
