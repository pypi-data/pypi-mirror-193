"""
A casino.

https://schema.org/Casino
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CasinoInheritedProperties(TypedDict):
    """A casino.

    References:
        https://schema.org/Casino
    Note:
        Model Depth 5
    Attributes:
    """


class CasinoProperties(TypedDict):
    """A casino.

    References:
        https://schema.org/Casino
    Note:
        Model Depth 5
    Attributes:
    """


class CasinoAllProperties(CasinoInheritedProperties, CasinoProperties, TypedDict):
    pass


class CasinoBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Casino", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CasinoProperties, CasinoInheritedProperties, CasinoAllProperties
    ] = CasinoAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Casino"
    return model


Casino = create_schema_org_model()


def create_casino_model(
    model: Union[CasinoProperties, CasinoInheritedProperties, CasinoAllProperties]
):
    _type = deepcopy(CasinoAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Casino. Please see: https://schema.org/Casino"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CasinoAllProperties):
    pydantic_type = create_casino_model(model=model)
    return pydantic_type(model).schema_json()
