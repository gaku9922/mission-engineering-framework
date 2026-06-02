from dataclasses import dataclass
from typing import Callable
from capabilities.base import Capability
from missions.mission import Mission

@dataclass
class MOE:
    id: str
    name: str
    mission: Mission
    capabilities: list[Capability]
    unit: str
    description: str
    calc_func: Callable[[list[Capability]], float]

    @property
    def value(self) -> float:
        """
        Capabilityの値が更新されても、常に最新のMOEの値を再計算して返す
        """
        return self.calc_func(self.capabilities)