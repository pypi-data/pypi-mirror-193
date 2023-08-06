"""
An auto parts store.

https://schema.org/AutoPartsStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AutoPartsStoreInheritedProperties(TypedDict):
    """An auto parts store.

    References:
        https://schema.org/AutoPartsStore
    Note:
        Model Depth 5
    Attributes:
    """


class AutoPartsStoreProperties(TypedDict):
    """An auto parts store.

    References:
        https://schema.org/AutoPartsStore
    Note:
        Model Depth 5
    Attributes:
    """


class AutoPartsStoreAllProperties(
    AutoPartsStoreInheritedProperties, AutoPartsStoreProperties, TypedDict
):
    pass


class AutoPartsStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AutoPartsStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AutoPartsStoreProperties,
        AutoPartsStoreInheritedProperties,
        AutoPartsStoreAllProperties,
    ] = AutoPartsStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AutoPartsStore"
    return model


AutoPartsStore = create_schema_org_model()


def create_autopartsstore_model(
    model: Union[
        AutoPartsStoreProperties,
        AutoPartsStoreInheritedProperties,
        AutoPartsStoreAllProperties,
    ]
):
    _type = deepcopy(AutoPartsStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of AutoPartsStore. Please see: https://schema.org/AutoPartsStore"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: AutoPartsStoreAllProperties):
    pydantic_type = create_autopartsstore_model(model=model)
    return pydantic_type(model).schema_json()
