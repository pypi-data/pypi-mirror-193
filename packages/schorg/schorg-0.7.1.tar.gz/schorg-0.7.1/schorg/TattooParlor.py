"""
A tattoo parlor.

https://schema.org/TattooParlor
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TattooParlorInheritedProperties(TypedDict):
    """A tattoo parlor.

    References:
        https://schema.org/TattooParlor
    Note:
        Model Depth 5
    Attributes:
    """

    


class TattooParlorProperties(TypedDict):
    """A tattoo parlor.

    References:
        https://schema.org/TattooParlor
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(TattooParlorInheritedProperties , TattooParlorProperties, TypedDict):
    pass


class TattooParlorBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TattooParlor",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TattooParlorProperties, TattooParlorInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TattooParlor"
    return model
    

TattooParlor = create_schema_org_model()


def create_tattooparlor_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_tattooparlor_model(model=model)
    return pydantic_type(model).schema_json()


