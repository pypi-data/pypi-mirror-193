"""
An enumeration that describes different types of medical procedures.

https://schema.org/MedicalProcedureType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalProcedureTypeInheritedProperties(TypedDict):
    """An enumeration that describes different types of medical procedures.

    References:
        https://schema.org/MedicalProcedureType
    Note:
        Model Depth 5
    Attributes:
    """

    


class MedicalProcedureTypeProperties(TypedDict):
    """An enumeration that describes different types of medical procedures.

    References:
        https://schema.org/MedicalProcedureType
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalProcedureTypeInheritedProperties , MedicalProcedureTypeProperties, TypedDict):
    pass


class MedicalProcedureTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalProcedureType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalProcedureTypeProperties, MedicalProcedureTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalProcedureType"
    return model
    

MedicalProcedureType = create_schema_org_model()


def create_medicalproceduretype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalproceduretype_model(model=model)
    return pydantic_type(model).schema_json()


