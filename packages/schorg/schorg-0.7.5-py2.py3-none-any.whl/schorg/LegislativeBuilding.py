"""
A legislative building&#x2014;for example, the state capitol.

https://schema.org/LegislativeBuilding
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LegislativeBuildingInheritedProperties(TypedDict):
    """A legislative building&#x2014;for example, the state capitol.

    References:
        https://schema.org/LegislativeBuilding
    Note:
        Model Depth 5
    Attributes:
    """


class LegislativeBuildingProperties(TypedDict):
    """A legislative building&#x2014;for example, the state capitol.

    References:
        https://schema.org/LegislativeBuilding
    Note:
        Model Depth 5
    Attributes:
    """


class LegislativeBuildingAllProperties(
    LegislativeBuildingInheritedProperties, LegislativeBuildingProperties, TypedDict
):
    pass


class LegislativeBuildingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LegislativeBuilding", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LegislativeBuildingProperties,
        LegislativeBuildingInheritedProperties,
        LegislativeBuildingAllProperties,
    ] = LegislativeBuildingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LegislativeBuilding"
    return model


LegislativeBuilding = create_schema_org_model()


def create_legislativebuilding_model(
    model: Union[
        LegislativeBuildingProperties,
        LegislativeBuildingInheritedProperties,
        LegislativeBuildingAllProperties,
    ]
):
    _type = deepcopy(LegislativeBuildingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LegislativeBuilding. Please see: https://schema.org/LegislativeBuilding"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LegislativeBuildingAllProperties):
    pydantic_type = create_legislativebuilding_model(model=model)
    return pydantic_type(model).schema_json()
