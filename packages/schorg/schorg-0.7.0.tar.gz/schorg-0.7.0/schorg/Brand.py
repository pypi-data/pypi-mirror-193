"""
A brand is a name used by an organization or business person for labeling a product, product group, or similar.

https://schema.org/Brand
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BrandInheritedProperties(TypedDict):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar.

    References:
        https://schema.org/Brand
    Note:
        Model Depth 3
    Attributes:
    """

    


class BrandProperties(TypedDict):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar.

    References:
        https://schema.org/Brand
    Note:
        Model Depth 3
    Attributes:
        slogan: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A slogan or motto associated with the item.
        review: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A review of the item.
        logo: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): An associated logo.
        aggregateRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The overall rating, based on a collection of reviews or ratings, of the item.
    """

    slogan: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    review: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    logo: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    aggregateRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(BrandInheritedProperties , BrandProperties, TypedDict):
    pass


class BrandBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Brand",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'slogan': {'exclude': True}}
        fields = {'review': {'exclude': True}}
        fields = {'logo': {'exclude': True}}
        fields = {'aggregateRating': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BrandProperties, BrandInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Brand"
    return model
    

Brand = create_schema_org_model()


def create_brand_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_brand_model(model=model)
    return pydantic_type(model).schema_json()


