"""
An aggregate rating of an Organization related to its role as an employer.

https://schema.org/EmployerAggregateRating
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EmployerAggregateRatingInheritedProperties(TypedDict):
    """An aggregate rating of an Organization related to its role as an employer.

    References:
        https://schema.org/EmployerAggregateRating
    Note:
        Model Depth 5
    Attributes:
        itemReviewed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The item that is being reviewed/rated.
        ratingCount: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The count of total number of ratings.
        reviewCount: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The count of total number of reviews.
    """

    itemReviewed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ratingCount: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    reviewCount: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    


class EmployerAggregateRatingProperties(TypedDict):
    """An aggregate rating of an Organization related to its role as an employer.

    References:
        https://schema.org/EmployerAggregateRating
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(EmployerAggregateRatingInheritedProperties , EmployerAggregateRatingProperties, TypedDict):
    pass


class EmployerAggregateRatingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EmployerAggregateRating",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'itemReviewed': {'exclude': True}}
        fields = {'ratingCount': {'exclude': True}}
        fields = {'reviewCount': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EmployerAggregateRatingProperties, EmployerAggregateRatingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EmployerAggregateRating"
    return model
    

EmployerAggregateRating = create_schema_org_model()


def create_employeraggregaterating_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_employeraggregaterating_model(model=model)
    return pydantic_type(model).schema_json()


