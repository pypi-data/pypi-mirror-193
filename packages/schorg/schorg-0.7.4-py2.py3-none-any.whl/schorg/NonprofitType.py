"""
NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.

https://schema.org/NonprofitType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NonprofitTypeInheritedProperties(TypedDict):
    """NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.

    References:
        https://schema.org/NonprofitType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class NonprofitTypeProperties(TypedDict):
    """NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.

    References:
        https://schema.org/NonprofitType
    Note:
        Model Depth 4
    Attributes:
    """


class NonprofitTypeAllProperties(
    NonprofitTypeInheritedProperties, NonprofitTypeProperties, TypedDict
):
    pass


class NonprofitTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NonprofitType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        NonprofitTypeProperties,
        NonprofitTypeInheritedProperties,
        NonprofitTypeAllProperties,
    ] = NonprofitTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NonprofitType"
    return model


NonprofitType = create_schema_org_model()


def create_nonprofittype_model(
    model: Union[
        NonprofitTypeProperties,
        NonprofitTypeInheritedProperties,
        NonprofitTypeAllProperties,
    ]
):
    _type = deepcopy(NonprofitTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of NonprofitTypeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NonprofitTypeAllProperties):
    pydantic_type = create_nonprofittype_model(model=model)
    return pydantic_type(model).schema_json()
