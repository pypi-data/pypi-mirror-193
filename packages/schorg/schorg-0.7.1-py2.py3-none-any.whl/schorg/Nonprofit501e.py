"""
Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

https://schema.org/Nonprofit501e
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501eInheritedProperties(TypedDict):
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

    References:
        https://schema.org/Nonprofit501e
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501eProperties(TypedDict):
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

    References:
        https://schema.org/Nonprofit501e
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501eInheritedProperties , Nonprofit501eProperties, TypedDict):
    pass


class Nonprofit501eBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501e",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501eProperties, Nonprofit501eInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501e"
    return model
    

Nonprofit501e = create_schema_org_model()


def create_nonprofit501e_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501e_model(model=model)
    return pydantic_type(model).schema_json()


