"""
Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

https://schema.org/Nonprofit501a
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501aInheritedProperties(TypedDict):
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

    References:
        https://schema.org/Nonprofit501a
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501aProperties(TypedDict):
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

    References:
        https://schema.org/Nonprofit501a
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501aAllProperties(
    Nonprofit501aInheritedProperties, Nonprofit501aProperties, TypedDict
):
    pass


class Nonprofit501aBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501a", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501aProperties,
        Nonprofit501aInheritedProperties,
        Nonprofit501aAllProperties,
    ] = Nonprofit501aAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501a"
    return model


Nonprofit501a = create_schema_org_model()


def create_nonprofit501a_model(
    model: Union[
        Nonprofit501aProperties,
        Nonprofit501aInheritedProperties,
        Nonprofit501aAllProperties,
    ]
):
    _type = deepcopy(Nonprofit501aAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501aAllProperties):
    pydantic_type = create_nonprofit501a_model(model=model)
    return pydantic_type(model).schema_json()
