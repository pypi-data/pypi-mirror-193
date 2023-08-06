"""
Nonprofit527: Non-profit type referring to political organizations.

https://schema.org/Nonprofit527
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit527InheritedProperties(TypedDict):
    """Nonprofit527: Non-profit type referring to political organizations.

    References:
        https://schema.org/Nonprofit527
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit527Properties(TypedDict):
    """Nonprofit527: Non-profit type referring to political organizations.

    References:
        https://schema.org/Nonprofit527
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit527InheritedProperties , Nonprofit527Properties, TypedDict):
    pass


class Nonprofit527BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit527",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit527Properties, Nonprofit527InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit527"
    return model
    

Nonprofit527 = create_schema_org_model()


def create_nonprofit527_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit527_model(model=model)
    return pydantic_type(model).schema_json()


