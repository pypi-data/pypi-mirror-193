"""
A toy store.

https://schema.org/ToyStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ToyStoreInheritedProperties(TypedDict):
    """A toy store.

    References:
        https://schema.org/ToyStore
    Note:
        Model Depth 5
    Attributes:
    """


class ToyStoreProperties(TypedDict):
    """A toy store.

    References:
        https://schema.org/ToyStore
    Note:
        Model Depth 5
    Attributes:
    """


class ToyStoreAllProperties(ToyStoreInheritedProperties, ToyStoreProperties, TypedDict):
    pass


class ToyStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ToyStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ToyStoreProperties, ToyStoreInheritedProperties, ToyStoreAllProperties
    ] = ToyStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ToyStore"
    return model


ToyStore = create_schema_org_model()


def create_toystore_model(
    model: Union[ToyStoreProperties, ToyStoreInheritedProperties, ToyStoreAllProperties]
):
    _type = deepcopy(ToyStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ToyStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ToyStoreAllProperties):
    pydantic_type = create_toystore_model(model=model)
    return pydantic_type(model).schema_json()
