from enum import Enum


class GetPlaybooksSort(str, Enum):
    TITLE = "title"
    STAGES = "stages"
    STEPS = "steps"

    def __str__(self) -> str:
        return str(self.value)
