"""
A public swimming pool.

https://schema.org/PublicSwimmingPool
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PublicSwimmingPoolInheritedProperties(TypedDict):
    """A public swimming pool.

    References:
        https://schema.org/PublicSwimmingPool
    Note:
        Model Depth 5
    Attributes:
    """


class PublicSwimmingPoolProperties(TypedDict):
    """A public swimming pool.

    References:
        https://schema.org/PublicSwimmingPool
    Note:
        Model Depth 5
    Attributes:
    """


class PublicSwimmingPoolAllProperties(
    PublicSwimmingPoolInheritedProperties, PublicSwimmingPoolProperties, TypedDict
):
    pass


class PublicSwimmingPoolBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PublicSwimmingPool", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PublicSwimmingPoolProperties,
        PublicSwimmingPoolInheritedProperties,
        PublicSwimmingPoolAllProperties,
    ] = PublicSwimmingPoolAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PublicSwimmingPool"
    return model


PublicSwimmingPool = create_schema_org_model()


def create_publicswimmingpool_model(
    model: Union[
        PublicSwimmingPoolProperties,
        PublicSwimmingPoolInheritedProperties,
        PublicSwimmingPoolAllProperties,
    ]
):
    _type = deepcopy(PublicSwimmingPoolAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PublicSwimmingPoolAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PublicSwimmingPoolAllProperties):
    pydantic_type = create_publicswimmingpool_model(model=model)
    return pydantic_type(model).schema_json()
