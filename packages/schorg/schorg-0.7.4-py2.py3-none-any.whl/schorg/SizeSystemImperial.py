"""
Imperial size system.

https://schema.org/SizeSystemImperial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SizeSystemImperialInheritedProperties(TypedDict):
    """Imperial size system.

    References:
        https://schema.org/SizeSystemImperial
    Note:
        Model Depth 5
    Attributes:
    """


class SizeSystemImperialProperties(TypedDict):
    """Imperial size system.

    References:
        https://schema.org/SizeSystemImperial
    Note:
        Model Depth 5
    Attributes:
    """


class SizeSystemImperialAllProperties(
    SizeSystemImperialInheritedProperties, SizeSystemImperialProperties, TypedDict
):
    pass


class SizeSystemImperialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SizeSystemImperial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SizeSystemImperialProperties,
        SizeSystemImperialInheritedProperties,
        SizeSystemImperialAllProperties,
    ] = SizeSystemImperialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SizeSystemImperial"
    return model


SizeSystemImperial = create_schema_org_model()


def create_sizesystemimperial_model(
    model: Union[
        SizeSystemImperialProperties,
        SizeSystemImperialInheritedProperties,
        SizeSystemImperialAllProperties,
    ]
):
    _type = deepcopy(SizeSystemImperialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SizeSystemImperialAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SizeSystemImperialAllProperties):
    pydantic_type = create_sizesystemimperial_model(model=model)
    return pydantic_type(model).schema_json()
