"""
A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.

https://schema.org/Rheumatologic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RheumatologicInheritedProperties(TypedDict):
    """A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.

    References:
        https://schema.org/Rheumatologic
    Note:
        Model Depth 6
    Attributes:
    """

    


class RheumatologicProperties(TypedDict):
    """A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.

    References:
        https://schema.org/Rheumatologic
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(RheumatologicInheritedProperties , RheumatologicProperties, TypedDict):
    pass


class RheumatologicBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Rheumatologic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RheumatologicProperties, RheumatologicInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Rheumatologic"
    return model
    

Rheumatologic = create_schema_org_model()


def create_rheumatologic_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_rheumatologic_model(model=model)
    return pydantic_type(model).schema_json()


