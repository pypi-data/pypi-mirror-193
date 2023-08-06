"""
A store that sells reading glasses and similar devices for improving vision.

https://schema.org/Optician
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OpticianInheritedProperties(TypedDict):
    """A store that sells reading glasses and similar devices for improving vision.

    References:
        https://schema.org/Optician
    Note:
        Model Depth 5
    Attributes:
    """


class OpticianProperties(TypedDict):
    """A store that sells reading glasses and similar devices for improving vision.

    References:
        https://schema.org/Optician
    Note:
        Model Depth 5
    Attributes:
    """


class OpticianAllProperties(OpticianInheritedProperties, OpticianProperties, TypedDict):
    pass


class OpticianBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Optician", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OpticianProperties, OpticianInheritedProperties, OpticianAllProperties
    ] = OpticianAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Optician"
    return model


Optician = create_schema_org_model()


def create_optician_model(
    model: Union[OpticianProperties, OpticianInheritedProperties, OpticianAllProperties]
):
    _type = deepcopy(OpticianAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OpticianAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OpticianAllProperties):
    pydantic_type = create_optician_model(model=model)
    return pydantic_type(model).schema_json()
