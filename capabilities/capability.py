from dataclasses import dataclass
from resources import Resource


@dataclass
class Capability:
    id: str
    name: str
    value: float
    unit: str
    resources: list[Resource]