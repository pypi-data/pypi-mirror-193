"""
The act of discovering/finding an object.

https://schema.org/DiscoverAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DiscoverActionInheritedProperties(TypedDict):
    """The act of discovering/finding an object.

    References:
        https://schema.org/DiscoverAction
    Note:
        Model Depth 4
    Attributes:
    """


class DiscoverActionProperties(TypedDict):
    """The act of discovering/finding an object.

    References:
        https://schema.org/DiscoverAction
    Note:
        Model Depth 4
    Attributes:
    """


class DiscoverActionAllProperties(
    DiscoverActionInheritedProperties, DiscoverActionProperties, TypedDict
):
    pass


class DiscoverActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DiscoverAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DiscoverActionProperties,
        DiscoverActionInheritedProperties,
        DiscoverActionAllProperties,
    ] = DiscoverActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DiscoverAction"
    return model


DiscoverAction = create_schema_org_model()


def create_discoveraction_model(
    model: Union[
        DiscoverActionProperties,
        DiscoverActionInheritedProperties,
        DiscoverActionAllProperties,
    ]
):
    _type = deepcopy(DiscoverActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DiscoverActionAllProperties):
    pydantic_type = create_discoveraction_model(model=model)
    return pydantic_type(model).schema_json()
