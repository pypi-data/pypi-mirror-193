"""
Residence type: Gated community.

https://schema.org/GatedResidenceCommunity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GatedResidenceCommunityInheritedProperties(TypedDict):
    """Residence type: Gated community.

    References:
        https://schema.org/GatedResidenceCommunity
    Note:
        Model Depth 4
    Attributes:
        accommodationFloorPlan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A floorplan of some [[Accommodation]].
    """

    accommodationFloorPlan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class GatedResidenceCommunityProperties(TypedDict):
    """Residence type: Gated community.

    References:
        https://schema.org/GatedResidenceCommunity
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(GatedResidenceCommunityInheritedProperties , GatedResidenceCommunityProperties, TypedDict):
    pass


class GatedResidenceCommunityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GatedResidenceCommunity",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'accommodationFloorPlan': {'exclude': True}}
        


def create_schema_org_model(type_: Union[GatedResidenceCommunityProperties, GatedResidenceCommunityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GatedResidenceCommunity"
    return model
    

GatedResidenceCommunity = create_schema_org_model()


def create_gatedresidencecommunity_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_gatedresidencecommunity_model(model=model)
    return pydantic_type(model).schema_json()


