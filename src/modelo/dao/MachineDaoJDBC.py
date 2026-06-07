from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.MachineInventarioVo import MachineInventarioVo
from src.modelo.vo.MachineVo import MachineVo


class MachineDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = """
        SELECT machine_id, state, last_revision_date, next_revision_date, description
        FROM machines
        ORDER BY machine_id
    """
    SQL_SELECT_BY_ID = """
        SELECT machine_id, state, last_revision_date, next_revision_date, description
        FROM machines
        WHERE machine_id = ?
    """
    SQL_INSERT = """
        INSERT INTO machines(machine_id, state, last_revision_date, next_revision_date, description)
        VALUES(?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE machines
        SET state = ?, last_revision_date = ?, next_revision_date = ?, description = ?
        WHERE machine_id = ?
    """
    SQL_UPDATE_STATE = "UPDATE machines SET state = ? WHERE machine_id = ?"
    SQL_DELETE = "DELETE FROM machines WHERE machine_id = ?"
    SQL_INVENTARIO = """
        SELECT m.machine_id, a.name, a.risk_level, m.state, m.last_revision_date,
               m.next_revision_date, m.description, s.storage_id, s.name
        FROM machines m
        INNER JOIN assets a ON a.asset_id = m.machine_id
        LEFT JOIN machine_location ml ON ml.machine_id = m.machine_id
        LEFT JOIN storage s ON s.storage_id = ml.storage_id
        WHERE (? = '' OR a.name LIKE ?)
          AND (? = '' OR m.state = ? OR s.name = ?)
        ORDER BY a.name
    """
    SQL_DISPONIBLES = """
        SELECT m.machine_id, a.name, a.risk_level, m.state, m.last_revision_date,
               m.next_revision_date, m.description, s.storage_id, s.name
        FROM machines m
        INNER JOIN assets a ON a.asset_id = m.machine_id
        LEFT JOIN machine_location ml ON ml.machine_id = m.machine_id
        LEFT JOIN storage s ON s.storage_id = ml.storage_id
        WHERE m.state = 'Operativa'
        ORDER BY a.name
    """
    SQL_TOTAL = "SELECT COUNT(*) FROM machines"
    SQL_BY_STATE = "SELECT state, COUNT(*) FROM machines GROUP BY state ORDER BY state"
    SQL_REVISION = """
        SELECT m.machine_id, a.name, a.risk_level, m.state, m.last_revision_date,
               m.next_revision_date, m.description, s.storage_id, s.name
        FROM machines m
        INNER JOIN assets a ON a.asset_id = m.machine_id
        LEFT JOIN machine_location ml ON ml.machine_id = m.machine_id
        LEFT JOIN storage s ON s.storage_id = ml.storage_id
        WHERE m.next_revision_date IS NOT NULL AND m.next_revision_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
        ORDER BY m.next_revision_date
    """

    def select(self):
        maquinas = []
        filas = self._select(self.SQL_SELECT, ())
        for fila in filas:
            maquinas.append(MachineVo(fila[0], fila[1], fila[2], fila[3], fila[4]))
        return maquinas

    def select_by_id(self, machine_id):
        fila = self._select_one(self.SQL_SELECT_BY_ID, (machine_id,))
        if fila is None:
            return None
        return MachineVo(fila[0], fila[1], fila[2], fila[3], fila[4])

    def insert(self, machine):
        return self._write(
            self.SQL_INSERT,
            (machine.machine_id, machine.state, machine.last_revision_date, machine.next_revision_date, machine.description)
        )

    def update(self, machine):
        return self._write(
            self.SQL_UPDATE,
            (machine.state, machine.last_revision_date, machine.next_revision_date, machine.description, machine.machine_id)
        )

    def update_state(self, machine_id, state):
        return self._write(self.SQL_UPDATE_STATE, (state, machine_id))

    def delete(self, machine_id):
        return self._write(self.SQL_DELETE, (machine_id,))

    def select_inventario(self, nombre, filtro):
        texto = ""
        patron = "%"
        if nombre is not None and nombre.strip() != "":
            texto = nombre.strip()
            patron = "%" + texto + "%"
        estado = ""
        if filtro is not None:
            estado = filtro
        filas = self._select(self.SQL_INVENTARIO, (texto, patron, estado, estado, estado))
        return self.__rows_to_inventario(filas)

    def select_disponibles(self):
        return self.__rows_to_inventario(self._select(self.SQL_DISPONIBLES, ()))

    def count(self):
        fila = self._select_one(self.SQL_TOTAL, ())
        if fila is None:
            return 0
        return fila[0]

    def select_by_state_count(self):
        return self._select(self.SQL_BY_STATE, ())

    def select_revisiones_proximas(self):
        return self.__rows_to_inventario(self._select(self.SQL_REVISION, ()))

    def __rows_to_inventario(self, filas):
        datos = []
        for fila in filas:
            datos.append(MachineInventarioVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8]))
        return datos
