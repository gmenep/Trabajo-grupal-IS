from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.MachineVo import MachineVo


class MachineDaoJDBC(Conexion):
    SQL_SELECT = """
        SELECT machine_id, state, last_revision_date, next_revision_date, description
        FROM machines
    """
    SQL_SELECT_BY_ID = """
        SELECT machine_id, state, last_revision_date, next_revision_date, description
        FROM machines
        WHERE machine_id = ?
    """
    SQL_INSERT = """
        INSERT INTO machines(
            machine_id, state, last_revision_date, next_revision_date, description
        )
        VALUES(?, ?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE machines
        SET state = ?, last_revision_date = ?, next_revision_date = ?, description = ?
        WHERE machine_id = ?
    """
    SQL_DELETE = "DELETE FROM machines WHERE machine_id = ?"

    def select(self) -> list[MachineVo]:
        cursor = None
        machines = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                machines.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Machine:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return machines

    def select_by_id(self, machine_id: int) -> MachineVo | None:
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (machine_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Machine:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, machine: MachineVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (
                    machine.machine_id,
                    machine.state,
                    machine.last_revision_date,
                    machine.next_revision_date,
                    machine.description
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Machine:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, machine: MachineVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (
                    machine.state,
                    machine.last_revision_date,
                    machine.next_revision_date,
                    machine.description,
                    machine.machine_id
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Machine:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, machine_id: int) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (machine_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Machine:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row) -> MachineVo:
        machine_id, state, last_revision_date, next_revision_date, description = row
        return MachineVo(
            machine_id,
            state,
            last_revision_date,
            next_revision_date,
            description
        )

    def __commit(self) -> None:
        if self.conexion is not None:
            self.conexion.commit()
