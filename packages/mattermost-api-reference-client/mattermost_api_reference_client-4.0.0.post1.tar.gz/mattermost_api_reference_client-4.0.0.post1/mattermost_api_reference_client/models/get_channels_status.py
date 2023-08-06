from enum import Enum


class GetChannelsStatus(str, Enum):
    ALL = "all"
    INPROGRESS = "InProgress"
    FINISHED = "Finished"

    def __str__(self) -> str:
        return str(self.value)
