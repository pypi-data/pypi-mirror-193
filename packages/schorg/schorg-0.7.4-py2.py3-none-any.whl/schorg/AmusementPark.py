"""
An amusement park.

https://schema.org/AmusementPark
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AmusementParkInheritedProperties(TypedDict):
    """An amusement park.

    References:
        https://schema.org/AmusementPark
    Note:
        Model Depth 5
    Attributes:
    """


class AmusementParkProperties(TypedDict):
    """An amusement park.

    References:
        https://schema.org/AmusementPark
    Note:
        Model Depth 5
    Attributes:
    """


class AmusementParkAllProperties(
    AmusementParkInheritedProperties, AmusementParkProperties, TypedDict
):
    pass


class AmusementParkBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AmusementPark", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AmusementParkProperties,
        AmusementParkInheritedProperties,
        AmusementParkAllProperties,
    ] = AmusementParkAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AmusementPark"
    return model


AmusementPark = create_schema_org_model()


def create_amusementpark_model(
    model: Union[
        AmusementParkProperties,
        AmusementParkInheritedProperties,
        AmusementParkAllProperties,
    ]
):
    _type = deepcopy(AmusementParkAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AmusementParkAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AmusementParkAllProperties):
    pydantic_type = create_amusementpark_model(model=model)
    return pydantic_type(model).schema_json()
