"""
A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.

https://schema.org/PlasticSurgery
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PlasticSurgeryInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.

    References:
        https://schema.org/PlasticSurgery
    Note:
        Model Depth 5
    Attributes:
    """

    


class PlasticSurgeryProperties(TypedDict):
    """A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.

    References:
        https://schema.org/PlasticSurgery
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PlasticSurgeryInheritedProperties , PlasticSurgeryProperties, TypedDict):
    pass


class PlasticSurgeryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PlasticSurgery",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PlasticSurgeryProperties, PlasticSurgeryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PlasticSurgery"
    return model
    

PlasticSurgery = create_schema_org_model()


def create_plasticsurgery_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_plasticsurgery_model(model=model)
    return pydantic_type(model).schema_json()


