"""
Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.

https://schema.org/LeisureTimeActivity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LeisureTimeActivityInheritedProperties(TypedDict):
    """Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.

    References:
        https://schema.org/LeisureTimeActivity
    Note:
        Model Depth 5
    Attributes:
    """


class LeisureTimeActivityProperties(TypedDict):
    """Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.

    References:
        https://schema.org/LeisureTimeActivity
    Note:
        Model Depth 5
    Attributes:
    """


class LeisureTimeActivityAllProperties(
    LeisureTimeActivityInheritedProperties, LeisureTimeActivityProperties, TypedDict
):
    pass


class LeisureTimeActivityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LeisureTimeActivity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LeisureTimeActivityProperties,
        LeisureTimeActivityInheritedProperties,
        LeisureTimeActivityAllProperties,
    ] = LeisureTimeActivityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LeisureTimeActivity"
    return model


LeisureTimeActivity = create_schema_org_model()


def create_leisuretimeactivity_model(
    model: Union[
        LeisureTimeActivityProperties,
        LeisureTimeActivityInheritedProperties,
        LeisureTimeActivityAllProperties,
    ]
):
    _type = deepcopy(LeisureTimeActivityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LeisureTimeActivity. Please see: https://schema.org/LeisureTimeActivity"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LeisureTimeActivityAllProperties):
    pydantic_type = create_leisuretimeactivity_model(model=model)
    return pydantic_type(model).schema_json()
