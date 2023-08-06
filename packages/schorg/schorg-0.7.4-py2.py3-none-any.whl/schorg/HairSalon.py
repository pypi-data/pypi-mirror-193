"""
A hair salon.

https://schema.org/HairSalon
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HairSalonInheritedProperties(TypedDict):
    """A hair salon.

    References:
        https://schema.org/HairSalon
    Note:
        Model Depth 5
    Attributes:
    """


class HairSalonProperties(TypedDict):
    """A hair salon.

    References:
        https://schema.org/HairSalon
    Note:
        Model Depth 5
    Attributes:
    """


class HairSalonAllProperties(
    HairSalonInheritedProperties, HairSalonProperties, TypedDict
):
    pass


class HairSalonBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HairSalon", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HairSalonProperties, HairSalonInheritedProperties, HairSalonAllProperties
    ] = HairSalonAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HairSalon"
    return model


HairSalon = create_schema_org_model()


def create_hairsalon_model(
    model: Union[
        HairSalonProperties, HairSalonInheritedProperties, HairSalonAllProperties
    ]
):
    _type = deepcopy(HairSalonAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of HairSalonAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HairSalonAllProperties):
    pydantic_type = create_hairsalon_model(model=model)
    return pydantic_type(model).schema_json()
