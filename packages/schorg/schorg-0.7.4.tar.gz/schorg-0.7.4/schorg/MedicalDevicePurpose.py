"""
Categories of medical devices, organized by the purpose or intended use of the device.

https://schema.org/MedicalDevicePurpose
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalDevicePurposeInheritedProperties(TypedDict):
    """Categories of medical devices, organized by the purpose or intended use of the device.

    References:
        https://schema.org/MedicalDevicePurpose
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalDevicePurposeProperties(TypedDict):
    """Categories of medical devices, organized by the purpose or intended use of the device.

    References:
        https://schema.org/MedicalDevicePurpose
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalDevicePurposeAllProperties(
    MedicalDevicePurposeInheritedProperties, MedicalDevicePurposeProperties, TypedDict
):
    pass


class MedicalDevicePurposeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalDevicePurpose", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicalDevicePurposeProperties,
        MedicalDevicePurposeInheritedProperties,
        MedicalDevicePurposeAllProperties,
    ] = MedicalDevicePurposeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalDevicePurpose"
    return model


MedicalDevicePurpose = create_schema_org_model()


def create_medicaldevicepurpose_model(
    model: Union[
        MedicalDevicePurposeProperties,
        MedicalDevicePurposeInheritedProperties,
        MedicalDevicePurposeAllProperties,
    ]
):
    _type = deepcopy(MedicalDevicePurposeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalDevicePurposeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalDevicePurposeAllProperties):
    pydantic_type = create_medicaldevicepurpose_model(model=model)
    return pydantic_type(model).schema_json()
