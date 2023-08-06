"""
A tennis complex.

https://schema.org/TennisComplex
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TennisComplexInheritedProperties(TypedDict):
    """A tennis complex.

    References:
        https://schema.org/TennisComplex
    Note:
        Model Depth 5
    Attributes:
    """

    


class TennisComplexProperties(TypedDict):
    """A tennis complex.

    References:
        https://schema.org/TennisComplex
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(TennisComplexInheritedProperties , TennisComplexProperties, TypedDict):
    pass


class TennisComplexBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TennisComplex",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TennisComplexProperties, TennisComplexInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TennisComplex"
    return model
    

TennisComplex = create_schema_org_model()


def create_tenniscomplex_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_tenniscomplex_model(model=model)
    return pydantic_type(model).schema_json()


