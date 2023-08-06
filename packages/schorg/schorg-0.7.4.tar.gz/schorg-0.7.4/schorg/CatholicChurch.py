"""
A Catholic church.

https://schema.org/CatholicChurch
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CatholicChurchInheritedProperties(TypedDict):
    """A Catholic church.

    References:
        https://schema.org/CatholicChurch
    Note:
        Model Depth 6
    Attributes:
    """


class CatholicChurchProperties(TypedDict):
    """A Catholic church.

    References:
        https://schema.org/CatholicChurch
    Note:
        Model Depth 6
    Attributes:
    """


class CatholicChurchAllProperties(
    CatholicChurchInheritedProperties, CatholicChurchProperties, TypedDict
):
    pass


class CatholicChurchBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CatholicChurch", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CatholicChurchProperties,
        CatholicChurchInheritedProperties,
        CatholicChurchAllProperties,
    ] = CatholicChurchAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CatholicChurch"
    return model


CatholicChurch = create_schema_org_model()


def create_catholicchurch_model(
    model: Union[
        CatholicChurchProperties,
        CatholicChurchInheritedProperties,
        CatholicChurchAllProperties,
    ]
):
    _type = deepcopy(CatholicChurchAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CatholicChurchAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CatholicChurchAllProperties):
    pydantic_type = create_catholicchurch_model(model=model)
    return pydantic_type(model).schema_json()
