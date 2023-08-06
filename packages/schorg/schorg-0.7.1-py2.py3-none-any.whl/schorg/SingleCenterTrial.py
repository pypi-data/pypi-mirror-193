"""
A trial that takes place at a single center.

https://schema.org/SingleCenterTrial
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SingleCenterTrialInheritedProperties(TypedDict):
    """A trial that takes place at a single center.

    References:
        https://schema.org/SingleCenterTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class SingleCenterTrialProperties(TypedDict):
    """A trial that takes place at a single center.

    References:
        https://schema.org/SingleCenterTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(SingleCenterTrialInheritedProperties , SingleCenterTrialProperties, TypedDict):
    pass


class SingleCenterTrialBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SingleCenterTrial",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SingleCenterTrialProperties, SingleCenterTrialInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SingleCenterTrial"
    return model
    

SingleCenterTrial = create_schema_org_model()


def create_singlecentertrial_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_singlecentertrial_model(model=model)
    return pydantic_type(model).schema_json()


