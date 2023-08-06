import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.file_status import FileStatus
from ..models.file_type import FileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileDatasetOut")


@attr.s(auto_attribs=True)
class FileDatasetOut:
    """
    Attributes:
        name (str):
        uid (str):
        status (FileStatus): An enumeration.
        collected (Union[Unset, datetime.datetime]):
        duration (Union[Unset, float]):
        creator (Union[Unset, str]):
        etag (Union[Unset, str]):
        size (Union[Unset, int]):
        mimetype (Union[Unset, str]):  Default: 'application/octet-stream'.
        altlocation (Union[Unset, str]):
        rating (Union[Unset, int]):
        immutable (Union[Unset, bool]):
        filetype (Union[Unset, FileType]): An enumeration. Default: FileType.UNDEFINED.
        created (Union[Unset, datetime.datetime]):
        modified (Union[Unset, datetime.datetime]):
        download_link (Union[Unset, str]):
    """

    name: str
    uid: str
    status: FileStatus
    collected: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, float] = UNSET
    creator: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    mimetype: Union[Unset, str] = "application/octet-stream"
    altlocation: Union[Unset, str] = UNSET
    rating: Union[Unset, int] = 0
    immutable: Union[Unset, bool] = False
    filetype: Union[Unset, FileType] = FileType.UNDEFINED
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    download_link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        uid = self.uid
        status = self.status.value

        collected: Union[Unset, str] = UNSET
        if not isinstance(self.collected, Unset):
            collected = self.collected.isoformat()

        duration = self.duration
        creator = self.creator
        etag = self.etag
        size = self.size
        mimetype = self.mimetype
        altlocation = self.altlocation
        rating = self.rating
        immutable = self.immutable
        filetype: Union[Unset, str] = UNSET
        if not isinstance(self.filetype, Unset):
            filetype = self.filetype.value

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        download_link = self.download_link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uid": uid,
                "status": status,
            }
        )
        if collected is not UNSET:
            field_dict["collected"] = collected
        if duration is not UNSET:
            field_dict["duration"] = duration
        if creator is not UNSET:
            field_dict["creator"] = creator
        if etag is not UNSET:
            field_dict["etag"] = etag
        if size is not UNSET:
            field_dict["size"] = size
        if mimetype is not UNSET:
            field_dict["mimetype"] = mimetype
        if altlocation is not UNSET:
            field_dict["altlocation"] = altlocation
        if rating is not UNSET:
            field_dict["rating"] = rating
        if immutable is not UNSET:
            field_dict["immutable"] = immutable
        if filetype is not UNSET:
            field_dict["filetype"] = filetype
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if download_link is not UNSET:
            field_dict["download_link"] = download_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        uid = d.pop("uid")

        status = FileStatus(d.pop("status"))

        _collected = d.pop("collected", UNSET)
        collected: Union[Unset, datetime.datetime]
        if isinstance(_collected, Unset):
            collected = UNSET
        else:
            collected = isoparse(_collected)

        duration = d.pop("duration", UNSET)

        creator = d.pop("creator", UNSET)

        etag = d.pop("etag", UNSET)

        size = d.pop("size", UNSET)

        mimetype = d.pop("mimetype", UNSET)

        altlocation = d.pop("altlocation", UNSET)

        rating = d.pop("rating", UNSET)

        immutable = d.pop("immutable", UNSET)

        _filetype = d.pop("filetype", UNSET)
        filetype: Union[Unset, FileType]
        if isinstance(_filetype, Unset):
            filetype = UNSET
        else:
            filetype = FileType(_filetype)

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

        download_link = d.pop("download_link", UNSET)

        file_dataset_out = cls(
            name=name,
            uid=uid,
            status=status,
            collected=collected,
            duration=duration,
            creator=creator,
            etag=etag,
            size=size,
            mimetype=mimetype,
            altlocation=altlocation,
            rating=rating,
            immutable=immutable,
            filetype=filetype,
            created=created,
            modified=modified,
            download_link=download_link,
        )

        file_dataset_out.additional_properties = d
        return file_dataset_out

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
