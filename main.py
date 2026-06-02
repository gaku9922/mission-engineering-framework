from resources import ResourceSet
from capabilities import CapabilitySet
from moes import MOESet

resource_set: ResourceSet = ResourceSet()
capability_set: CapabilitySet = CapabilitySet(resource_set=resource_set)
moe_set: MOESet = MOESet(capability_set=capability_set)

# MOE算出
print(moe_set.moon_surface_movement_exploration_achievement_rate_moe.value)
print(moe_set.power_supply_achievement_rate_moe.value)
print(moe_set.communication_achievement_rate_moe.value)