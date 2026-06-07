class MaterialVo:
    def __init__(self, material_id, specifications, formula, measure_unit):
        self.__material_id = material_id
        self.__specifications = specifications
        self.__formula = formula
        self.__measure_unit = measure_unit

    @property
    def material_id(self):
        return self.__material_id

    @property
    def specifications(self):
        return self.__specifications

    @property
    def formula(self):
        return self.__formula

    @property
    def measure_unit(self):
        return self.__measure_unit
