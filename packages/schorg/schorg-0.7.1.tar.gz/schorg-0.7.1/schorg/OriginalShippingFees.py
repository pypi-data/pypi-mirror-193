"""
Specifies that the customer must pay the original shipping costs when returning a product.

https://schema.org/OriginalShippingFees
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OriginalShippingFeesInheritedProperties(TypedDict):
    """Specifies that the customer must pay the original shipping costs when returning a product.

    References:
        https://schema.org/OriginalShippingFees
    Note:
        Model Depth 5
    Attributes:
    """

    


class OriginalShippingFeesProperties(TypedDict):
    """Specifies that the customer must pay the original shipping costs when returning a product.

    References:
        https://schema.org/OriginalShippingFees
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(OriginalShippingFeesInheritedProperties , OriginalShippingFeesProperties, TypedDict):
    pass


class OriginalShippingFeesBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OriginalShippingFees",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OriginalShippingFeesProperties, OriginalShippingFeesInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OriginalShippingFees"
    return model
    

OriginalShippingFees = create_schema_org_model()


def create_originalshippingfees_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_originalshippingfees_model(model=model)
    return pydantic_type(model).schema_json()


