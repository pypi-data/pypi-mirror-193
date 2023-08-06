"""
Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed Forces.

https://schema.org/Nonprofit501c19
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c19InheritedProperties(TypedDict):
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed Forces.

    References:
        https://schema.org/Nonprofit501c19
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c19Properties(TypedDict):
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed Forces.

    References:
        https://schema.org/Nonprofit501c19
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c19AllProperties(
    Nonprofit501c19InheritedProperties, Nonprofit501c19Properties, TypedDict
):
    pass


class Nonprofit501c19BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c19", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c19Properties,
        Nonprofit501c19InheritedProperties,
        Nonprofit501c19AllProperties,
    ] = Nonprofit501c19AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c19"
    return model


Nonprofit501c19 = create_schema_org_model()


def create_nonprofit501c19_model(
    model: Union[
        Nonprofit501c19Properties,
        Nonprofit501c19InheritedProperties,
        Nonprofit501c19AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c19AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of Nonprofit501c19AllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c19AllProperties):
    pydantic_type = create_nonprofit501c19_model(model=model)
    return pydantic_type(model).schema_json()
