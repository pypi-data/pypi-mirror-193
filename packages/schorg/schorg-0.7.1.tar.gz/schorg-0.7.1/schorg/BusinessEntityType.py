"""
A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.Commonly used values:* http://purl.org/goodrelations/v1#Business* http://purl.org/goodrelations/v1#Enduser* http://purl.org/goodrelations/v1#PublicInstitution* http://purl.org/goodrelations/v1#Reseller	  

https://schema.org/BusinessEntityType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BusinessEntityTypeInheritedProperties(TypedDict):
    """A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.Commonly used values:* http://purl.org/goodrelations/v1#Business* http://purl.org/goodrelations/v1#Enduser* http://purl.org/goodrelations/v1#PublicInstitution* http://purl.org/goodrelations/v1#Reseller	  

    References:
        https://schema.org/BusinessEntityType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class BusinessEntityTypeProperties(TypedDict):
    """A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.Commonly used values:* http://purl.org/goodrelations/v1#Business* http://purl.org/goodrelations/v1#Enduser* http://purl.org/goodrelations/v1#PublicInstitution* http://purl.org/goodrelations/v1#Reseller	  

    References:
        https://schema.org/BusinessEntityType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(BusinessEntityTypeInheritedProperties , BusinessEntityTypeProperties, TypedDict):
    pass


class BusinessEntityTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BusinessEntityType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BusinessEntityTypeProperties, BusinessEntityTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BusinessEntityType"
    return model
    

BusinessEntityType = create_schema_org_model()


def create_businessentitytype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_businessentitytype_model(model=model)
    return pydantic_type(model).schema_json()


