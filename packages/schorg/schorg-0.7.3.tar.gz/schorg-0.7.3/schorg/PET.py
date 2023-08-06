"""
Positron emission tomography imaging.

https://schema.org/PET
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class PETAllProperties(PETInheritedProperties, PETProperties, TypedDict):
    pass


class PETBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PET", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PETProperties, PETInheritedProperties, PETAllProperties
    ] = PETAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PET"
    return model


PET = create_schema_org_model()


def create_pet_model(
    model: Union[PETProperties, PETInheritedProperties, PETAllProperties]
):
    _type = deepcopy(PETAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PETAllProperties):
    pydantic_type = create_pet_model(model=model)
    return pydantic_type(model).schema_json()
