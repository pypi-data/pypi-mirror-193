"""
A venue map (e.g. for malls, auditoriums, museums, etc.).

https://schema.org/VenueMap
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(VenueMapInheritedProperties , VenueMapProperties, TypedDict):
    pass


class VenueMapBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VenueMap",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[VenueMapProperties, VenueMapInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VenueMap"
    return model
    

VenueMap = create_schema_org_model()


def create_venuemap_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_venuemap_model(model=model)
    return pydantic_type(model).schema_json()


