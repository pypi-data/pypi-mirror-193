from typing import ClassVar, Type

from msgspec import Struct


class SchemaModel(Struct):
    __schemas__: ClassVar[dict[str, Type["SchemaModel"]]] = dict()

    def __init_subclass__(cls) -> None:
        SchemaModel.__schemas__[cls.__name__] = cls

    @classmethod
    def customize_schema(cls, schema: dict) -> dict:
        return schema
