"""
The airline boards by zones of the plane.

https://schema.org/ZoneBoardingPolicy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ZoneBoardingPolicyInheritedProperties(TypedDict):
    """The airline boards by zones of the plane.

    References:
        https://schema.org/ZoneBoardingPolicy
    Note:
        Model Depth 5
    Attributes:
    """


class ZoneBoardingPolicyProperties(TypedDict):
    """The airline boards by zones of the plane.

    References:
        https://schema.org/ZoneBoardingPolicy
    Note:
        Model Depth 5
    Attributes:
    """


class ZoneBoardingPolicyAllProperties(
    ZoneBoardingPolicyInheritedProperties, ZoneBoardingPolicyProperties, TypedDict
):
    pass


class ZoneBoardingPolicyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ZoneBoardingPolicy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ZoneBoardingPolicyProperties,
        ZoneBoardingPolicyInheritedProperties,
        ZoneBoardingPolicyAllProperties,
    ] = ZoneBoardingPolicyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ZoneBoardingPolicy"
    return model


ZoneBoardingPolicy = create_schema_org_model()


def create_zoneboardingpolicy_model(
    model: Union[
        ZoneBoardingPolicyProperties,
        ZoneBoardingPolicyInheritedProperties,
        ZoneBoardingPolicyAllProperties,
    ]
):
    _type = deepcopy(ZoneBoardingPolicyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ZoneBoardingPolicyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ZoneBoardingPolicyAllProperties):
    pydantic_type = create_zoneboardingpolicy_model(model=model)
    return pydantic_type(model).schema_json()
