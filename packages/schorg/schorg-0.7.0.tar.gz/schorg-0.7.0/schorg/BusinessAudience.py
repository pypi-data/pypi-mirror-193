"""
A set of characteristics belonging to businesses, e.g. who compose an item's target audience.

https://schema.org/BusinessAudience
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BusinessAudienceInheritedProperties(TypedDict):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target audience.

    References:
        https://schema.org/BusinessAudience
    Note:
        Model Depth 4
    Attributes:
        audienceType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area associated with the audience.
    """

    audienceType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    geographicArea: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class BusinessAudienceProperties(TypedDict):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target audience.

    References:
        https://schema.org/BusinessAudience
    Note:
        Model Depth 4
    Attributes:
        yearlyRevenue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The size of the business in annual revenue.
        numberOfEmployees: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of employees in an organization, e.g. business.
        yearsInOperation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The age of the business.
    """

    yearlyRevenue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfEmployees: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    yearsInOperation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(BusinessAudienceInheritedProperties , BusinessAudienceProperties, TypedDict):
    pass


class BusinessAudienceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BusinessAudience",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'audienceType': {'exclude': True}}
        fields = {'geographicArea': {'exclude': True}}
        fields = {'yearlyRevenue': {'exclude': True}}
        fields = {'numberOfEmployees': {'exclude': True}}
        fields = {'yearsInOperation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BusinessAudienceProperties, BusinessAudienceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BusinessAudience"
    return model
    

BusinessAudience = create_schema_org_model()


def create_businessaudience_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_businessaudience_model(model=model)
    return pydantic_type(model).schema_json()


