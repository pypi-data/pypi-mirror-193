"""
Information about how or where to find a topic. Also may contain location data that can be used for where to look for help if the topic is observed.

https://schema.org/HowOrWhereHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HowOrWhereHealthAspectInheritedProperties(TypedDict):
    """Information about how or where to find a topic. Also may contain location data that can be used for where to look for help if the topic is observed.

    References:
        https://schema.org/HowOrWhereHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class HowOrWhereHealthAspectProperties(TypedDict):
    """Information about how or where to find a topic. Also may contain location data that can be used for where to look for help if the topic is observed.

    References:
        https://schema.org/HowOrWhereHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class HowOrWhereHealthAspectAllProperties(
    HowOrWhereHealthAspectInheritedProperties,
    HowOrWhereHealthAspectProperties,
    TypedDict,
):
    pass


class HowOrWhereHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HowOrWhereHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HowOrWhereHealthAspectProperties,
        HowOrWhereHealthAspectInheritedProperties,
        HowOrWhereHealthAspectAllProperties,
    ] = HowOrWhereHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HowOrWhereHealthAspect"
    return model


HowOrWhereHealthAspect = create_schema_org_model()


def create_howorwherehealthaspect_model(
    model: Union[
        HowOrWhereHealthAspectProperties,
        HowOrWhereHealthAspectInheritedProperties,
        HowOrWhereHealthAspectAllProperties,
    ]
):
    _type = deepcopy(HowOrWhereHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HowOrWhereHealthAspect. Please see: https://schema.org/HowOrWhereHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HowOrWhereHealthAspectAllProperties):
    pydantic_type = create_howorwherehealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
