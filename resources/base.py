from dataclasses import dataclass


@dataclass
class Resource:
    id: str
    name: str
    description: str