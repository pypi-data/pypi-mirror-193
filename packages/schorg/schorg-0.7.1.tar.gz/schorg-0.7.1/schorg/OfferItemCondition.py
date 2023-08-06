"""
A list of possible conditions for the item.

https://schema.org/OfferItemCondition
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfferItemConditionInheritedProperties(TypedDict):
    """A list of possible conditions for the item.

    References:
        https://schema.org/OfferItemCondition
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class OfferItemConditionProperties(TypedDict):
    """A list of possible conditions for the item.

    References:
        https://schema.org/OfferItemCondition
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(OfferItemConditionInheritedProperties , OfferItemConditionProperties, TypedDict):
    pass


class OfferItemConditionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OfferItemCondition",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[OfferItemConditionProperties, OfferItemConditionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfferItemCondition"
    return model
    

OfferItemCondition = create_schema_org_model()


def create_offeritemcondition_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_offeritemcondition_model(model=model)
    return pydantic_type(model).schema_json()


