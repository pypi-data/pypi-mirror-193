"""
A courthouse.

https://schema.org/Courthouse
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CourthouseInheritedProperties(TypedDict):
    """A courthouse.

    References:
        https://schema.org/Courthouse
    Note:
        Model Depth 5
    Attributes:
    """


class CourthouseProperties(TypedDict):
    """A courthouse.

    References:
        https://schema.org/Courthouse
    Note:
        Model Depth 5
    Attributes:
    """


class CourthouseAllProperties(
    CourthouseInheritedProperties, CourthouseProperties, TypedDict
):
    pass


class CourthouseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Courthouse", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CourthouseProperties, CourthouseInheritedProperties, CourthouseAllProperties
    ] = CourthouseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Courthouse"
    return model


Courthouse = create_schema_org_model()


def create_courthouse_model(
    model: Union[
        CourthouseProperties, CourthouseInheritedProperties, CourthouseAllProperties
    ]
):
    _type = deepcopy(CourthouseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CourthouseAllProperties):
    pydantic_type = create_courthouse_model(model=model)
    return pydantic_type(model).schema_json()
