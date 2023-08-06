from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsightUserInformation")


@attr.s(auto_attribs=True)
class InsightUserInformation:
    """
    Attributes:
        id (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        nickname (Union[Unset, str]):
        username (Union[Unset, str]):
        last_picture_update (Union[Unset, str]):
        create_at (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    last_picture_update: Union[Unset, str] = UNSET
    create_at: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        first_name = self.first_name
        last_name = self.last_name
        nickname = self.nickname
        username = self.username
        last_picture_update = self.last_picture_update
        create_at = self.create_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if username is not UNSET:
            field_dict["username"] = username
        if last_picture_update is not UNSET:
            field_dict["last_picture_update"] = last_picture_update
        if create_at is not UNSET:
            field_dict["create_at"] = create_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        nickname = d.pop("nickname", UNSET)

        username = d.pop("username", UNSET)

        last_picture_update = d.pop("last_picture_update", UNSET)

        create_at = d.pop("create_at", UNSET)

        insight_user_information = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            username=username,
            last_picture_update=last_picture_update,
            create_at=create_at,
        )

        insight_user_information.additional_properties = d
        return insight_user_information

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
