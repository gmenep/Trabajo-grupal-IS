class AssetVo:
    def __init__(self, asset_id, name, asset_type, risk_level):
        self.__asset_id = asset_id
        self.__name = name
        self.__asset_type = asset_type
        self.__risk_level = risk_level

    @property
    def asset_id(self):
        return self.__asset_id

    @property
    def name(self):
        return self.__name

    @property
    def asset_type(self):
        return self.__asset_type

    @property
    def risk_level(self):
        return self.__risk_level
