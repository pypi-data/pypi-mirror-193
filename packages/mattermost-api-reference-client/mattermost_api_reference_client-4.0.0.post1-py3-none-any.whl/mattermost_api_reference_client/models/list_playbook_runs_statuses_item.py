from enum import Enum


class ListPlaybookRunsStatusesItem(str, Enum):
    INPROGRESS = "InProgress"
    FINISHED = "Finished"

    def __str__(self) -> str:
        return str(self.value)
