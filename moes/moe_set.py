from moes import MOE
from capabilities import Capability
from capabilities import CapabilitySet
from missions import Mission


class MOESet:
    def __init__(self, capability_set: CapabilitySet):

        # 月面移動探査達成率
        def moon_surface_movement_exploration_achievement_rate_calc_func(caps: list[Capability]) -> float:
            return (caps[0].value + caps[1].value) / 2

        self.moon_surface_movement_exploration_achievement_rate_moe: MOE = MOE(
            id="moon_surface_movement_exploration_achievement_rate_moe",
            name="月面移動探査達成率",
            mission=Mission.EXPLORATION_MOBILITY,
            capabilities=[
                capability_set.moon_surface_movement_distance_ability,
                capability_set.moon_surface_movement_speed_ability
            ],
            unit="-",
            description="月面移動探査達成率は、月面移動能力（距離）と月面移動能力（速度）の合計を月面移動能力（距離）と月面移動能力（速度）の合計で割った値です。",
            calc_func=moon_surface_movement_exploration_achievement_rate_calc_func,
        )

        # 電力供給達成率
        def power_supply_achievement_rate_calc_func(caps: list[Capability]) -> float:
            return caps[0].value / 1000 * 100

        self.power_supply_achievement_rate_moe: MOE = MOE(
            id="power_supply_achievement_rate_moe",
            name="電力供給達成率",
            mission=Mission.POWER_THERMAL_MANAGEMENT,
            capabilities=[capability_set.power_supply_ability],
            unit="%",
            description="電力供給達成率は、電力供給能力を電力供給要求量で割った値です。",
            calc_func=power_supply_achievement_rate_calc_func,
        )

        # 通信達成率
        def communication_achievement_rate_calc_func(caps: list[Capability]) -> float:
            return caps[0].value / 500 * 100

        self.communication_achievement_rate_moe: MOE = MOE(
            id="communication_achievement_rate_moe",
            name="通信達成率",
            mission=Mission.COMMUNICATION_OPERATION,
            capabilities=[capability_set.communication_ability],
            unit="%",
            description="通信達成率は、通信能力を通信要求量で割った値です。",
            calc_func=communication_achievement_rate_calc_func,
        )