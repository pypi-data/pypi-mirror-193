"""
The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.

https://schema.org/WesternConventional
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WesternConventionalInheritedProperties(TypedDict):
    """The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.

    References:
        https://schema.org/WesternConventional
    Note:
        Model Depth 6
    Attributes:
    """

    


class WesternConventionalProperties(TypedDict):
    """The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.

    References:
        https://schema.org/WesternConventional
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WesternConventionalInheritedProperties , WesternConventionalProperties, TypedDict):
    pass


class WesternConventionalBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WesternConventional",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WesternConventionalProperties, WesternConventionalInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WesternConventional"
    return model
    

WesternConventional = create_schema_org_model()


def create_westernconventional_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_westernconventional_model(model=model)
    return pydantic_type(model).schema_json()


