from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ItemRenameJsonBody")


@attr.s(auto_attribs=True)
class ItemRenameJsonBody:
    """
    Attributes:
        title (str): The new title of the item. Example: Gather information from server's logs..
        command (str): The new slash command of the item. Example: /jira update ticket.
    """

    title: str
    command: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        command = self.command

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "command": command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        command = d.pop("command")

        item_rename_json_body = cls(
            title=title,
            command=command,
        )

        item_rename_json_body.additional_properties = d
        return item_rename_json_body

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
