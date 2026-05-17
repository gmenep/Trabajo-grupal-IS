from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.MaterialVo import MaterialVo


class MaterialDaoJDBC(Conexion):
    SQL_SELECT = """
        SELECT material_id, specifications, formula, measure_unit
        FROM materials
    """
    SQL_SELECT_BY_ID = """
        SELECT material_id, specifications, formula, measure_unit
        FROM materials
        WHERE material_id = ?
    """
    SQL_INSERT = """
        INSERT INTO materials(material_id, specifications, formula, measure_unit)
        VALUES(?, ?, ?, ?)
    """
    SQL_UPDATE = """
        UPDATE materials
        SET specifications = ?, formula = ?, measure_unit = ?
        WHERE material_id = ?
    """
    SQL_DELETE = "DELETE FROM materials WHERE material_id = ?"

    def select(self) -> list[MaterialVo]:
        cursor = None
        materials = []

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()

            for row in rows:
                materials.append(self.__map_row(row))

        except Exception as e:
            print("Error en select de Material:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return materials

    def select_by_id(self, material_id: int) -> MaterialVo | None:
        cursor = None

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT_BY_ID, (material_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return self.__map_row(row)

        except Exception as e:
            print("Error en select_by_id de Material:", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()

    def insert(self, material: MaterialVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_INSERT,
                (
                    material.material_id,
                    material.specifications,
                    material.formula,
                    material.measure_unit
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en insert de Material:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def update(self, material: MaterialVo) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(
                self.SQL_UPDATE,
                (
                    material.specifications,
                    material.formula,
                    material.measure_unit,
                    material.material_id
                )
            )
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en update de Material:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def delete(self, material_id: int) -> int:
        cursor = None
        rows = 0

        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_DELETE, (material_id,))
            rows = cursor.rowcount
            self.__commit()

        except Exception as e:
            print("Error en delete de Material:", e)

        finally:
            if cursor is not None:
                cursor.close()

        return rows

    def __map_row(self, row) -> MaterialVo:
        material_id, specifications, formula, measure_unit = row
        return MaterialVo(material_id, specifications, formula, measure_unit)

    def __commit(self) -> None:
        if self.conexion is not None:
            self.conexion.commit()
