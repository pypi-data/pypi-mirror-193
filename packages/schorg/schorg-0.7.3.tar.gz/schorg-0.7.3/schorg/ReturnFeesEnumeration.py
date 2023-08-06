"""
Enumerates several kinds of policies for product return fees.

https://schema.org/ReturnFeesEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnFeesEnumerationInheritedProperties(TypedDict):
    """Enumerates several kinds of policies for product return fees.

    References:
        https://schema.org/ReturnFeesEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ReturnFeesEnumerationProperties(TypedDict):
    """Enumerates several kinds of policies for product return fees.

    References:
        https://schema.org/ReturnFeesEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class ReturnFeesEnumerationAllProperties(
    ReturnFeesEnumerationInheritedProperties, ReturnFeesEnumerationProperties, TypedDict
):
    pass


class ReturnFeesEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnFeesEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReturnFeesEnumerationProperties,
        ReturnFeesEnumerationInheritedProperties,
        ReturnFeesEnumerationAllProperties,
    ] = ReturnFeesEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnFeesEnumeration"
    return model


ReturnFeesEnumeration = create_schema_org_model()


def create_returnfeesenumeration_model(
    model: Union[
        ReturnFeesEnumerationProperties,
        ReturnFeesEnumerationInheritedProperties,
        ReturnFeesEnumerationAllProperties,
    ]
):
    _type = deepcopy(ReturnFeesEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReturnFeesEnumerationAllProperties):
    pydantic_type = create_returnfeesenumeration_model(model=model)
    return pydantic_type(model).schema_json()
