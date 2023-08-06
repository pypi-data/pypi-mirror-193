"""
Abdomen clinical examination.

https://schema.org/Abdomen
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AbdomenInheritedProperties(TypedDict):
    """Abdomen clinical examination.

    References:
        https://schema.org/Abdomen
    Note:
        Model Depth 5
    Attributes:
    """


class AbdomenProperties(TypedDict):
    """Abdomen clinical examination.

    References:
        https://schema.org/Abdomen
    Note:
        Model Depth 5
    Attributes:
    """


class AbdomenAllProperties(AbdomenInheritedProperties, AbdomenProperties, TypedDict):
    pass


class AbdomenBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Abdomen", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AbdomenProperties, AbdomenInheritedProperties, AbdomenAllProperties
    ] = AbdomenAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Abdomen"
    return model


Abdomen = create_schema_org_model()


def create_abdomen_model(
    model: Union[AbdomenProperties, AbdomenInheritedProperties, AbdomenAllProperties]
):
    _type = deepcopy(AbdomenAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AbdomenAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AbdomenAllProperties):
    pydantic_type = create_abdomen_model(model=model)
    return pydantic_type(model).schema_json()
