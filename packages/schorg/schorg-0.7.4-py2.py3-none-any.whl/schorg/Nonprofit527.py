"""
Nonprofit527: Non-profit type referring to political organizations.

https://schema.org/Nonprofit527
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit527InheritedProperties(TypedDict):
    """Nonprofit527: Non-profit type referring to political organizations.

    References:
        https://schema.org/Nonprofit527
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit527Properties(TypedDict):
    """Nonprofit527: Non-profit type referring to political organizations.

    References:
        https://schema.org/Nonprofit527
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit527AllProperties(
    Nonprofit527InheritedProperties, Nonprofit527Properties, TypedDict
):
    pass


class Nonprofit527BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit527", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit527Properties,
        Nonprofit527InheritedProperties,
        Nonprofit527AllProperties,
    ] = Nonprofit527AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit527"
    return model


Nonprofit527 = create_schema_org_model()


def create_nonprofit527_model(
    model: Union[
        Nonprofit527Properties,
        Nonprofit527InheritedProperties,
        Nonprofit527AllProperties,
    ]
):
    _type = deepcopy(Nonprofit527AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of Nonprofit527AllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit527AllProperties):
    pydantic_type = create_nonprofit527_model(model=model)
    return pydantic_type(model).schema_json()
