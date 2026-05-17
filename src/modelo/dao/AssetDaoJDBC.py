from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.AssetVo import AssetVo


class AssetDaoJDBC(Conexion):
    SQL_SELECT = "SELECT asset_id, name, asset_type, risk_level FROM assets"
    SQL_SELECT_BY_ID = """
        SELECT asset_id, name, asset_type, risk_level
        FROM assets
        WHERE asset_id = ?
    """
    SQL_INSERT = """
        INSERT INTO assets(asset_id, name, asset_type, risk_level)
        VALUES(?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE assets
        SET name = ?, asset_type = ?, risk_level = ?
        WHERE asset_id = ?
    """
    SQL_DELETE = "DELETE FROM assets WHERE asset_id = ?"

    def select(self):
        cursor = None
        assets = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                assets.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Asset:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return assets

    def select_by_id(self, asset_id):
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (asset_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Asset:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, asset):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (asset.asset_id, asset.name, asset.asset_type, asset.risk_level)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Asset:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, asset):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (asset.name, asset.asset_type, asset.risk_level, asset.asset_id)
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Asset:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, asset_id):
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (asset_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Asset:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row):
        asset_id, name, asset_type, risk_level = row
        return AssetVo(asset_id, name, asset_type, risk_level)

    def __commit(self):
        if self.conexion is not None:
            self.conexion.commit()
