from dataclasses import dataclass
from resources.base import Resource


@dataclass
class Capability:
    id: str
    name: str
    value: float
    unit: str
    resources: list[Resource]