"""
Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

https://schema.org/OccupationalExperienceRequirements
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OccupationalExperienceRequirementsInheritedProperties(TypedDict):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    References:
        https://schema.org/OccupationalExperienceRequirements
    Note:
        Model Depth 3
    Attributes:
    """

    


class OccupationalExperienceRequirementsProperties(TypedDict):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    References:
        https://schema.org/OccupationalExperienceRequirements
    Note:
        Model Depth 3
    Attributes:
        monthsOfExperience: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): Indicates the minimal number of months of experience required for a position.
    """

    monthsOfExperience: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class AllProperties(OccupationalExperienceRequirementsInheritedProperties , OccupationalExperienceRequirementsProperties, TypedDict):
    pass


class OccupationalExperienceRequirementsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OccupationalExperienceRequirements",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'monthsOfExperience': {'exclude': True}}
        


def create_schema_org_model(type_: Union[OccupationalExperienceRequirementsProperties, OccupationalExperienceRequirementsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OccupationalExperienceRequirements"
    return model
    

OccupationalExperienceRequirements = create_schema_org_model()


def create_occupationalexperiencerequirements_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_occupationalexperiencerequirements_model(model=model)
    return pydantic_type(model).schema_json()


