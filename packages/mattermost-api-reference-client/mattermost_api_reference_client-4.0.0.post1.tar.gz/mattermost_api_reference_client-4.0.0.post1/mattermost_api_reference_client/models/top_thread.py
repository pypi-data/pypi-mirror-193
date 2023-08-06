from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insight_user_information import InsightUserInformation
    from ..models.post import Post


T = TypeVar("T", bound="TopThread")


@attr.s(auto_attribs=True)
class TopThread:
    """
    Attributes:
        post (Union[Unset, Post]):
        channel_id (Union[Unset, str]):
        channel_display_name (Union[Unset, str]):
        channel_name (Union[Unset, str]):
        participants (Union[Unset, List[str]]):
        user_information (Union[Unset, InsightUserInformation]):
    """

    post: Union[Unset, "Post"] = UNSET
    channel_id: Union[Unset, str] = UNSET
    channel_display_name: Union[Unset, str] = UNSET
    channel_name: Union[Unset, str] = UNSET
    participants: Union[Unset, List[str]] = UNSET
    user_information: Union[Unset, "InsightUserInformation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        post: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        channel_id = self.channel_id
        channel_display_name = self.channel_display_name
        channel_name = self.channel_name
        participants: Union[Unset, List[str]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants

        user_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_information, Unset):
            user_information = self.user_information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post is not UNSET:
            field_dict["post"] = post
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if channel_display_name is not UNSET:
            field_dict["channel_display_name"] = channel_display_name
        if channel_name is not UNSET:
            field_dict["channel_name"] = channel_name
        if participants is not UNSET:
            field_dict["Participants"] = participants
        if user_information is not UNSET:
            field_dict["user_information"] = user_information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.insight_user_information import InsightUserInformation
        from ..models.post import Post

        d = src_dict.copy()
        _post = d.pop("post", UNSET)
        post: Union[Unset, Post]
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = Post.from_dict(_post)

        channel_id = d.pop("channel_id", UNSET)

        channel_display_name = d.pop("channel_display_name", UNSET)

        channel_name = d.pop("channel_name", UNSET)

        participants = cast(List[str], d.pop("Participants", UNSET))

        _user_information = d.pop("user_information", UNSET)
        user_information: Union[Unset, InsightUserInformation]
        if isinstance(_user_information, Unset):
            user_information = UNSET
        else:
            user_information = InsightUserInformation.from_dict(_user_information)

        top_thread = cls(
            post=post,
            channel_id=channel_id,
            channel_display_name=channel_display_name,
            channel_name=channel_name,
            participants=participants,
            user_information=user_information,
        )

        top_thread.additional_properties = d
        return top_thread

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
