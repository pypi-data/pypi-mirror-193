"""
An enumeration that describes different types of medical procedures.

https://schema.org/MedicalProcedureType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class MedicalProcedureTypeAllProperties(
    MedicalProcedureTypeInheritedProperties, MedicalProcedureTypeProperties, TypedDict
):
    pass


class MedicalProcedureTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalProcedureType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicalProcedureTypeProperties,
        MedicalProcedureTypeInheritedProperties,
        MedicalProcedureTypeAllProperties,
    ] = MedicalProcedureTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalProcedureType"
    return model


MedicalProcedureType = create_schema_org_model()


def create_medicalproceduretype_model(
    model: Union[
        MedicalProcedureTypeProperties,
        MedicalProcedureTypeInheritedProperties,
        MedicalProcedureTypeAllProperties,
    ]
):
    _type = deepcopy(MedicalProcedureTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MedicalProcedureType. Please see: https://schema.org/MedicalProcedureType"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MedicalProcedureTypeAllProperties):
    pydantic_type = create_medicalproceduretype_model(model=model)
    return pydantic_type(model).schema_json()
