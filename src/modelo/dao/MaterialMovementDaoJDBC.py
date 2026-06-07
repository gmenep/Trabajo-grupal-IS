from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.MaterialMovementVo import MaterialMovementVo


class MaterialMovementDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = """
        SELECT movement_id, material_id, storage_id, batch_number, user_id, quantity, movement_type, movement_date, notes
        FROM material_movements
        ORDER BY movement_date DESC
    """
    SQL_INSERT = """
        INSERT INTO material_movements(material_id, storage_id, batch_number, user_id, quantity, movement_type, notes)
        VALUES(?, ?, ?, ?, ?, ?, ?)
    """
    SQL_USAGE = """
        SELECT a.name, COALESCE(SUM(mm.quantity), 0)
        FROM material_movements mm
        INNER JOIN assets a ON a.asset_id = mm.material_id
        WHERE mm.movement_type IN ('SALIDA', 'SOLICITUD')
        GROUP BY a.name
        ORDER BY a.name
    """

    def select(self):
        movimientos = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            movimientos.append(MaterialMovementVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8]))
        return movimientos

    def insert(self, movement):
        return self._insert_id(
            self.SQL_INSERT,
            (
                movement.material_id,
                movement.storage_id,
                movement.batch_number,
                movement.user_id,
                movement.quantity,
                movement.movement_type,
                movement.notes
            )
        )

    def select_usage(self):
        return self._select(self.SQL_USAGE, ())
