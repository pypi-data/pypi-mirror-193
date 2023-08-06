from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_dm_insight_user_information import TopDMInsightUserInformation


T = TypeVar("T", bound="TopDM")


@attr.s(auto_attribs=True)
class TopDM:
    """
    Attributes:
        post_count (Union[Unset, int]):
        outgoing_message_count (Union[Unset, int]):
        second_participant (Union[Unset, TopDMInsightUserInformation]):
    """

    post_count: Union[Unset, int] = UNSET
    outgoing_message_count: Union[Unset, int] = UNSET
    second_participant: Union[Unset, "TopDMInsightUserInformation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        post_count = self.post_count
        outgoing_message_count = self.outgoing_message_count
        second_participant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.second_participant, Unset):
            second_participant = self.second_participant.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_count is not UNSET:
            field_dict["post_count"] = post_count
        if outgoing_message_count is not UNSET:
            field_dict["outgoing_message_count"] = outgoing_message_count
        if second_participant is not UNSET:
            field_dict["second_participant"] = second_participant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.top_dm_insight_user_information import TopDMInsightUserInformation

        d = src_dict.copy()
        post_count = d.pop("post_count", UNSET)

        outgoing_message_count = d.pop("outgoing_message_count", UNSET)

        _second_participant = d.pop("second_participant", UNSET)
        second_participant: Union[Unset, TopDMInsightUserInformation]
        if isinstance(_second_participant, Unset):
            second_participant = UNSET
        else:
            second_participant = TopDMInsightUserInformation.from_dict(_second_participant)

        top_dm = cls(
            post_count=post_count,
            outgoing_message_count=outgoing_message_count,
            second_participant=second_participant,
        )

        top_dm.additional_properties = d
        return top_dm

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
