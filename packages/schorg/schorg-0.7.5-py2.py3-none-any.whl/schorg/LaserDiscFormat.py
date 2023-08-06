"""
LaserDiscFormat.

https://schema.org/LaserDiscFormat
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LaserDiscFormatInheritedProperties(TypedDict):
    """LaserDiscFormat.

    References:
        https://schema.org/LaserDiscFormat
    Note:
        Model Depth 5
    Attributes:
    """


class LaserDiscFormatProperties(TypedDict):
    """LaserDiscFormat.

    References:
        https://schema.org/LaserDiscFormat
    Note:
        Model Depth 5
    Attributes:
    """


class LaserDiscFormatAllProperties(
    LaserDiscFormatInheritedProperties, LaserDiscFormatProperties, TypedDict
):
    pass


class LaserDiscFormatBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LaserDiscFormat", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LaserDiscFormatProperties,
        LaserDiscFormatInheritedProperties,
        LaserDiscFormatAllProperties,
    ] = LaserDiscFormatAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LaserDiscFormat"
    return model


LaserDiscFormat = create_schema_org_model()


def create_laserdiscformat_model(
    model: Union[
        LaserDiscFormatProperties,
        LaserDiscFormatInheritedProperties,
        LaserDiscFormatAllProperties,
    ]
):
    _type = deepcopy(LaserDiscFormatAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LaserDiscFormat. Please see: https://schema.org/LaserDiscFormat"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LaserDiscFormatAllProperties):
    pydantic_type = create_laserdiscformat_model(model=model)
    return pydantic_type(model).schema_json()
