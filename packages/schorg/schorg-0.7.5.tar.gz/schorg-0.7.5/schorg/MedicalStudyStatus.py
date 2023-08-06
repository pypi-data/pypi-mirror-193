"""
The status of a medical study. Enumerated type.

https://schema.org/MedicalStudyStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalStudyStatusInheritedProperties(TypedDict):
    """The status of a medical study. Enumerated type.

    References:
        https://schema.org/MedicalStudyStatus
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalStudyStatusProperties(TypedDict):
    """The status of a medical study. Enumerated type.

    References:
        https://schema.org/MedicalStudyStatus
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalStudyStatusAllProperties(
    MedicalStudyStatusInheritedProperties, MedicalStudyStatusProperties, TypedDict
):
    pass


class MedicalStudyStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalStudyStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicalStudyStatusProperties,
        MedicalStudyStatusInheritedProperties,
        MedicalStudyStatusAllProperties,
    ] = MedicalStudyStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalStudyStatus"
    return model


MedicalStudyStatus = create_schema_org_model()


def create_medicalstudystatus_model(
    model: Union[
        MedicalStudyStatusProperties,
        MedicalStudyStatusInheritedProperties,
        MedicalStudyStatusAllProperties,
    ]
):
    _type = deepcopy(MedicalStudyStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MedicalStudyStatus. Please see: https://schema.org/MedicalStudyStatus"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MedicalStudyStatusAllProperties):
    pydantic_type = create_medicalstudystatus_model(model=model)
    return pydantic_type(model).schema_json()
