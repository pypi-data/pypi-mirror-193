import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScopeIn")


@attr.s(auto_attribs=True)
class ScopeIn:
    """
    Attributes:
        name (str):
        description (str):
        restricted (Union[Unset, datetime.datetime]):
        archived (Union[Unset, datetime.datetime]):
    """

    name: str
    description: str
    restricted: Union[Unset, datetime.datetime] = UNSET
    archived: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        restricted: Union[Unset, str] = UNSET
        if not isinstance(self.restricted, Unset):
            if self.restricted:
                restricted = self.restricted.isoformat()
            else:
                restricted = None

        archived: Union[Unset, str] = UNSET
        if not isinstance(self.archived, Unset):
            if self.archived:
                archived = self.archived.isoformat()
            else:
                archived = None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        _restricted = d.pop("restricted", UNSET)
        restricted: Union[Unset, datetime.datetime]
        if isinstance(_restricted, Unset):
            restricted = UNSET
        else:
            restricted = isoparse(_restricted) if _restricted else None

        _archived = d.pop("archived", UNSET)
        archived: Union[Unset, datetime.datetime]
        if isinstance(_archived, Unset):
            archived = UNSET
        else:
            archived = isoparse(_archived) if _archived else None

        scope_in = cls(
            name=name,
            description=description,
            restricted=restricted,
            archived=archived,
        )

        scope_in.additional_properties = d
        return scope_in

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
