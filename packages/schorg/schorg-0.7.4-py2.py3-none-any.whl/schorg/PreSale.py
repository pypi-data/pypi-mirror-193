"""
Indicates that the item is available for ordering and delivery before general availability.

https://schema.org/PreSale
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class PreSaleAllProperties(PreSaleInheritedProperties, PreSaleProperties, TypedDict):
    pass


class PreSaleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PreSale", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PreSaleProperties, PreSaleInheritedProperties, PreSaleAllProperties
    ] = PreSaleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PreSale"
    return model


PreSale = create_schema_org_model()


def create_presale_model(
    model: Union[PreSaleProperties, PreSaleInheritedProperties, PreSaleAllProperties]
):
    _type = deepcopy(PreSaleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PreSaleAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PreSaleAllProperties):
    pydantic_type = create_presale_model(model=model)
    return pydantic_type(model).schema_json()
