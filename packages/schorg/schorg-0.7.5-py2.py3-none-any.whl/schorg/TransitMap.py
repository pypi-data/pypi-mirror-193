"""
A transit map.

https://schema.org/TransitMap
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TransitMapInheritedProperties(TypedDict):
    """A transit map.

    References:
        https://schema.org/TransitMap
    Note:
        Model Depth 5
    Attributes:
    """


class TransitMapProperties(TypedDict):
    """A transit map.

    References:
        https://schema.org/TransitMap
    Note:
        Model Depth 5
    Attributes:
    """


class TransitMapAllProperties(
    TransitMapInheritedProperties, TransitMapProperties, TypedDict
):
    pass


class TransitMapBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TransitMap", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TransitMapProperties, TransitMapInheritedProperties, TransitMapAllProperties
    ] = TransitMapAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TransitMap"
    return model


TransitMap = create_schema_org_model()


def create_transitmap_model(
    model: Union[
        TransitMapProperties, TransitMapInheritedProperties, TransitMapAllProperties
    ]
):
    _type = deepcopy(TransitMapAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TransitMap. Please see: https://schema.org/TransitMap"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TransitMapAllProperties):
    pydantic_type = create_transitmap_model(model=model)
    return pydantic_type(model).schema_json()
