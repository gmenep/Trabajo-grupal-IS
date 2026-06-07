from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.MaterialInventarioVo import MaterialInventarioVo
from src.modelo.vo.MaterialVo import MaterialVo


class MaterialDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = "SELECT material_id, specifications, formula, measure_unit FROM materials ORDER BY material_id"
    SQL_SELECT_BY_ID = "SELECT material_id, specifications, formula, measure_unit FROM materials WHERE material_id = ?"
    SQL_INSERT = "INSERT INTO materials(material_id, specifications, formula, measure_unit) VALUES(?, ?, ?, ?)"
    SQL_UPDATE = """
        UPDATE materials
        SET specifications = ?, formula = ?, measure_unit = ?
        WHERE material_id = ?
    """
    SQL_DELETE = "DELETE FROM materials WHERE material_id = ?"
    SQL_INVENTARIO = """
        SELECT m.material_id, a.name, a.risk_level, m.specifications, m.formula, m.measure_unit,
               s.storage_id, s.name, si.batch_number, si.quantity, si.exp_date
        FROM materials m
        INNER JOIN assets a ON a.asset_id = m.material_id
        LEFT JOIN storedin si ON si.material_id = m.material_id
        LEFT JOIN storage s ON s.storage_id = si.storage_id
        WHERE (? = '' OR a.name LIKE ?)
          AND (? = 0 OR s.storage_id = ?)
        ORDER BY a.name, si.exp_date, si.batch_number
    """
    SQL_AGRUPADO = """
        SELECT m.material_id, a.name, a.risk_level, m.specifications, m.formula, m.measure_unit,
               NULL, 'Todos', '', COALESCE(SUM(si.quantity), 0), NULL
        FROM materials m
        INNER JOIN assets a ON a.asset_id = m.material_id
        LEFT JOIN storedin si ON si.material_id = m.material_id
        GROUP BY m.material_id, a.name, a.risk_level, m.specifications, m.formula, m.measure_unit
        ORDER BY a.name
    """
    SQL_TOTAL = "SELECT COUNT(*) FROM materials"
    SQL_STOCK_BAJO = """
        SELECT m.material_id, a.name, a.risk_level, m.specifications, m.formula, m.measure_unit,
               s.storage_id, s.name, si.batch_number, si.quantity, si.exp_date
        FROM storedin si
        INNER JOIN materials m ON m.material_id = si.material_id
        INNER JOIN assets a ON a.asset_id = m.material_id
        INNER JOIN storage s ON s.storage_id = si.storage_id
        WHERE si.quantity <= 5
        ORDER BY si.quantity
    """
    SQL_CADUCIDAD = """
        SELECT m.material_id, a.name, a.risk_level, m.specifications, m.formula, m.measure_unit,
               s.storage_id, s.name, si.batch_number, si.quantity, si.exp_date
        FROM storedin si
        INNER JOIN materials m ON m.material_id = si.material_id
        INNER JOIN assets a ON a.asset_id = m.material_id
        INNER JOIN storage s ON s.storage_id = si.storage_id
        WHERE si.exp_date IS NOT NULL AND si.exp_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
        ORDER BY si.exp_date
    """
    SQL_POR_ALMACEN = """
        SELECT s.name, COUNT(DISTINCT si.material_id), COALESCE(SUM(si.quantity), 0)
        FROM storage s
        LEFT JOIN storedin si ON si.storage_id = s.storage_id
        GROUP BY s.storage_id, s.name
        ORDER BY s.name
    """

    def select(self):
        materiales = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            materiales.append(MaterialVo(fila[0], fila[1], fila[2], fila[3]))
        return materiales

    def select_by_id(self, material_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (material_id,))
        if fila is None:
            return None
        return MaterialVo(fila[0], fila[1], fila[2], fila[3])

    def insert(self, material):
        return self._write(
            self.SQL_INSERT,
            (material.material_id, material.specifications, material.formula, material.measure_unit)
        )

    def update(self, material):
        return self._write(
            self.SQL_UPDATE,
            (material.specifications, material.formula, material.measure_unit, material.material_id)
        )

    def delete(self, material_id):
        return self._write(self.SQL_DELETE, (material_id,))

    def select_inventario(self, nombre, storage_id):
        texto = ""
        patron = "%"
        if nombre is not None and nombre.strip() != "":
            texto = nombre.strip()
            patron = "%" + texto + "%"
        almacen = 0
        if storage_id is not None:
            almacen = storage_id
        filas = self._select(self.SQL_INVENTARIO, (texto, patron, almacen, almacen))
        return self.__rows_to_inventario(filas)

    def select_agrupado(self):
        filas = self._select(self.SQL_AGRUPADO, ())
        return self.__rows_to_inventario(filas)

    def count(self):
        fila = self._select_one(self.SQL_TOTAL, ())
        if fila is None:
            return 0
        return fila[0]

    def select_stock_bajo(self):
        return self.__rows_to_inventario(self._select(self.SQL_STOCK_BAJO, ()))

    def select_proximos_caducar(self):
        return self.__rows_to_inventario(self._select(self.SQL_CADUCIDAD, ()))

    def select_por_almacen(self):
        return self._select(self.SQL_POR_ALMACEN, ())

    def __rows_to_inventario(self, filas):
        datos = []
        for fila in filas:
            datos.append(MaterialInventarioVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10]))
        return datos
