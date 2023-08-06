"""
Specifies that product returns must be made in a store.

https://schema.org/ReturnInStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnInStoreInheritedProperties(TypedDict):
    """Specifies that product returns must be made in a store.

    References:
        https://schema.org/ReturnInStore
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnInStoreProperties(TypedDict):
    """Specifies that product returns must be made in a store.

    References:
        https://schema.org/ReturnInStore
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnInStoreAllProperties(
    ReturnInStoreInheritedProperties, ReturnInStoreProperties, TypedDict
):
    pass


class ReturnInStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnInStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReturnInStoreProperties,
        ReturnInStoreInheritedProperties,
        ReturnInStoreAllProperties,
    ] = ReturnInStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnInStore"
    return model


ReturnInStore = create_schema_org_model()


def create_returninstore_model(
    model: Union[
        ReturnInStoreProperties,
        ReturnInStoreInheritedProperties,
        ReturnInStoreAllProperties,
    ]
):
    _type = deepcopy(ReturnInStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ReturnInStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReturnInStoreAllProperties):
    pydantic_type = create_returninstore_model(model=model)
    return pydantic_type(model).schema_json()
