"""
Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.

https://schema.org/Clinician
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ClinicianInheritedProperties(TypedDict):
    """Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.

    References:
        https://schema.org/Clinician
    Note:
        Model Depth 6
    Attributes:
    """


class ClinicianProperties(TypedDict):
    """Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.

    References:
        https://schema.org/Clinician
    Note:
        Model Depth 6
    Attributes:
    """


class ClinicianAllProperties(
    ClinicianInheritedProperties, ClinicianProperties, TypedDict
):
    pass


class ClinicianBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Clinician", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ClinicianProperties, ClinicianInheritedProperties, ClinicianAllProperties
    ] = ClinicianAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Clinician"
    return model


Clinician = create_schema_org_model()


def create_clinician_model(
    model: Union[
        ClinicianProperties, ClinicianInheritedProperties, ClinicianAllProperties
    ]
):
    _type = deepcopy(ClinicianAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Clinician. Please see: https://schema.org/Clinician"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ClinicianAllProperties):
    pydantic_type = create_clinician_model(model=model)
    return pydantic_type(model).schema_json()
