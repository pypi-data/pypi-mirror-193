from enum import Enum


class FileType(str, Enum):
    UNDEFINED = "undefined"
    SRC = "src"
    PREVIEW = "preview"
    RAW = "raw"
    DERIVED = "derived"
    CONF = "conf"

    def __str__(self) -> str:
        return str(self.value)
