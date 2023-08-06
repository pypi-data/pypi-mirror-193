"""
A trial that takes place at multiple centers.

https://schema.org/MultiCenterTrial
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MultiCenterTrialInheritedProperties(TypedDict):
    """A trial that takes place at multiple centers.

    References:
        https://schema.org/MultiCenterTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class MultiCenterTrialProperties(TypedDict):
    """A trial that takes place at multiple centers.

    References:
        https://schema.org/MultiCenterTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(MultiCenterTrialInheritedProperties , MultiCenterTrialProperties, TypedDict):
    pass


class MultiCenterTrialBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MultiCenterTrial",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MultiCenterTrialProperties, MultiCenterTrialInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MultiCenterTrial"
    return model
    

MultiCenterTrial = create_schema_org_model()


def create_multicentertrial_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_multicentertrial_model(model=model)
    return pydantic_type(model).schema_json()


