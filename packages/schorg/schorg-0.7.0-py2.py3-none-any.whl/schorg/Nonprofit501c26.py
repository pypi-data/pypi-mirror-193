"""
Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage for High-Risk Individuals.

https://schema.org/Nonprofit501c26
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c26InheritedProperties(TypedDict):
    """Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage for High-Risk Individuals.

    References:
        https://schema.org/Nonprofit501c26
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501c26Properties(TypedDict):
    """Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage for High-Risk Individuals.

    References:
        https://schema.org/Nonprofit501c26
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501c26InheritedProperties , Nonprofit501c26Properties, TypedDict):
    pass


class Nonprofit501c26BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501c26",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501c26Properties, Nonprofit501c26InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c26"
    return model
    

Nonprofit501c26 = create_schema_org_model()


def create_nonprofit501c26_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501c26_model(model=model)
    return pydantic_type(model).schema_json()


