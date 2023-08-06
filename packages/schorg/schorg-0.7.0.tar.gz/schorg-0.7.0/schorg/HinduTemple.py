"""
A Hindu temple.

https://schema.org/HinduTemple
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HinduTempleInheritedProperties(TypedDict):
    """A Hindu temple.

    References:
        https://schema.org/HinduTemple
    Note:
        Model Depth 5
    Attributes:
    """

    


class HinduTempleProperties(TypedDict):
    """A Hindu temple.

    References:
        https://schema.org/HinduTemple
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HinduTempleInheritedProperties , HinduTempleProperties, TypedDict):
    pass


class HinduTempleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HinduTemple",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HinduTempleProperties, HinduTempleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HinduTemple"
    return model
    

HinduTemple = create_schema_org_model()


def create_hindutemple_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hindutemple_model(model=model)
    return pydantic_type(model).schema_json()


