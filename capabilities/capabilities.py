from capabilities.base import Capability
from resources import resources


# 月面移動能力（距離）
moon_surface_movement_distance_ability: Capability = Capability(
    id="moon_surface_movement_distance_ability",
    name="月面移動能力（距離）",
    value=100,
    unit="km",
    resources=[resources.pressurized_rover, resources.long_distance_hopper],
)

# 月面移動能力（速度）
moon_surface_movement_speed_ability: Capability = Capability(
    id="moon_surface_movement_speed_ability",
    name="月面移動能力（速度）",
    value=100,
    unit="km/h",
    resources=[resources.pressurized_rover, resources.long_distance_hopper],
)

# 電力供給能力
power_supply_ability: Capability = Capability(
    id="power_supply_ability",
    name="電力供給能力",
    value=100,
    unit="kW",
    resources=[resources.power_system],
)

# 通信能力
communication_ability: Capability = Capability(
    id="communication_ability",
    name="通信能力",
    value=100,
    unit="Mbps",
    resources=[resources.antenna_unit],
)