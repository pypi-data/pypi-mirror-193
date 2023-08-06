"""
The airline boards by groups based on check-in time, priority, etc.

https://schema.org/GroupBoardingPolicy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class GroupBoardingPolicyAllProperties(
    GroupBoardingPolicyInheritedProperties, GroupBoardingPolicyProperties, TypedDict
):
    pass


class GroupBoardingPolicyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GroupBoardingPolicy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GroupBoardingPolicyProperties,
        GroupBoardingPolicyInheritedProperties,
        GroupBoardingPolicyAllProperties,
    ] = GroupBoardingPolicyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GroupBoardingPolicy"
    return model


GroupBoardingPolicy = create_schema_org_model()


def create_groupboardingpolicy_model(
    model: Union[
        GroupBoardingPolicyProperties,
        GroupBoardingPolicyInheritedProperties,
        GroupBoardingPolicyAllProperties,
    ]
):
    _type = deepcopy(GroupBoardingPolicyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GroupBoardingPolicy. Please see: https://schema.org/GroupBoardingPolicy"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GroupBoardingPolicyAllProperties):
    pydantic_type = create_groupboardingpolicy_model(model=model)
    return pydantic_type(model).schema_json()
