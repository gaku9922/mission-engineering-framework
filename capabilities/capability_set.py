from resources import ResourceSet
from capabilities import Capability


class CapabilitySet:
    def __init__(self, resource_set: ResourceSet):

        # 月面移動能力（距離）
        self.moon_surface_movement_distance_ability: Capability = Capability(
            id="moon_surface_movement_distance_ability",
            name="月面移動能力（距離）",
            value=100,
            unit="km",
            resources=[resource_set.pressurized_rover, resource_set.long_distance_hopper],
        )

        # 月面移動能力（速度）
        self.moon_surface_movement_speed_ability: Capability = Capability(
            id="moon_surface_movement_speed_ability",
            name="月面移動能力（速度）",
            value=100,
            unit="km/h",
            resources=[resource_set.pressurized_rover, resource_set.long_distance_hopper],
        )

        # 電力供給能力
        self.power_supply_ability: Capability = Capability(
            id="power_supply_ability",
            name="電力供給能力",
            value=100,
            unit="kW",
            resources=[resource_set.power_system],
        )

        # 通信能力
        self.communication_ability: Capability = Capability(
            id="communication_ability",
            name="通信能力",
            value=100,
            unit="Mbps",
            resources=[resource_set.antenna_unit],
        )