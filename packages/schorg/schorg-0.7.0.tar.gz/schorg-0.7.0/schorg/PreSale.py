"""
Indicates that the item is available for ordering and delivery before general availability.

https://schema.org/PreSale
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PreSaleInheritedProperties(TypedDict):
    """Indicates that the item is available for ordering and delivery before general availability.

    References:
        https://schema.org/PreSale
    Note:
        Model Depth 5
    Attributes:
    """

    


class PreSaleProperties(TypedDict):
    """Indicates that the item is available for ordering and delivery before general availability.

    References:
        https://schema.org/PreSale
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PreSaleInheritedProperties , PreSaleProperties, TypedDict):
    pass


class PreSaleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PreSale",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PreSaleProperties, PreSaleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PreSale"
    return model
    

PreSale = create_schema_org_model()


def create_presale_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_presale_model(model=model)
    return pydantic_type(model).schema_json()


