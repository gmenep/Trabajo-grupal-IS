class MaterialVo:
    def __init__(
        self,
        material_id,
        specifications,
        formula,
        measure_unit
    ):
        self.__material_id = material_id
        self.__specifications = specifications
        self.__formula = formula
        self.__measure_unit = measure_unit

    @property
    def material_id(self):
        return self.__material_id

    @material_id.setter
    def material_id(self, material_id):
        self.__material_id = material_id

    @property
    def specifications(self):
        return self.__specifications

    @specifications.setter
    def specifications(self, specifications):
        self.__specifications = specifications

    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula):
        self.__formula = formula

    @property
    def measure_unit(self):
        return self.__measure_unit

    @measure_unit.setter
    def measure_unit(self, measure_unit):
        self.__measure_unit = measure_unit
