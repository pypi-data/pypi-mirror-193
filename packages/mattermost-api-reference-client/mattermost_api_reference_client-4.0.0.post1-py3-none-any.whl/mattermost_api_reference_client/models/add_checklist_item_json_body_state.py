from enum import Enum


class AddChecklistItemJsonBodyState(str, Enum):
    VALUE_0 = ""
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
