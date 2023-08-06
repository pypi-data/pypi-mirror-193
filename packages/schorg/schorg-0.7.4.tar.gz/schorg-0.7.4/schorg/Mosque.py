"""
A mosque.

https://schema.org/Mosque
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MosqueInheritedProperties(TypedDict):
    """A mosque.

    References:
        https://schema.org/Mosque
    Note:
        Model Depth 5
    Attributes:
    """


class MosqueProperties(TypedDict):
    """A mosque.

    References:
        https://schema.org/Mosque
    Note:
        Model Depth 5
    Attributes:
    """


class MosqueAllProperties(MosqueInheritedProperties, MosqueProperties, TypedDict):
    pass


class MosqueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Mosque", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MosqueProperties, MosqueInheritedProperties, MosqueAllProperties
    ] = MosqueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Mosque"
    return model


Mosque = create_schema_org_model()


def create_mosque_model(
    model: Union[MosqueProperties, MosqueInheritedProperties, MosqueAllProperties]
):
    _type = deepcopy(MosqueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MosqueAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MosqueAllProperties):
    pydantic_type = create_mosque_model(model=model)
    return pydantic_type(model).schema_json()
