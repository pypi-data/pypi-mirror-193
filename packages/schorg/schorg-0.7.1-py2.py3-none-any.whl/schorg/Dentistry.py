"""
A branch of medicine that is involved in the dental care.

https://schema.org/Dentistry
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DentistryInheritedProperties(TypedDict):
    """A branch of medicine that is involved in the dental care.

    References:
        https://schema.org/Dentistry
    Note:
        Model Depth 6
    Attributes:
    """

    


class DentistryProperties(TypedDict):
    """A branch of medicine that is involved in the dental care.

    References:
        https://schema.org/Dentistry
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(DentistryInheritedProperties , DentistryProperties, TypedDict):
    pass


class DentistryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Dentistry",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DentistryProperties, DentistryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Dentistry"
    return model
    

Dentistry = create_schema_org_model()


def create_dentistry_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_dentistry_model(model=model)
    return pydantic_type(model).schema_json()


