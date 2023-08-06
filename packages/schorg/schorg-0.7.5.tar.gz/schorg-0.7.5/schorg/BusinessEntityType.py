"""
A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.Commonly used values:* http://purl.org/goodrelations/v1#Business* http://purl.org/goodrelations/v1#Enduser* http://purl.org/goodrelations/v1#PublicInstitution* http://purl.org/goodrelations/v1#Reseller	  

https://schema.org/BusinessEntityType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class BusinessEntityTypeAllProperties(
    BusinessEntityTypeInheritedProperties, BusinessEntityTypeProperties, TypedDict
):
    pass


class BusinessEntityTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BusinessEntityType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BusinessEntityTypeProperties,
        BusinessEntityTypeInheritedProperties,
        BusinessEntityTypeAllProperties,
    ] = BusinessEntityTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BusinessEntityType"
    return model


BusinessEntityType = create_schema_org_model()


def create_businessentitytype_model(
    model: Union[
        BusinessEntityTypeProperties,
        BusinessEntityTypeInheritedProperties,
        BusinessEntityTypeAllProperties,
    ]
):
    _type = deepcopy(BusinessEntityTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BusinessEntityType. Please see: https://schema.org/BusinessEntityType"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BusinessEntityTypeAllProperties):
    pydantic_type = create_businessentitytype_model(model=model)
    return pydantic_type(model).schema_json()
