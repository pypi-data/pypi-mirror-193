"""
Positron emission tomography imaging.

https://schema.org/PET
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PETInheritedProperties(TypedDict):
    """Positron emission tomography imaging.

    References:
        https://schema.org/PET
    Note:
        Model Depth 6
    Attributes:
    """

    


class PETProperties(TypedDict):
    """Positron emission tomography imaging.

    References:
        https://schema.org/PET
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(PETInheritedProperties , PETProperties, TypedDict):
    pass


class PETBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PET",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PETProperties, PETInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PET"
    return model
    

PET = create_schema_org_model()


def create_pet_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_pet_model(model=model)
    return pydantic_type(model).schema_json()


