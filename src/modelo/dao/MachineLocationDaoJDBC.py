from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.MachineLocationVo import MachineLocationVo


class MachineLocationDaoJDBC(BaseDaoJDBC):
    SQL_SELECT = "SELECT machine_id, storage_id FROM machine_location WHERE machine_id = ?"
    SQL_UPSERT = """
        INSERT INTO machine_location(machine_id, storage_id)
        VALUES(?, ?)
        ON DUPLICATE KEY UPDATE storage_id = VALUES(storage_id)
    """
    SQL_DELETE = "DELETE FROM machine_location WHERE machine_id = ?"

    def select_by_machine(self, machine_id):
        fila = self._select_one(self.SQL_SELECT, (machine_id,))
        if fila is None:
            return None
        return MachineLocationVo(fila[0], fila[1])

    def upsert(self, machine_location):
        return self._write(self.SQL_UPSERT, (machine_location.machine_id, machine_location.storage_id))

    def delete(self, machine_id):
        return self._write(self.SQL_DELETE, (machine_id,))
