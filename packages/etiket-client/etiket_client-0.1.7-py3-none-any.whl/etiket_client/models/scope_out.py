import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScopeOut")


@attr.s(auto_attribs=True)
class ScopeOut:
    """
    Attributes:
        name (str):
        description (str):
        restricted (Union[Unset, datetime.datetime]):
        archived (Union[Unset, datetime.datetime]):
        created (Union[Unset, datetime.datetime]):
        modified (Union[Unset, datetime.datetime]):
    """

    name: str
    description: str
    restricted: Union[Unset, datetime.datetime] = UNSET
    archived: Union[Unset, datetime.datetime] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
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

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

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
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified

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

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        scope_out = cls(
            name=name,
            description=description,
            restricted=restricted,
            archived=archived,
            created=created,
            modified=modified,
        )

        scope_out.additional_properties = d
        return scope_out

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
