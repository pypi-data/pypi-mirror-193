"""
An indication for preventing an underlying condition, symptom, etc.

https://schema.org/PreventionIndication
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PreventionIndicationInheritedProperties(TypedDict):
    """An indication for preventing an underlying condition, symptom, etc.

    References:
        https://schema.org/PreventionIndication
    Note:
        Model Depth 4
    Attributes:
    """

    


class PreventionIndicationProperties(TypedDict):
    """An indication for preventing an underlying condition, symptom, etc.

    References:
        https://schema.org/PreventionIndication
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(PreventionIndicationInheritedProperties , PreventionIndicationProperties, TypedDict):
    pass


class PreventionIndicationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PreventionIndication",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PreventionIndicationProperties, PreventionIndicationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PreventionIndication"
    return model
    

PreventionIndication = create_schema_org_model()


def create_preventionindication_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_preventionindication_model(model=model)
    return pydantic_type(model).schema_json()


