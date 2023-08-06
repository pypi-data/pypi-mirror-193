"""
A randomized trial design.

https://schema.org/RandomizedTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RandomizedTrialInheritedProperties(TypedDict):
    """A randomized trial design.

    References:
        https://schema.org/RandomizedTrial
    Note:
        Model Depth 6
    Attributes:
    """


class RandomizedTrialProperties(TypedDict):
    """A randomized trial design.

    References:
        https://schema.org/RandomizedTrial
    Note:
        Model Depth 6
    Attributes:
    """


class RandomizedTrialAllProperties(
    RandomizedTrialInheritedProperties, RandomizedTrialProperties, TypedDict
):
    pass


class RandomizedTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RandomizedTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RandomizedTrialProperties,
        RandomizedTrialInheritedProperties,
        RandomizedTrialAllProperties,
    ] = RandomizedTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RandomizedTrial"
    return model


RandomizedTrial = create_schema_org_model()


def create_randomizedtrial_model(
    model: Union[
        RandomizedTrialProperties,
        RandomizedTrialInheritedProperties,
        RandomizedTrialAllProperties,
    ]
):
    _type = deepcopy(RandomizedTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RandomizedTrialAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RandomizedTrialAllProperties):
    pydantic_type = create_randomizedtrial_model(model=model)
    return pydantic_type(model).schema_json()
