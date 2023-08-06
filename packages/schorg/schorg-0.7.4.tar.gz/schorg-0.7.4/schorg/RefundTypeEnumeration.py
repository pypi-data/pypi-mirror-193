"""
Enumerates several kinds of product return refund types.

https://schema.org/RefundTypeEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RefundTypeEnumerationInheritedProperties(TypedDict):
    """Enumerates several kinds of product return refund types.

    References:
        https://schema.org/RefundTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class RefundTypeEnumerationProperties(TypedDict):
    """Enumerates several kinds of product return refund types.

    References:
        https://schema.org/RefundTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class RefundTypeEnumerationAllProperties(
    RefundTypeEnumerationInheritedProperties, RefundTypeEnumerationProperties, TypedDict
):
    pass


class RefundTypeEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RefundTypeEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RefundTypeEnumerationProperties,
        RefundTypeEnumerationInheritedProperties,
        RefundTypeEnumerationAllProperties,
    ] = RefundTypeEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RefundTypeEnumeration"
    return model


RefundTypeEnumeration = create_schema_org_model()


def create_refundtypeenumeration_model(
    model: Union[
        RefundTypeEnumerationProperties,
        RefundTypeEnumerationInheritedProperties,
        RefundTypeEnumerationAllProperties,
    ]
):
    _type = deepcopy(RefundTypeEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RefundTypeEnumerationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RefundTypeEnumerationAllProperties):
    pydantic_type = create_refundtypeenumeration_model(model=model)
    return pydantic_type(model).schema_json()
