"""
Enumerates several types of return labels for product returns.

https://schema.org/ReturnLabelSourceEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnLabelSourceEnumerationInheritedProperties(TypedDict):
    """Enumerates several types of return labels for product returns.

    References:
        https://schema.org/ReturnLabelSourceEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ReturnLabelSourceEnumerationProperties(TypedDict):
    """Enumerates several types of return labels for product returns.

    References:
        https://schema.org/ReturnLabelSourceEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class ReturnLabelSourceEnumerationAllProperties(
    ReturnLabelSourceEnumerationInheritedProperties,
    ReturnLabelSourceEnumerationProperties,
    TypedDict,
):
    pass


class ReturnLabelSourceEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnLabelSourceEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReturnLabelSourceEnumerationProperties,
        ReturnLabelSourceEnumerationInheritedProperties,
        ReturnLabelSourceEnumerationAllProperties,
    ] = ReturnLabelSourceEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnLabelSourceEnumeration"
    return model


ReturnLabelSourceEnumeration = create_schema_org_model()


def create_returnlabelsourceenumeration_model(
    model: Union[
        ReturnLabelSourceEnumerationProperties,
        ReturnLabelSourceEnumerationInheritedProperties,
        ReturnLabelSourceEnumerationAllProperties,
    ]
):
    _type = deepcopy(ReturnLabelSourceEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReturnLabelSourceEnumerationAllProperties"
            )
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReturnLabelSourceEnumerationAllProperties):
    pydantic_type = create_returnlabelsourceenumeration_model(model=model)
    return pydantic_type(model).schema_json()
