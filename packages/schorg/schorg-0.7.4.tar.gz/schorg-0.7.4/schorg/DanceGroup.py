"""
A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

https://schema.org/DanceGroup
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DanceGroupInheritedProperties(TypedDict):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    References:
        https://schema.org/DanceGroup
    Note:
        Model Depth 4
    Attributes:
    """


class DanceGroupProperties(TypedDict):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    References:
        https://schema.org/DanceGroup
    Note:
        Model Depth 4
    Attributes:
    """


class DanceGroupAllProperties(
    DanceGroupInheritedProperties, DanceGroupProperties, TypedDict
):
    pass


class DanceGroupBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DanceGroup", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DanceGroupProperties, DanceGroupInheritedProperties, DanceGroupAllProperties
    ] = DanceGroupAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DanceGroup"
    return model


DanceGroup = create_schema_org_model()


def create_dancegroup_model(
    model: Union[
        DanceGroupProperties, DanceGroupInheritedProperties, DanceGroupAllProperties
    ]
):
    _type = deepcopy(DanceGroupAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DanceGroupAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DanceGroupAllProperties):
    pydantic_type = create_dancegroup_model(model=model)
    return pydantic_type(model).schema_json()
