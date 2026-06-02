from enum import Enum


class Mission(Enum):
    TRANSPORTATION = "輸送・補給・帰還"
    POWER_THERMAL_MANAGEMENT = "電力・熱管理"
    COMMUNICATION_OPERATION = "通信測位・運用管制"
    MANNED_BASE_LIFE_SUPPORT = "有人拠点・生命維持・保全"
    FOOD_RESOURCE_CIRCULATION = "食糧生産・生活資源循環"
    RESOURCE_UTILIZATION = "資源利用・推薬・資材製造"
    EXPLORATION_MOBILITY = "広域探査・表面移動"
    SCIENCE_VALUE_CREATION = "科学・価値創出"
