"""
Genitourinary system function assessment with clinical examination.

https://schema.org/Genitourinary
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GenitourinaryInheritedProperties(TypedDict):
    """Genitourinary system function assessment with clinical examination.

    References:
        https://schema.org/Genitourinary
    Note:
        Model Depth 5
    Attributes:
    """


class GenitourinaryProperties(TypedDict):
    """Genitourinary system function assessment with clinical examination.

    References:
        https://schema.org/Genitourinary
    Note:
        Model Depth 5
    Attributes:
    """


class GenitourinaryAllProperties(
    GenitourinaryInheritedProperties, GenitourinaryProperties, TypedDict
):
    pass


class GenitourinaryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Genitourinary", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GenitourinaryProperties,
        GenitourinaryInheritedProperties,
        GenitourinaryAllProperties,
    ] = GenitourinaryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Genitourinary"
    return model


Genitourinary = create_schema_org_model()


def create_genitourinary_model(
    model: Union[
        GenitourinaryProperties,
        GenitourinaryInheritedProperties,
        GenitourinaryAllProperties,
    ]
):
    _type = deepcopy(GenitourinaryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of GenitourinaryAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GenitourinaryAllProperties):
    pydantic_type = create_genitourinary_model(model=model)
    return pydantic_type(model).schema_json()
