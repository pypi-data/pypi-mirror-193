"""
Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections.

https://schema.org/Infectious
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InfectiousInheritedProperties(TypedDict):
    """Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections.

    References:
        https://schema.org/Infectious
    Note:
        Model Depth 6
    Attributes:
    """

    


class InfectiousProperties(TypedDict):
    """Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections.

    References:
        https://schema.org/Infectious
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(InfectiousInheritedProperties , InfectiousProperties, TypedDict):
    pass


class InfectiousBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Infectious",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[InfectiousProperties, InfectiousInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Infectious"
    return model
    

Infectious = create_schema_org_model()


def create_infectious_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_infectious_model(model=model)
    return pydantic_type(model).schema_json()


