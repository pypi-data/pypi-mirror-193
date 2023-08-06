"""
Information about the risk factors and possible complications that may follow a topic.

https://schema.org/RisksOrComplicationsHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RisksOrComplicationsHealthAspectInheritedProperties(TypedDict):
    """Information about the risk factors and possible complications that may follow a topic.

    References:
        https://schema.org/RisksOrComplicationsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class RisksOrComplicationsHealthAspectProperties(TypedDict):
    """Information about the risk factors and possible complications that may follow a topic.

    References:
        https://schema.org/RisksOrComplicationsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class RisksOrComplicationsHealthAspectAllProperties(
    RisksOrComplicationsHealthAspectInheritedProperties,
    RisksOrComplicationsHealthAspectProperties,
    TypedDict,
):
    pass


class RisksOrComplicationsHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RisksOrComplicationsHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RisksOrComplicationsHealthAspectProperties,
        RisksOrComplicationsHealthAspectInheritedProperties,
        RisksOrComplicationsHealthAspectAllProperties,
    ] = RisksOrComplicationsHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RisksOrComplicationsHealthAspect"
    return model


RisksOrComplicationsHealthAspect = create_schema_org_model()


def create_risksorcomplicationshealthaspect_model(
    model: Union[
        RisksOrComplicationsHealthAspectProperties,
        RisksOrComplicationsHealthAspectInheritedProperties,
        RisksOrComplicationsHealthAspectAllProperties,
    ]
):
    _type = deepcopy(RisksOrComplicationsHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of RisksOrComplicationsHealthAspect. Please see: https://schema.org/RisksOrComplicationsHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: RisksOrComplicationsHealthAspectAllProperties):
    pydantic_type = create_risksorcomplicationshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
