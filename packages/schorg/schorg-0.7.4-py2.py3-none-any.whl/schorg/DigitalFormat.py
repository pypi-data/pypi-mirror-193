"""
DigitalFormat.

https://schema.org/DigitalFormat
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DigitalFormatInheritedProperties(TypedDict):
    """DigitalFormat.

    References:
        https://schema.org/DigitalFormat
    Note:
        Model Depth 5
    Attributes:
    """


class DigitalFormatProperties(TypedDict):
    """DigitalFormat.

    References:
        https://schema.org/DigitalFormat
    Note:
        Model Depth 5
    Attributes:
    """


class DigitalFormatAllProperties(
    DigitalFormatInheritedProperties, DigitalFormatProperties, TypedDict
):
    pass


class DigitalFormatBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DigitalFormat", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DigitalFormatProperties,
        DigitalFormatInheritedProperties,
        DigitalFormatAllProperties,
    ] = DigitalFormatAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DigitalFormat"
    return model


DigitalFormat = create_schema_org_model()


def create_digitalformat_model(
    model: Union[
        DigitalFormatProperties,
        DigitalFormatInheritedProperties,
        DigitalFormatAllProperties,
    ]
):
    _type = deepcopy(DigitalFormatAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DigitalFormatAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DigitalFormatAllProperties):
    pydantic_type = create_digitalformat_model(model=model)
    return pydantic_type(model).schema_json()
