"""
Multicellular parasite that causes an infection.

https://schema.org/MulticellularParasite
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MulticellularParasiteInheritedProperties(TypedDict):
    """Multicellular parasite that causes an infection.

    References:
        https://schema.org/MulticellularParasite
    Note:
        Model Depth 6
    Attributes:
    """

    


class MulticellularParasiteProperties(TypedDict):
    """Multicellular parasite that causes an infection.

    References:
        https://schema.org/MulticellularParasite
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(MulticellularParasiteInheritedProperties , MulticellularParasiteProperties, TypedDict):
    pass


class MulticellularParasiteBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MulticellularParasite",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MulticellularParasiteProperties, MulticellularParasiteInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MulticellularParasite"
    return model
    

MulticellularParasite = create_schema_org_model()


def create_multicellularparasite_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_multicellularparasite_model(model=model)
    return pydantic_type(model).schema_json()


