from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.AssetVo import AssetVo


class AssetDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = "SELECT asset_id, name, asset_type, risk_level FROM assets ORDER BY name"
    SQL_SELECT_BY_ID = "SELECT asset_id, name, asset_type, risk_level FROM assets WHERE asset_id = ?"
    SQL_SELECT_BY_NAME_TYPE = """
        SELECT asset_id, name, asset_type, risk_level
        FROM assets
        WHERE name = ? AND asset_type = ?
    """
    SQL_INSERT = "INSERT INTO assets(name, asset_type, risk_level) VALUES(?, ?, ?)"
    SQL_UPDATE = "UPDATE assets SET name = ?, asset_type = ?, risk_level = ? WHERE asset_id = ?"
    SQL_DELETE = "DELETE FROM assets WHERE asset_id = ?"

    def select(self):
        assets = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            assets.append(self.__row_to_vo(fila))
        return assets

    def select_by_id(self, asset_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (asset_id,))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def select_by_name_type(self, name, asset_type):
        fila = self._select_one(self.SQL_SELECT_BY_NAME_TYPE, (name, asset_type))
        if fila is None:
            return None
        return self.__row_to_vo(fila)

    def insert(self, asset):
        return self._insert_id(self.SQL_INSERT, (asset.name, asset.asset_type, asset.risk_level))

    def update(self, asset):
        return self._write(self.SQL_UPDATE, (asset.name, asset.asset_type, asset.risk_level, asset.asset_id))

    def delete(self, asset_id):
        return self._write(self.SQL_DELETE, (asset_id,))

    def __row_to_vo(self, fila):
        return AssetVo(fila[0], fila[1], fila[2], fila[3])
