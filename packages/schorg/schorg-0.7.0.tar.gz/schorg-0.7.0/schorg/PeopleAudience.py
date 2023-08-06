"""
A set of characteristics belonging to people, e.g. who compose an item's target audience.

https://schema.org/PeopleAudience
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PeopleAudienceInheritedProperties(TypedDict):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    References:
        https://schema.org/PeopleAudience
    Note:
        Model Depth 4
    Attributes:
        audienceType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area associated with the audience.
    """

    audienceType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    geographicArea: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class PeopleAudienceProperties(TypedDict):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    References:
        https://schema.org/PeopleAudience
    Note:
        Model Depth 4
    Attributes:
        healthCondition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifying the health condition(s) of a patient, medical study, or other target audience.
        requiredGender: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Audiences defined by a person's gender.
        suggestedMinAge: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): Minimum recommended age in years for the audience or user.
        requiredMinAge: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): Audiences defined by a person's minimum age.
        suggestedMeasurement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
        suggestedGender: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
        requiredMaxAge: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): Audiences defined by a person's maximum age.
        suggestedAge: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
        suggestedMaxAge: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): Maximum recommended age in years for the audience or user.
    """

    healthCondition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    requiredGender: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    suggestedMinAge: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    requiredMinAge: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    suggestedMeasurement: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    suggestedGender: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    requiredMaxAge: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    suggestedAge: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    suggestedMaxAge: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class AllProperties(PeopleAudienceInheritedProperties , PeopleAudienceProperties, TypedDict):
    pass


class PeopleAudienceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PeopleAudience",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'audienceType': {'exclude': True}}
        fields = {'geographicArea': {'exclude': True}}
        fields = {'healthCondition': {'exclude': True}}
        fields = {'requiredGender': {'exclude': True}}
        fields = {'suggestedMinAge': {'exclude': True}}
        fields = {'requiredMinAge': {'exclude': True}}
        fields = {'suggestedMeasurement': {'exclude': True}}
        fields = {'suggestedGender': {'exclude': True}}
        fields = {'requiredMaxAge': {'exclude': True}}
        fields = {'suggestedAge': {'exclude': True}}
        fields = {'suggestedMaxAge': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PeopleAudienceProperties, PeopleAudienceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PeopleAudience"
    return model
    

PeopleAudience = create_schema_org_model()


def create_peopleaudience_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_peopleaudience_model(model=model)
    return pydantic_type(model).schema_json()


