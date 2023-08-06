"""
Systems of medical practice.

https://schema.org/MedicineSystem
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicineSystemInheritedProperties(TypedDict):
    """Systems of medical practice.

    References:
        https://schema.org/MedicineSystem
    Note:
        Model Depth 5
    Attributes:
    """


class MedicineSystemProperties(TypedDict):
    """Systems of medical practice.

    References:
        https://schema.org/MedicineSystem
    Note:
        Model Depth 5
    Attributes:
    """


class MedicineSystemAllProperties(
    MedicineSystemInheritedProperties, MedicineSystemProperties, TypedDict
):
    pass


class MedicineSystemBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicineSystem", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicineSystemProperties,
        MedicineSystemInheritedProperties,
        MedicineSystemAllProperties,
    ] = MedicineSystemAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicineSystem"
    return model


MedicineSystem = create_schema_org_model()


def create_medicinesystem_model(
    model: Union[
        MedicineSystemProperties,
        MedicineSystemInheritedProperties,
        MedicineSystemAllProperties,
    ]
):
    _type = deepcopy(MedicineSystemAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicineSystemAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicineSystemAllProperties):
    pydantic_type = create_medicinesystem_model(model=model)
    return pydantic_type(model).schema_json()
