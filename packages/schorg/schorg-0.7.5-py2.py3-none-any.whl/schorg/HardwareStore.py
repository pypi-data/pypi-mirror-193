"""
A hardware store.

https://schema.org/HardwareStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HardwareStoreInheritedProperties(TypedDict):
    """A hardware store.

    References:
        https://schema.org/HardwareStore
    Note:
        Model Depth 5
    Attributes:
    """


class HardwareStoreProperties(TypedDict):
    """A hardware store.

    References:
        https://schema.org/HardwareStore
    Note:
        Model Depth 5
    Attributes:
    """


class HardwareStoreAllProperties(
    HardwareStoreInheritedProperties, HardwareStoreProperties, TypedDict
):
    pass


class HardwareStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HardwareStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HardwareStoreProperties,
        HardwareStoreInheritedProperties,
        HardwareStoreAllProperties,
    ] = HardwareStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HardwareStore"
    return model


HardwareStore = create_schema_org_model()


def create_hardwarestore_model(
    model: Union[
        HardwareStoreProperties,
        HardwareStoreInheritedProperties,
        HardwareStoreAllProperties,
    ]
):
    _type = deepcopy(HardwareStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HardwareStore. Please see: https://schema.org/HardwareStore"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HardwareStoreAllProperties):
    pydantic_type = create_hardwarestore_model(model=model)
    return pydantic_type(model).schema_json()
