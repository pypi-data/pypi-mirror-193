"""
A pond.

https://schema.org/Pond
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PondInheritedProperties(TypedDict):
    """A pond.

    References:
        https://schema.org/Pond
    Note:
        Model Depth 5
    Attributes:
    """

    


class PondProperties(TypedDict):
    """A pond.

    References:
        https://schema.org/Pond
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PondInheritedProperties , PondProperties, TypedDict):
    pass


class PondBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Pond",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PondProperties, PondInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Pond"
    return model
    

Pond = create_schema_org_model()


def create_pond_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_pond_model(model=model)
    return pydantic_type(model).schema_json()


