class MaterialVo:
    def __init__(
        self,
        material_id: int,
        specifications: str,
        formula: str,
        measure_unit: str
    ) -> None:
        self.__material_id = material_id
        self.__specifications = specifications
        self.__formula = formula
        self.__measure_unit = measure_unit

    @property
    def material_id(self) -> int:
        return self.__material_id

    @property
    def specifications(self) -> str:
        return self.__specifications

    @property
    def formula(self) -> str:
        return self.__formula

    @property
    def measure_unit(self) -> str:
        return self.__measure_unit
