import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadOut")


@attr.s(auto_attribs=True)
class UploadOut:
    """
    Attributes:
        uid (str):
        offset (int):
        length (int):
        concat (bool):
        completed (bool):
        expires (Union[Unset, datetime.datetime]):
    """

    uid: str
    offset: int
    length: int
    concat: bool
    completed: bool
    expires: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid
        offset = self.offset
        length = self.length
        concat = self.concat
        completed = self.completed
        expires: Union[Unset, str] = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uid": uid,
                "offset": offset,
                "length": length,
                "concat": concat,
                "completed": completed,
            }
        )
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uid = d.pop("uid")

        offset = d.pop("offset")

        length = d.pop("length")

        concat = d.pop("concat")

        completed = d.pop("completed")

        _expires = d.pop("expires", UNSET)
        expires: Union[Unset, datetime.datetime]
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        upload_out = cls(
            uid=uid,
            offset=offset,
            length=length,
            concat=concat,
            completed=completed,
            expires=expires,
        )

        upload_out.additional_properties = d
        return upload_out

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
