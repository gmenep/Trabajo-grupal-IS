from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.StorageVo import StorageVo


class StorageDaoJDBC(Conexion):
    SQL_SELECT = "SELECT storage_id, name, specifications FROM storage"
    SQL_SELECT_BY_ID = """
        SELECT storage_id, name, specifications
        FROM storage
        WHERE storage_id = ?
    """
    SQL_INSERT = """
        INSERT INTO storage(storage_id, name, specifications)
        VALUES(?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE storage
        SET name = ?, specifications = ?
        WHERE storage_id = ?
    """
    SQL_DELETE = "DELETE FROM storage WHERE storage_id = ?"

    def select(self) -> list[StorageVo]:
        cursor = None
        storage_items = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                storage_items.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Storage:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return storage_items

    def select_by_id(self, storage_id: int) -> StorageVo | None:
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (storage_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Storage:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, storage: StorageVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (storage.storage_id, storage.name, storage.specifications)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Storage:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, storage: StorageVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (storage.name, storage.specifications, storage.storage_id)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Storage:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, storage_id: int) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (storage_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Storage:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row) -> StorageVo:
        storage_id, name, specifications = row
        return StorageVo(storage_id, name, specifications)

    def __commit(self) -> None:
        if self.conexion is not None:
            self.conexion.commit()
