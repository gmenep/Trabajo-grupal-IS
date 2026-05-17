from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.StoredInVo import StoredInVo


class StoredInDaoJDBC(Conexion):
    SQL_SELECT = """
        SELECT material_id, storage_id, quantity, batch_number, exp_date
        FROM storedin
    """
    SQL_SELECT_BY_ID = """
        SELECT material_id, storage_id, quantity, batch_number, exp_date
        FROM storedin
        WHERE material_id = ? AND storage_id = ? AND batch_number = ?
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
    SQL_DELETE = """
        DELETE FROM storedin
        WHERE material_id = ? AND storage_id = ? AND batch_number = ?
    """

    def select(self) -> list[StoredInVo]:
        cursor = None
        stored_items = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                stored_items.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de StoredIn:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return stored_items

    # Clave primaria compuesta: material_id, storage_id, batch_number.
    def select_by_id(
        self,
        material_id: int,
        storage_id: int,
        batch_number: str
    ) -> StoredInVo | None:
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_SELECT_BY_ID,
                (material_id, storage_id, batch_number)
            )
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de StoredIn:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, stored_in: StoredInVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (
                    stored_in.material_id,
                    stored_in.storage_id,
                    stored_in.quantity,
                    stored_in.batch_number,
                    stored_in.exp_date
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de StoredIn:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, stored_in: StoredInVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (
                    stored_in.quantity,
                    stored_in.exp_date,
                    stored_in.material_id,
                    stored_in.storage_id,
                    stored_in.batch_number
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de StoredIn:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, material_id: int, storage_id: int, batch_number: str) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (material_id, storage_id, batch_number))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de StoredIn:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row) -> StoredInVo:
        material_id, storage_id, quantity, batch_number, exp_date = row
        return StoredInVo(material_id, storage_id, quantity, batch_number, exp_date)

    def __commit(self) -> None:
        if self.conexion is not None:
            self.conexion.commit()
