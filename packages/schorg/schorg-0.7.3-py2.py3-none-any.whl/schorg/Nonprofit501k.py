"""
Nonprofit501k: Non-profit type referring to Child Care Organizations.

https://schema.org/Nonprofit501k
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501kInheritedProperties(TypedDict):
    """Nonprofit501k: Non-profit type referring to Child Care Organizations.

    References:
        https://schema.org/Nonprofit501k
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501kProperties(TypedDict):
    """Nonprofit501k: Non-profit type referring to Child Care Organizations.

    References:
        https://schema.org/Nonprofit501k
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501kAllProperties(
    Nonprofit501kInheritedProperties, Nonprofit501kProperties, TypedDict
):
    pass


class Nonprofit501kBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501k", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501kProperties,
        Nonprofit501kInheritedProperties,
        Nonprofit501kAllProperties,
    ] = Nonprofit501kAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501k"
    return model


Nonprofit501k = create_schema_org_model()


def create_nonprofit501k_model(
    model: Union[
        Nonprofit501kProperties,
        Nonprofit501kInheritedProperties,
        Nonprofit501kAllProperties,
    ]
):
    _type = deepcopy(Nonprofit501kAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501kAllProperties):
    pydantic_type = create_nonprofit501k_model(model=model)
    return pydantic_type(model).schema_json()
