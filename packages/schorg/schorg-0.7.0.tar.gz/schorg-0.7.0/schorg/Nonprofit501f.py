"""
Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.

https://schema.org/Nonprofit501f
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501fInheritedProperties(TypedDict):
    """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.

    References:
        https://schema.org/Nonprofit501f
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501fProperties(TypedDict):
    """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.

    References:
        https://schema.org/Nonprofit501f
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501fInheritedProperties , Nonprofit501fProperties, TypedDict):
    pass


class Nonprofit501fBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501f",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501fProperties, Nonprofit501fInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501f"
    return model
    

Nonprofit501f = create_schema_org_model()


def create_nonprofit501f_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501f_model(model=model)
    return pydantic_type(model).schema_json()


