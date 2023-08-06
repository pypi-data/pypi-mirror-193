"""
Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.

https://schema.org/MinimumAdvertisedPrice
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MinimumAdvertisedPriceInheritedProperties(TypedDict):
    """Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.

    References:
        https://schema.org/MinimumAdvertisedPrice
    Note:
        Model Depth 5
    Attributes:
    """

    


class MinimumAdvertisedPriceProperties(TypedDict):
    """Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.

    References:
        https://schema.org/MinimumAdvertisedPrice
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MinimumAdvertisedPriceInheritedProperties , MinimumAdvertisedPriceProperties, TypedDict):
    pass


class MinimumAdvertisedPriceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MinimumAdvertisedPrice",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MinimumAdvertisedPriceProperties, MinimumAdvertisedPriceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MinimumAdvertisedPrice"
    return model
    

MinimumAdvertisedPrice = create_schema_org_model()


def create_minimumadvertisedprice_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_minimumadvertisedprice_model(model=model)
    return pydantic_type(model).schema_json()


