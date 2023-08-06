"""
Information about coping or life related to the topic.

https://schema.org/LivingWithHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LivingWithHealthAspectInheritedProperties(TypedDict):
    """Information about coping or life related to the topic.

    References:
        https://schema.org/LivingWithHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class LivingWithHealthAspectProperties(TypedDict):
    """Information about coping or life related to the topic.

    References:
        https://schema.org/LivingWithHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class LivingWithHealthAspectAllProperties(
    LivingWithHealthAspectInheritedProperties,
    LivingWithHealthAspectProperties,
    TypedDict,
):
    pass


class LivingWithHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LivingWithHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LivingWithHealthAspectProperties,
        LivingWithHealthAspectInheritedProperties,
        LivingWithHealthAspectAllProperties,
    ] = LivingWithHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LivingWithHealthAspect"
    return model


LivingWithHealthAspect = create_schema_org_model()


def create_livingwithhealthaspect_model(
    model: Union[
        LivingWithHealthAspectProperties,
        LivingWithHealthAspectInheritedProperties,
        LivingWithHealthAspectAllProperties,
    ]
):
    _type = deepcopy(LivingWithHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LivingWithHealthAspect. Please see: https://schema.org/LivingWithHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LivingWithHealthAspectAllProperties):
    pydantic_type = create_livingwithhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
