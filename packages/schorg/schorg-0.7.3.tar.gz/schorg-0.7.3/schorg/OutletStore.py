"""
An outlet store.

https://schema.org/OutletStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OutletStoreInheritedProperties(TypedDict):
    """An outlet store.

    References:
        https://schema.org/OutletStore
    Note:
        Model Depth 5
    Attributes:
    """


class OutletStoreProperties(TypedDict):
    """An outlet store.

    References:
        https://schema.org/OutletStore
    Note:
        Model Depth 5
    Attributes:
    """


class OutletStoreAllProperties(
    OutletStoreInheritedProperties, OutletStoreProperties, TypedDict
):
    pass


class OutletStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OutletStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OutletStoreProperties, OutletStoreInheritedProperties, OutletStoreAllProperties
    ] = OutletStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OutletStore"
    return model


OutletStore = create_schema_org_model()


def create_outletstore_model(
    model: Union[
        OutletStoreProperties, OutletStoreInheritedProperties, OutletStoreAllProperties
    ]
):
    _type = deepcopy(OutletStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OutletStoreAllProperties):
    pydantic_type = create_outletstore_model(model=model)
    return pydantic_type(model).schema_json()
