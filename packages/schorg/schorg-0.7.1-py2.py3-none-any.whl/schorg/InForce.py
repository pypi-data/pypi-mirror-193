"""
Indicates that a legislation is in force.

https://schema.org/InForce
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InForceInheritedProperties(TypedDict):
    """Indicates that a legislation is in force.

    References:
        https://schema.org/InForce
    Note:
        Model Depth 6
    Attributes:
    """

    


class InForceProperties(TypedDict):
    """Indicates that a legislation is in force.

    References:
        https://schema.org/InForce
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(InForceInheritedProperties , InForceProperties, TypedDict):
    pass


class InForceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InForce",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[InForceProperties, InForceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InForce"
    return model
    

InForce = create_schema_org_model()


def create_inforce_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_inforce_model(model=model)
    return pydantic_type(model).schema_json()


