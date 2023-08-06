"""
Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

https://schema.org/Nonprofit501a
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501aInheritedProperties(TypedDict):
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

    References:
        https://schema.org/Nonprofit501a
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501aProperties(TypedDict):
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

    References:
        https://schema.org/Nonprofit501a
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501aInheritedProperties , Nonprofit501aProperties, TypedDict):
    pass


class Nonprofit501aBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501a",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501aProperties, Nonprofit501aInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501a"
    return model
    

Nonprofit501a = create_schema_org_model()


def create_nonprofit501a_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501a_model(model=model)
    return pydantic_type(model).schema_json()


