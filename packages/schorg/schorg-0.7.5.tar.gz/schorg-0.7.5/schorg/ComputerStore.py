"""
A computer store.

https://schema.org/ComputerStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComputerStoreInheritedProperties(TypedDict):
    """A computer store.

    References:
        https://schema.org/ComputerStore
    Note:
        Model Depth 5
    Attributes:
    """


class ComputerStoreProperties(TypedDict):
    """A computer store.

    References:
        https://schema.org/ComputerStore
    Note:
        Model Depth 5
    Attributes:
    """


class ComputerStoreAllProperties(
    ComputerStoreInheritedProperties, ComputerStoreProperties, TypedDict
):
    pass


class ComputerStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ComputerStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ComputerStoreProperties,
        ComputerStoreInheritedProperties,
        ComputerStoreAllProperties,
    ] = ComputerStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComputerStore"
    return model


ComputerStore = create_schema_org_model()


def create_computerstore_model(
    model: Union[
        ComputerStoreProperties,
        ComputerStoreInheritedProperties,
        ComputerStoreAllProperties,
    ]
):
    _type = deepcopy(ComputerStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ComputerStore. Please see: https://schema.org/ComputerStore"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ComputerStoreAllProperties):
    pydantic_type = create_computerstore_model(model=model)
    return pydantic_type(model).schema_json()
