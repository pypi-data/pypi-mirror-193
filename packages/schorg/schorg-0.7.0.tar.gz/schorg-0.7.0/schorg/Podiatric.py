"""
Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.

https://schema.org/Podiatric
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PodiatricInheritedProperties(TypedDict):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.

    References:
        https://schema.org/Podiatric
    Note:
        Model Depth 5
    Attributes:
    """

    


class PodiatricProperties(TypedDict):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.

    References:
        https://schema.org/Podiatric
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PodiatricInheritedProperties , PodiatricProperties, TypedDict):
    pass


class PodiatricBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Podiatric",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PodiatricProperties, PodiatricInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Podiatric"
    return model
    

Podiatric = create_schema_org_model()


def create_podiatric_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_podiatric_model(model=model)
    return pydantic_type(model).schema_json()


