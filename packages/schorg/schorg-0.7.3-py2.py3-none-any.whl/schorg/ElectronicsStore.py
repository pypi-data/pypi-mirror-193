"""
An electronics store.

https://schema.org/ElectronicsStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ElectronicsStoreInheritedProperties(TypedDict):
    """An electronics store.

    References:
        https://schema.org/ElectronicsStore
    Note:
        Model Depth 5
    Attributes:
    """


class ElectronicsStoreProperties(TypedDict):
    """An electronics store.

    References:
        https://schema.org/ElectronicsStore
    Note:
        Model Depth 5
    Attributes:
    """


class ElectronicsStoreAllProperties(
    ElectronicsStoreInheritedProperties, ElectronicsStoreProperties, TypedDict
):
    pass


class ElectronicsStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ElectronicsStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ElectronicsStoreProperties,
        ElectronicsStoreInheritedProperties,
        ElectronicsStoreAllProperties,
    ] = ElectronicsStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ElectronicsStore"
    return model


ElectronicsStore = create_schema_org_model()


def create_electronicsstore_model(
    model: Union[
        ElectronicsStoreProperties,
        ElectronicsStoreInheritedProperties,
        ElectronicsStoreAllProperties,
    ]
):
    _type = deepcopy(ElectronicsStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ElectronicsStoreAllProperties):
    pydantic_type = create_electronicsstore_model(model=model)
    return pydantic_type(model).schema_json()
