"""
Specifies that the customer must pay the return shipping costs when returning a product.

https://schema.org/ReturnShippingFees
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnShippingFeesInheritedProperties(TypedDict):
    """Specifies that the customer must pay the return shipping costs when returning a product.

    References:
        https://schema.org/ReturnShippingFees
    Note:
        Model Depth 5
    Attributes:
    """

    


class ReturnShippingFeesProperties(TypedDict):
    """Specifies that the customer must pay the return shipping costs when returning a product.

    References:
        https://schema.org/ReturnShippingFees
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReturnShippingFeesInheritedProperties , ReturnShippingFeesProperties, TypedDict):
    pass


class ReturnShippingFeesBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReturnShippingFees",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReturnShippingFeesProperties, ReturnShippingFeesInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnShippingFees"
    return model
    

ReturnShippingFees = create_schema_org_model()


def create_returnshippingfees_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_returnshippingfees_model(model=model)
    return pydantic_type(model).schema_json()


