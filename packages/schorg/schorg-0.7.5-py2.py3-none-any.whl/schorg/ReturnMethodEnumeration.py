"""
Enumerates several types of product return methods.

https://schema.org/ReturnMethodEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnMethodEnumerationInheritedProperties(TypedDict):
    """Enumerates several types of product return methods.

    References:
        https://schema.org/ReturnMethodEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ReturnMethodEnumerationProperties(TypedDict):
    """Enumerates several types of product return methods.

    References:
        https://schema.org/ReturnMethodEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class ReturnMethodEnumerationAllProperties(
    ReturnMethodEnumerationInheritedProperties,
    ReturnMethodEnumerationProperties,
    TypedDict,
):
    pass


class ReturnMethodEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnMethodEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReturnMethodEnumerationProperties,
        ReturnMethodEnumerationInheritedProperties,
        ReturnMethodEnumerationAllProperties,
    ] = ReturnMethodEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnMethodEnumeration"
    return model


ReturnMethodEnumeration = create_schema_org_model()


def create_returnmethodenumeration_model(
    model: Union[
        ReturnMethodEnumerationProperties,
        ReturnMethodEnumerationInheritedProperties,
        ReturnMethodEnumerationAllProperties,
    ]
):
    _type = deepcopy(ReturnMethodEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReturnMethodEnumeration. Please see: https://schema.org/ReturnMethodEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReturnMethodEnumerationAllProperties):
    pydantic_type = create_returnmethodenumeration_model(model=model)
    return pydantic_type(model).schema_json()
