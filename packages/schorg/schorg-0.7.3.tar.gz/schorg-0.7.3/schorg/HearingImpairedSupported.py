"""
Uses devices to support users with hearing impairments.

https://schema.org/HearingImpairedSupported
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HearingImpairedSupportedInheritedProperties(TypedDict):
    """Uses devices to support users with hearing impairments.

    References:
        https://schema.org/HearingImpairedSupported
    Note:
        Model Depth 5
    Attributes:
    """


class HearingImpairedSupportedProperties(TypedDict):
    """Uses devices to support users with hearing impairments.

    References:
        https://schema.org/HearingImpairedSupported
    Note:
        Model Depth 5
    Attributes:
    """


class HearingImpairedSupportedAllProperties(
    HearingImpairedSupportedInheritedProperties,
    HearingImpairedSupportedProperties,
    TypedDict,
):
    pass


class HearingImpairedSupportedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HearingImpairedSupported", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HearingImpairedSupportedProperties,
        HearingImpairedSupportedInheritedProperties,
        HearingImpairedSupportedAllProperties,
    ] = HearingImpairedSupportedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HearingImpairedSupported"
    return model


HearingImpairedSupported = create_schema_org_model()


def create_hearingimpairedsupported_model(
    model: Union[
        HearingImpairedSupportedProperties,
        HearingImpairedSupportedInheritedProperties,
        HearingImpairedSupportedAllProperties,
    ]
):
    _type = deepcopy(HearingImpairedSupportedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HearingImpairedSupportedAllProperties):
    pydantic_type = create_hearingimpairedsupported_model(model=model)
    return pydantic_type(model).schema_json()
