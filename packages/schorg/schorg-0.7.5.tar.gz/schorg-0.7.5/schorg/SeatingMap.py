"""
A seating map.

https://schema.org/SeatingMap
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SeatingMapInheritedProperties(TypedDict):
    """A seating map.

    References:
        https://schema.org/SeatingMap
    Note:
        Model Depth 5
    Attributes:
    """


class SeatingMapProperties(TypedDict):
    """A seating map.

    References:
        https://schema.org/SeatingMap
    Note:
        Model Depth 5
    Attributes:
    """


class SeatingMapAllProperties(
    SeatingMapInheritedProperties, SeatingMapProperties, TypedDict
):
    pass


class SeatingMapBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SeatingMap", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SeatingMapProperties, SeatingMapInheritedProperties, SeatingMapAllProperties
    ] = SeatingMapAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SeatingMap"
    return model


SeatingMap = create_schema_org_model()


def create_seatingmap_model(
    model: Union[
        SeatingMapProperties, SeatingMapInheritedProperties, SeatingMapAllProperties
    ]
):
    _type = deepcopy(SeatingMapAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SeatingMap. Please see: https://schema.org/SeatingMap"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SeatingMapAllProperties):
    pydantic_type = create_seatingmap_model(model=model)
    return pydantic_type(model).schema_json()
