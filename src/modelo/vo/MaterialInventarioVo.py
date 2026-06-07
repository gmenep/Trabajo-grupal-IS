class MaterialInventarioVo:
    def __init__(self, material_id, name, risk_level, specifications, formula, measure_unit, storage_id, storage_name, batch_number, quantity, exp_date):
        self.__material_id = material_id
        self.__name = name
        self.__risk_level = risk_level
        self.__specifications = specifications
        self.__formula = formula
        self.__measure_unit = measure_unit
        self.__storage_id = storage_id
        self.__storage_name = storage_name
        self.__batch_number = batch_number
        self.__quantity = quantity
        self.__exp_date = exp_date

    @property
    def material_id(self):
        return self.__material_id

    @property
    def name(self):
        return self.__name

    @property
    def risk_level(self):
        return self.__risk_level

    @property
    def specifications(self):
        return self.__specifications

    @property
    def formula(self):
        return self.__formula

    @property
    def measure_unit(self):
        return self.__measure_unit

    @property
    def storage_id(self):
        return self.__storage_id

    @property
    def storage_name(self):
        return self.__storage_name

    @property
    def batch_number(self):
        return self.__batch_number

    @property
    def quantity(self):
        return self.__quantity

    @property
    def exp_date(self):
        return self.__exp_date
