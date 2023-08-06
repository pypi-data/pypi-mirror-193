"""
A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.

https://schema.org/Gynecologic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GynecologicInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.

    References:
        https://schema.org/Gynecologic
    Note:
        Model Depth 5
    Attributes:
    """

    


class GynecologicProperties(TypedDict):
    """A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.

    References:
        https://schema.org/Gynecologic
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(GynecologicInheritedProperties , GynecologicProperties, TypedDict):
    pass


class GynecologicBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Gynecologic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[GynecologicProperties, GynecologicInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Gynecologic"
    return model
    

Gynecologic = create_schema_org_model()


def create_gynecologic_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_gynecologic_model(model=model)
    return pydantic_type(model).schema_json()


