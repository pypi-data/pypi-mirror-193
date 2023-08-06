"""
A prion is an infectious agent composed of protein in a misfolded form.

https://schema.org/Prion
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PrionInheritedProperties(TypedDict):
    """A prion is an infectious agent composed of protein in a misfolded form.

    References:
        https://schema.org/Prion
    Note:
        Model Depth 6
    Attributes:
    """


class PrionProperties(TypedDict):
    """A prion is an infectious agent composed of protein in a misfolded form.

    References:
        https://schema.org/Prion
    Note:
        Model Depth 6
    Attributes:
    """


class PrionAllProperties(PrionInheritedProperties, PrionProperties, TypedDict):
    pass


class PrionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Prion", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PrionProperties, PrionInheritedProperties, PrionAllProperties
    ] = PrionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Prion"
    return model


Prion = create_schema_org_model()


def create_prion_model(
    model: Union[PrionProperties, PrionInheritedProperties, PrionAllProperties]
):
    _type = deepcopy(PrionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PrionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PrionAllProperties):
    pydantic_type = create_prion_model(model=model)
    return pydantic_type(model).schema_json()
