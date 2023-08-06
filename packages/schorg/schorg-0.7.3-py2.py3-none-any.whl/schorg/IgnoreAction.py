"""
The act of intentionally disregarding the object. An agent ignores an object.

https://schema.org/IgnoreAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class IgnoreActionInheritedProperties(TypedDict):
    """The act of intentionally disregarding the object. An agent ignores an object.

    References:
        https://schema.org/IgnoreAction
    Note:
        Model Depth 4
    Attributes:
    """


class IgnoreActionProperties(TypedDict):
    """The act of intentionally disregarding the object. An agent ignores an object.

    References:
        https://schema.org/IgnoreAction
    Note:
        Model Depth 4
    Attributes:
    """


class IgnoreActionAllProperties(
    IgnoreActionInheritedProperties, IgnoreActionProperties, TypedDict
):
    pass


class IgnoreActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="IgnoreAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        IgnoreActionProperties,
        IgnoreActionInheritedProperties,
        IgnoreActionAllProperties,
    ] = IgnoreActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "IgnoreAction"
    return model


IgnoreAction = create_schema_org_model()


def create_ignoreaction_model(
    model: Union[
        IgnoreActionProperties,
        IgnoreActionInheritedProperties,
        IgnoreActionAllProperties,
    ]
):
    _type = deepcopy(IgnoreActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: IgnoreActionAllProperties):
    pydantic_type = create_ignoreaction_model(model=model)
    return pydantic_type(model).schema_json()
