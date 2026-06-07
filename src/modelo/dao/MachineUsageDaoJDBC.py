from src.modelo.dao.BaseDaoJDBC import BaseDaoJDBC
from src.modelo.vo.MachineUsageVo import MachineUsageVo
from src.modelo.vo.ProyectoAsignacionVo import ProyectoAsignacionVo


class MachineUsageDaoJDBC(BaseDaoJDBC):
    SQL_SELECT_ACTIVE_BY_USER = """
        SELECT usage_id, machine_id, user_id, project_id, start_date, end_date, state
        FROM machine_usage
        WHERE user_id = ? AND state = 'ACTIVO'
        ORDER BY start_date
    """
    SQL_SELECT_ACTIVE_BY_MACHINE = """
        SELECT usage_id, machine_id, user_id, project_id, start_date, end_date, state
        FROM machine_usage
        WHERE machine_id = ? AND state = 'ACTIVO'
    """
    SQL_INSERT = """
        INSERT INTO machine_usage(machine_id, user_id, project_id, state)
        VALUES(?, ?, ?, ?)
    """
    SQL_FINISH = """
        UPDATE machine_usage
        SET state = 'FINALIZADO', end_date = NOW()
        WHERE usage_id = ? AND user_id = ? AND state = 'ACTIVO'
    """
    SQL_ASIGNACIONES = """
        SELECT mu.project_id, mu.machine_id, a.name, mu.user_id, COALESCE(u.full_name, u.login)
        FROM machine_usage mu
        INNER JOIN machines m ON m.machine_id = mu.machine_id
        INNER JOIN assets a ON a.asset_id = m.machine_id
        INNER JOIN users u ON u.user_id = mu.user_id
        WHERE mu.state = 'ACTIVO' AND mu.project_id IS NOT NULL
        ORDER BY mu.project_id, a.name
    """

    def __init__(self):
        BaseDaoJDBC.__init__(self)
        self.__asegurar_estructura()

    def select_active_by_user(self, user_id):
        return self.__rows_to_vo(self._select(self.SQL_SELECT_ACTIVE_BY_USER, (user_id,)))

    def select_active_by_machine(self, machine_id):
        return self.__rows_to_vo(self._select(self.SQL_SELECT_ACTIVE_BY_MACHINE, (machine_id,)))

    def insert(self, usage):
        return self._insert_id(self.SQL_INSERT, (usage.machine_id, usage.user_id, usage.project_id, usage.state))

    def finish(self, usage_id, user_id):
        return self._write(self.SQL_FINISH, (usage_id, user_id))

    def select_asignaciones_activas(self):
        asignaciones = []
        filas = self._select(self.SQL_ASIGNACIONES, ())
        for fila in filas:
            asignaciones.append(ProyectoAsignacionVo(fila[0], fila[1], fila[2], fila[3], fila[4]))
        return asignaciones

    def __asegurar_estructura(self):
        filas = self._select("SHOW COLUMNS FROM machine_usage LIKE 'project_id'", ())
        if len(filas) == 0:
            self._write("ALTER TABLE machine_usage ADD COLUMN project_id int NULL AFTER user_id", ())

    def __rows_to_vo(self, filas):
        usos = []
        for fila in filas:
            usos.append(MachineUsageVo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))
        return usos
