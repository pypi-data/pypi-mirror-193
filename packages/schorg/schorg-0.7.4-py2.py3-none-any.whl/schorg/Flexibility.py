"""
Physical activity that is engaged in to improve joint and muscle flexibility.

https://schema.org/Flexibility
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FlexibilityInheritedProperties(TypedDict):
    """Physical activity that is engaged in to improve joint and muscle flexibility.

    References:
        https://schema.org/Flexibility
    Note:
        Model Depth 5
    Attributes:
    """


class FlexibilityProperties(TypedDict):
    """Physical activity that is engaged in to improve joint and muscle flexibility.

    References:
        https://schema.org/Flexibility
    Note:
        Model Depth 5
    Attributes:
    """


class FlexibilityAllProperties(
    FlexibilityInheritedProperties, FlexibilityProperties, TypedDict
):
    pass


class FlexibilityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Flexibility", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FlexibilityProperties, FlexibilityInheritedProperties, FlexibilityAllProperties
    ] = FlexibilityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Flexibility"
    return model


Flexibility = create_schema_org_model()


def create_flexibility_model(
    model: Union[
        FlexibilityProperties, FlexibilityInheritedProperties, FlexibilityAllProperties
    ]
):
    _type = deepcopy(FlexibilityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FlexibilityAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FlexibilityAllProperties):
    pydantic_type = create_flexibility_model(model=model)
    return pydantic_type(model).schema_json()
