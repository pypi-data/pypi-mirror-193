"""
Content about the benefits and advantages of usage or utilization of topic.

https://schema.org/BenefitsHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BenefitsHealthAspectInheritedProperties(TypedDict):
    """Content about the benefits and advantages of usage or utilization of topic.

    References:
        https://schema.org/BenefitsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class BenefitsHealthAspectProperties(TypedDict):
    """Content about the benefits and advantages of usage or utilization of topic.

    References:
        https://schema.org/BenefitsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(BenefitsHealthAspectInheritedProperties , BenefitsHealthAspectProperties, TypedDict):
    pass


class BenefitsHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BenefitsHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BenefitsHealthAspectProperties, BenefitsHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BenefitsHealthAspect"
    return model
    

BenefitsHealthAspect = create_schema_org_model()


def create_benefitshealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_benefitshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


