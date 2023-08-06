"""
The airline boards by groups based on check-in time, priority, etc.

https://schema.org/GroupBoardingPolicy
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GroupBoardingPolicyInheritedProperties(TypedDict):
    """The airline boards by groups based on check-in time, priority, etc.

    References:
        https://schema.org/GroupBoardingPolicy
    Note:
        Model Depth 5
    Attributes:
    """

    


class GroupBoardingPolicyProperties(TypedDict):
    """The airline boards by groups based on check-in time, priority, etc.

    References:
        https://schema.org/GroupBoardingPolicy
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(GroupBoardingPolicyInheritedProperties , GroupBoardingPolicyProperties, TypedDict):
    pass


class GroupBoardingPolicyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GroupBoardingPolicy",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[GroupBoardingPolicyProperties, GroupBoardingPolicyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GroupBoardingPolicy"
    return model
    

GroupBoardingPolicy = create_schema_org_model()


def create_groupboardingpolicy_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_groupboardingpolicy_model(model=model)
    return pydantic_type(model).schema_json()


