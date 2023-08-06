"""
A randomized trial design.

https://schema.org/RandomizedTrial
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(RandomizedTrialInheritedProperties , RandomizedTrialProperties, TypedDict):
    pass


class RandomizedTrialBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RandomizedTrial",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RandomizedTrialProperties, RandomizedTrialInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RandomizedTrial"
    return model
    

RandomizedTrial = create_schema_org_model()


def create_randomizedtrial_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_randomizedtrial_model(model=model)
    return pydantic_type(model).schema_json()


