"""
The airline boards by zones of the plane.

https://schema.org/ZoneBoardingPolicy
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ZoneBoardingPolicyInheritedProperties , ZoneBoardingPolicyProperties, TypedDict):
    pass


class ZoneBoardingPolicyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ZoneBoardingPolicy",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ZoneBoardingPolicyProperties, ZoneBoardingPolicyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ZoneBoardingPolicy"
    return model
    

ZoneBoardingPolicy = create_schema_org_model()


def create_zoneboardingpolicy_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_zoneboardingpolicy_model(model=model)
    return pydantic_type(model).schema_json()


