"""
Branch of medicine that pertains to the health services to improve and protect community health, especially epidemiology, sanitation, immunization, and preventive medicine.

https://schema.org/PublicHealth
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PublicHealthInheritedProperties(TypedDict):
    """Branch of medicine that pertains to the health services to improve and protect community health, especially epidemiology, sanitation, immunization, and preventive medicine.

    References:
        https://schema.org/PublicHealth
    Note:
        Model Depth 5
    Attributes:
    """

    


class PublicHealthProperties(TypedDict):
    """Branch of medicine that pertains to the health services to improve and protect community health, especially epidemiology, sanitation, immunization, and preventive medicine.

    References:
        https://schema.org/PublicHealth
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PublicHealthInheritedProperties , PublicHealthProperties, TypedDict):
    pass


class PublicHealthBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PublicHealth",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PublicHealthProperties, PublicHealthInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PublicHealth"
    return model
    

PublicHealth = create_schema_org_model()


def create_publichealth_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_publichealth_model(model=model)
    return pydantic_type(model).schema_json()


