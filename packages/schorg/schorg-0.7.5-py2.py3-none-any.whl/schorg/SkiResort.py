"""
A ski resort.

https://schema.org/SkiResort
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SkiResortInheritedProperties(TypedDict):
    """A ski resort.

    References:
        https://schema.org/SkiResort
    Note:
        Model Depth 5
    Attributes:
    """


class SkiResortProperties(TypedDict):
    """A ski resort.

    References:
        https://schema.org/SkiResort
    Note:
        Model Depth 5
    Attributes:
    """


class SkiResortAllProperties(
    SkiResortInheritedProperties, SkiResortProperties, TypedDict
):
    pass


class SkiResortBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SkiResort", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SkiResortProperties, SkiResortInheritedProperties, SkiResortAllProperties
    ] = SkiResortAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SkiResort"
    return model


SkiResort = create_schema_org_model()


def create_skiresort_model(
    model: Union[
        SkiResortProperties, SkiResortInheritedProperties, SkiResortAllProperties
    ]
):
    _type = deepcopy(SkiResortAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SkiResort. Please see: https://schema.org/SkiResort"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SkiResortAllProperties):
    pydantic_type = create_skiresort_model(model=model)
    return pydantic_type(model).schema_json()
