"""
Enumerates different price types, for example list price, invoice price, and sale price.

https://schema.org/PriceTypeEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PriceTypeEnumerationInheritedProperties(TypedDict):
    """Enumerates different price types, for example list price, invoice price, and sale price.

    References:
        https://schema.org/PriceTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PriceTypeEnumerationProperties(TypedDict):
    """Enumerates different price types, for example list price, invoice price, and sale price.

    References:
        https://schema.org/PriceTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class PriceTypeEnumerationAllProperties(
    PriceTypeEnumerationInheritedProperties, PriceTypeEnumerationProperties, TypedDict
):
    pass


class PriceTypeEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PriceTypeEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PriceTypeEnumerationProperties,
        PriceTypeEnumerationInheritedProperties,
        PriceTypeEnumerationAllProperties,
    ] = PriceTypeEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PriceTypeEnumeration"
    return model


PriceTypeEnumeration = create_schema_org_model()


def create_pricetypeenumeration_model(
    model: Union[
        PriceTypeEnumerationProperties,
        PriceTypeEnumerationInheritedProperties,
        PriceTypeEnumerationAllProperties,
    ]
):
    _type = deepcopy(PriceTypeEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PriceTypeEnumerationAllProperties):
    pydantic_type = create_pricetypeenumeration_model(model=model)
    return pydantic_type(model).schema_json()
