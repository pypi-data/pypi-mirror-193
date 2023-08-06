"""
Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.

https://schema.org/Nonprofit501q
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501qInheritedProperties(TypedDict):
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.

    References:
        https://schema.org/Nonprofit501q
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501qProperties(TypedDict):
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.

    References:
        https://schema.org/Nonprofit501q
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501qAllProperties(
    Nonprofit501qInheritedProperties, Nonprofit501qProperties, TypedDict
):
    pass


class Nonprofit501qBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501q", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501qProperties,
        Nonprofit501qInheritedProperties,
        Nonprofit501qAllProperties,
    ] = Nonprofit501qAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501q"
    return model


Nonprofit501q = create_schema_org_model()


def create_nonprofit501q_model(
    model: Union[
        Nonprofit501qProperties,
        Nonprofit501qInheritedProperties,
        Nonprofit501qAllProperties,
    ]
):
    _type = deepcopy(Nonprofit501qAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of Nonprofit501qAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501qAllProperties):
    pydantic_type = create_nonprofit501q_model(model=model)
    return pydantic_type(model).schema_json()
