from resources.base import Resource


# 月面与圧ローバー
pressurized_rover: Resource = Resource(
    id="pressurized_rover",
    name="月面与圧ローバー",
    description="月面を移動するための与圧ローバー",
)

# 居住棟
living_module: Resource = Resource(
    id="living_module",
    name="居住棟",
    description="居住するための棟",
)

# 長距離移動ホッパー
long_distance_hopper: Resource = Resource(
    id="long_distance_hopper",
    name="長距離移動ホッパー",
    description="長距離を移動するためのホッパー",
)

# アンテナユニット
antenna_unit: Resource = Resource(
    id="antenna_unit",
    name="アンテナユニット",
    description="アンテナを搭載するためのユニット",
)

# 電力システム
power_system: Resource = Resource(
    id="power_system",
    name="電力システム",
    description="電力を供給するためのシステム",
)