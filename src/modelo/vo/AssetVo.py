class AssetVo:
    def __init__(
        self,
        asset_id: int | None,
        name: str,
        asset_type: str,
        risk_level: str
    ) -> None:
        self.__asset_id = asset_id
        self.__name = name
        self.__asset_type = asset_type
        self.__risk_level = risk_level

    @property
    def asset_id(self) -> int | None:
        return self.__asset_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def asset_type(self) -> str:
        return self.__asset_type

    @property
    def risk_level(self) -> str:
        return self.__risk_level
