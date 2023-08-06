"""
A prion is an infectious agent composed of protein in a misfolded form.

https://schema.org/Prion
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PrionInheritedProperties(TypedDict):
    """A prion is an infectious agent composed of protein in a misfolded form.

    References:
        https://schema.org/Prion
    Note:
        Model Depth 6
    Attributes:
    """

    


class PrionProperties(TypedDict):
    """A prion is an infectious agent composed of protein in a misfolded form.

    References:
        https://schema.org/Prion
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(PrionInheritedProperties , PrionProperties, TypedDict):
    pass


class PrionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Prion",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PrionProperties, PrionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Prion"
    return model
    

Prion = create_schema_org_model()


def create_prion_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_prion_model(model=model)
    return pydantic_type(model).schema_json()


