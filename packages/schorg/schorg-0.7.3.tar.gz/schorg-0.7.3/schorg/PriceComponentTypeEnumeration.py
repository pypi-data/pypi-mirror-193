"""
Enumerates different price components that together make up the total price for an offered product.

https://schema.org/PriceComponentTypeEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PriceComponentTypeEnumerationInheritedProperties(TypedDict):
    """Enumerates different price components that together make up the total price for an offered product.

    References:
        https://schema.org/PriceComponentTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PriceComponentTypeEnumerationProperties(TypedDict):
    """Enumerates different price components that together make up the total price for an offered product.

    References:
        https://schema.org/PriceComponentTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class PriceComponentTypeEnumerationAllProperties(
    PriceComponentTypeEnumerationInheritedProperties,
    PriceComponentTypeEnumerationProperties,
    TypedDict,
):
    pass


class PriceComponentTypeEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PriceComponentTypeEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PriceComponentTypeEnumerationProperties,
        PriceComponentTypeEnumerationInheritedProperties,
        PriceComponentTypeEnumerationAllProperties,
    ] = PriceComponentTypeEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PriceComponentTypeEnumeration"
    return model


PriceComponentTypeEnumeration = create_schema_org_model()


def create_pricecomponenttypeenumeration_model(
    model: Union[
        PriceComponentTypeEnumerationProperties,
        PriceComponentTypeEnumerationInheritedProperties,
        PriceComponentTypeEnumerationAllProperties,
    ]
):
    _type = deepcopy(PriceComponentTypeEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PriceComponentTypeEnumerationAllProperties):
    pydantic_type = create_pricecomponenttypeenumeration_model(model=model)
    return pydantic_type(model).schema_json()
