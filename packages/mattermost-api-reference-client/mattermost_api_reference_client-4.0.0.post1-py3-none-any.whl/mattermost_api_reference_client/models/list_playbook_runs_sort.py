from enum import Enum


class ListPlaybookRunsSort(str, Enum):
    ID = "id"
    NAME = "name"
    IS_ACTIVE = "is_active"
    CREATE_AT = "create_at"
    END_AT = "end_at"
    TEAM_ID = "team_id"
    OWNER_USER_ID = "owner_user_id"

    def __str__(self) -> str:
        return str(self.value)
