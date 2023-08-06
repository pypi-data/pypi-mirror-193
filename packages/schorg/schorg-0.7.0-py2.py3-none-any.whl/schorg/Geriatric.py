"""
A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.

https://schema.org/Geriatric
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GeriatricInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.

    References:
        https://schema.org/Geriatric
    Note:
        Model Depth 5
    Attributes:
    """

    


class GeriatricProperties(TypedDict):
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.

    References:
        https://schema.org/Geriatric
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(GeriatricInheritedProperties , GeriatricProperties, TypedDict):
    pass


class GeriatricBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Geriatric",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[GeriatricProperties, GeriatricInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Geriatric"
    return model
    

Geriatric = create_schema_org_model()


def create_geriatric_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_geriatric_model(model=model)
    return pydantic_type(model).schema_json()


