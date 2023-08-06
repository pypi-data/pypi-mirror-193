from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TriggerIdReturn")


@attr.s(auto_attribs=True)
class TriggerIdReturn:
    """
    Attributes:
        trigger_id (str): The trigger_id returned by the slash command. Example: ceenjwsg6tgdzjpofxqemy1aio.
    """

    trigger_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trigger_id = self.trigger_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_id": trigger_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trigger_id = d.pop("trigger_id")

        trigger_id_return = cls(
            trigger_id=trigger_id,
        )

        trigger_id_return.additional_properties = d
        return trigger_id_return

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
