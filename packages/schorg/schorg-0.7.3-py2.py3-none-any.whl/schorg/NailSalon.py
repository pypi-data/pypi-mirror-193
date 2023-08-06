"""
A nail salon.

https://schema.org/NailSalon
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NailSalonInheritedProperties(TypedDict):
    """A nail salon.

    References:
        https://schema.org/NailSalon
    Note:
        Model Depth 5
    Attributes:
    """


class NailSalonProperties(TypedDict):
    """A nail salon.

    References:
        https://schema.org/NailSalon
    Note:
        Model Depth 5
    Attributes:
    """


class NailSalonAllProperties(
    NailSalonInheritedProperties, NailSalonProperties, TypedDict
):
    pass


class NailSalonBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NailSalon", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NailSalonProperties, NailSalonInheritedProperties, NailSalonAllProperties
    ] = NailSalonAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NailSalon"
    return model


NailSalon = create_schema_org_model()


def create_nailsalon_model(
    model: Union[
        NailSalonProperties, NailSalonInheritedProperties, NailSalonAllProperties
    ]
):
    _type = deepcopy(NailSalonAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NailSalonAllProperties):
    pydantic_type = create_nailsalon_model(model=model)
    return pydantic_type(model).schema_json()
