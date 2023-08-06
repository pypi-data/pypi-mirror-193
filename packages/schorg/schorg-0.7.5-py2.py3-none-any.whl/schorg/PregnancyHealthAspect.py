"""
Content discussing pregnancy-related aspects of a health topic.

https://schema.org/PregnancyHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PregnancyHealthAspectInheritedProperties(TypedDict):
    """Content discussing pregnancy-related aspects of a health topic.

    References:
        https://schema.org/PregnancyHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class PregnancyHealthAspectProperties(TypedDict):
    """Content discussing pregnancy-related aspects of a health topic.

    References:
        https://schema.org/PregnancyHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class PregnancyHealthAspectAllProperties(
    PregnancyHealthAspectInheritedProperties, PregnancyHealthAspectProperties, TypedDict
):
    pass


class PregnancyHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PregnancyHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PregnancyHealthAspectProperties,
        PregnancyHealthAspectInheritedProperties,
        PregnancyHealthAspectAllProperties,
    ] = PregnancyHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PregnancyHealthAspect"
    return model


PregnancyHealthAspect = create_schema_org_model()


def create_pregnancyhealthaspect_model(
    model: Union[
        PregnancyHealthAspectProperties,
        PregnancyHealthAspectInheritedProperties,
        PregnancyHealthAspectAllProperties,
    ]
):
    _type = deepcopy(PregnancyHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PregnancyHealthAspect. Please see: https://schema.org/PregnancyHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PregnancyHealthAspectAllProperties):
    pydantic_type = create_pregnancyhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
