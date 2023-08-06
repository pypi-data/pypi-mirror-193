"""
Nonprofit501n: Non-profit type referring to Charitable Risk Pools.

https://schema.org/Nonprofit501n
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501nInheritedProperties(TypedDict):
    """Nonprofit501n: Non-profit type referring to Charitable Risk Pools.

    References:
        https://schema.org/Nonprofit501n
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501nProperties(TypedDict):
    """Nonprofit501n: Non-profit type referring to Charitable Risk Pools.

    References:
        https://schema.org/Nonprofit501n
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501nInheritedProperties , Nonprofit501nProperties, TypedDict):
    pass


class Nonprofit501nBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501n",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501nProperties, Nonprofit501nInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501n"
    return model
    

Nonprofit501n = create_schema_org_model()


def create_nonprofit501n_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501n_model(model=model)
    return pydantic_type(model).schema_json()


