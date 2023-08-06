"""
A venue map (e.g. for malls, auditoriums, museums, etc.).

https://schema.org/VenueMap
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VenueMapInheritedProperties(TypedDict):
    """A venue map (e.g. for malls, auditoriums, museums, etc.).

    References:
        https://schema.org/VenueMap
    Note:
        Model Depth 5
    Attributes:
    """


class VenueMapProperties(TypedDict):
    """A venue map (e.g. for malls, auditoriums, museums, etc.).

    References:
        https://schema.org/VenueMap
    Note:
        Model Depth 5
    Attributes:
    """


class VenueMapAllProperties(VenueMapInheritedProperties, VenueMapProperties, TypedDict):
    pass


class VenueMapBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="VenueMap", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        VenueMapProperties, VenueMapInheritedProperties, VenueMapAllProperties
    ] = VenueMapAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VenueMap"
    return model


VenueMap = create_schema_org_model()


def create_venuemap_model(
    model: Union[VenueMapProperties, VenueMapInheritedProperties, VenueMapAllProperties]
):
    _type = deepcopy(VenueMapAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: VenueMapAllProperties):
    pydantic_type = create_venuemap_model(model=model)
    return pydantic_type(model).schema_json()
