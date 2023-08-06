"""
A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

https://schema.org/LiquorStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LiquorStoreInheritedProperties(TypedDict):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    References:
        https://schema.org/LiquorStore
    Note:
        Model Depth 5
    Attributes:
    """


class LiquorStoreProperties(TypedDict):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    References:
        https://schema.org/LiquorStore
    Note:
        Model Depth 5
    Attributes:
    """


class LiquorStoreAllProperties(
    LiquorStoreInheritedProperties, LiquorStoreProperties, TypedDict
):
    pass


class LiquorStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LiquorStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LiquorStoreProperties, LiquorStoreInheritedProperties, LiquorStoreAllProperties
    ] = LiquorStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LiquorStore"
    return model


LiquorStore = create_schema_org_model()


def create_liquorstore_model(
    model: Union[
        LiquorStoreProperties, LiquorStoreInheritedProperties, LiquorStoreAllProperties
    ]
):
    _type = deepcopy(LiquorStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LiquorStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LiquorStoreAllProperties):
    pydantic_type = create_liquorstore_model(model=model)
    return pydantic_type(model).schema_json()
