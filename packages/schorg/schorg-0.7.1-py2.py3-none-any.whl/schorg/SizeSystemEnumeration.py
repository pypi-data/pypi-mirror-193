"""
Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.

https://schema.org/SizeSystemEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SizeSystemEnumerationInheritedProperties(TypedDict):
    """Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.

    References:
        https://schema.org/SizeSystemEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class SizeSystemEnumerationProperties(TypedDict):
    """Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.

    References:
        https://schema.org/SizeSystemEnumeration
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(SizeSystemEnumerationInheritedProperties , SizeSystemEnumerationProperties, TypedDict):
    pass


class SizeSystemEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SizeSystemEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[SizeSystemEnumerationProperties, SizeSystemEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SizeSystemEnumeration"
    return model
    

SizeSystemEnumeration = create_schema_org_model()


def create_sizesystemenumeration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_sizesystemenumeration_model(model=model)
    return pydantic_type(model).schema_json()


