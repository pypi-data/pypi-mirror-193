"""
A waterfall, like Niagara.

https://schema.org/Waterfall
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WaterfallInheritedProperties(TypedDict):
    """A waterfall, like Niagara.

    References:
        https://schema.org/Waterfall
    Note:
        Model Depth 5
    Attributes:
    """


class WaterfallProperties(TypedDict):
    """A waterfall, like Niagara.

    References:
        https://schema.org/Waterfall
    Note:
        Model Depth 5
    Attributes:
    """


class WaterfallAllProperties(
    WaterfallInheritedProperties, WaterfallProperties, TypedDict
):
    pass


class WaterfallBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Waterfall", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WaterfallProperties, WaterfallInheritedProperties, WaterfallAllProperties
    ] = WaterfallAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Waterfall"
    return model


Waterfall = create_schema_org_model()


def create_waterfall_model(
    model: Union[
        WaterfallProperties, WaterfallInheritedProperties, WaterfallAllProperties
    ]
):
    _type = deepcopy(WaterfallAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WaterfallAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WaterfallAllProperties):
    pydantic_type = create_waterfall_model(model=model)
    return pydantic_type(model).schema_json()
