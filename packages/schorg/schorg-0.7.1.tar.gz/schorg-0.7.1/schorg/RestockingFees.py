"""
Specifies that the customer must pay a restocking fee when returning a product.

https://schema.org/RestockingFees
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RestockingFeesInheritedProperties(TypedDict):
    """Specifies that the customer must pay a restocking fee when returning a product.

    References:
        https://schema.org/RestockingFees
    Note:
        Model Depth 5
    Attributes:
    """

    


class RestockingFeesProperties(TypedDict):
    """Specifies that the customer must pay a restocking fee when returning a product.

    References:
        https://schema.org/RestockingFees
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(RestockingFeesInheritedProperties , RestockingFeesProperties, TypedDict):
    pass


class RestockingFeesBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RestockingFees",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RestockingFeesProperties, RestockingFeesInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RestockingFees"
    return model
    

RestockingFees = create_schema_org_model()


def create_restockingfees_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_restockingfees_model(model=model)
    return pydantic_type(model).schema_json()


