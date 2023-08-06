"""
Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.

https://schema.org/Nonprofit501c14
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c14InheritedProperties(TypedDict):
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.

    References:
        https://schema.org/Nonprofit501c14
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c14Properties(TypedDict):
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.

    References:
        https://schema.org/Nonprofit501c14
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c14AllProperties(
    Nonprofit501c14InheritedProperties, Nonprofit501c14Properties, TypedDict
):
    pass


class Nonprofit501c14BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c14", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c14Properties,
        Nonprofit501c14InheritedProperties,
        Nonprofit501c14AllProperties,
    ] = Nonprofit501c14AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c14"
    return model


Nonprofit501c14 = create_schema_org_model()


def create_nonprofit501c14_model(
    model: Union[
        Nonprofit501c14Properties,
        Nonprofit501c14InheritedProperties,
        Nonprofit501c14AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c14AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of Nonprofit501c14AllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c14AllProperties):
    pydantic_type = create_nonprofit501c14_model(model=model)
    return pydantic_type(model).schema_json()
