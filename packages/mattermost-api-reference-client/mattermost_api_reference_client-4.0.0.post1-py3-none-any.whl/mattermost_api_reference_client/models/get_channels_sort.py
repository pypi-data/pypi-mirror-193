from enum import Enum


class GetChannelsSort(str, Enum):
    ID = "id"
    NAME = "name"
    CREATE_AT = "create_at"
    END_AT = "end_at"
    TEAM_ID = "team_id"
    OWNER_USER_ID = "owner_user_id"

    def __str__(self) -> str:
        return str(self.value)
