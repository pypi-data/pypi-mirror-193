"""
Available by prescription only.

https://schema.org/PrescriptionOnly
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PrescriptionOnlyInheritedProperties(TypedDict):
    """Available by prescription only.

    References:
        https://schema.org/PrescriptionOnly
    Note:
        Model Depth 6
    Attributes:
    """


class PrescriptionOnlyProperties(TypedDict):
    """Available by prescription only.

    References:
        https://schema.org/PrescriptionOnly
    Note:
        Model Depth 6
    Attributes:
    """


class PrescriptionOnlyAllProperties(
    PrescriptionOnlyInheritedProperties, PrescriptionOnlyProperties, TypedDict
):
    pass


class PrescriptionOnlyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PrescriptionOnly", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PrescriptionOnlyProperties,
        PrescriptionOnlyInheritedProperties,
        PrescriptionOnlyAllProperties,
    ] = PrescriptionOnlyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PrescriptionOnly"
    return model


PrescriptionOnly = create_schema_org_model()


def create_prescriptiononly_model(
    model: Union[
        PrescriptionOnlyProperties,
        PrescriptionOnlyInheritedProperties,
        PrescriptionOnlyAllProperties,
    ]
):
    _type = deepcopy(PrescriptionOnlyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PrescriptionOnlyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PrescriptionOnlyAllProperties):
    pydantic_type = create_prescriptiononly_model(model=model)
    return pydantic_type(model).schema_json()
