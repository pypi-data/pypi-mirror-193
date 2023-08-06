"""
Indicates that parts of the legislation are in force, and parts are not.

https://schema.org/PartiallyInForce
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PartiallyInForceInheritedProperties(TypedDict):
    """Indicates that parts of the legislation are in force, and parts are not.

    References:
        https://schema.org/PartiallyInForce
    Note:
        Model Depth 6
    Attributes:
    """

    


class PartiallyInForceProperties(TypedDict):
    """Indicates that parts of the legislation are in force, and parts are not.

    References:
        https://schema.org/PartiallyInForce
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(PartiallyInForceInheritedProperties , PartiallyInForceProperties, TypedDict):
    pass


class PartiallyInForceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PartiallyInForce",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PartiallyInForceProperties, PartiallyInForceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PartiallyInForce"
    return model
    

PartiallyInForce = create_schema_org_model()


def create_partiallyinforce_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_partiallyinforce_model(model=model)
    return pydantic_type(model).schema_json()


