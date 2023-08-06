"""
A tattoo parlor.

https://schema.org/TattooParlor
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TattooParlorInheritedProperties(TypedDict):
    """A tattoo parlor.

    References:
        https://schema.org/TattooParlor
    Note:
        Model Depth 5
    Attributes:
    """


class TattooParlorProperties(TypedDict):
    """A tattoo parlor.

    References:
        https://schema.org/TattooParlor
    Note:
        Model Depth 5
    Attributes:
    """


class TattooParlorAllProperties(
    TattooParlorInheritedProperties, TattooParlorProperties, TypedDict
):
    pass


class TattooParlorBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TattooParlor", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TattooParlorProperties,
        TattooParlorInheritedProperties,
        TattooParlorAllProperties,
    ] = TattooParlorAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TattooParlor"
    return model


TattooParlor = create_schema_org_model()


def create_tattooparlor_model(
    model: Union[
        TattooParlorProperties,
        TattooParlorInheritedProperties,
        TattooParlorAllProperties,
    ]
):
    _type = deepcopy(TattooParlorAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of TattooParlorAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TattooParlorAllProperties):
    pydantic_type = create_tattooparlor_model(model=model)
    return pydantic_type(model).schema_json()
