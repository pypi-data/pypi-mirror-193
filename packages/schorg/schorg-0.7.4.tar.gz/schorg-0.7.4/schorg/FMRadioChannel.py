"""
A radio channel that uses FM.

https://schema.org/FMRadioChannel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FMRadioChannelInheritedProperties(TypedDict):
    """A radio channel that uses FM.

    References:
        https://schema.org/FMRadioChannel
    Note:
        Model Depth 5
    Attributes:
    """


class FMRadioChannelProperties(TypedDict):
    """A radio channel that uses FM.

    References:
        https://schema.org/FMRadioChannel
    Note:
        Model Depth 5
    Attributes:
    """


class FMRadioChannelAllProperties(
    FMRadioChannelInheritedProperties, FMRadioChannelProperties, TypedDict
):
    pass


class FMRadioChannelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FMRadioChannel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FMRadioChannelProperties,
        FMRadioChannelInheritedProperties,
        FMRadioChannelAllProperties,
    ] = FMRadioChannelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FMRadioChannel"
    return model


FMRadioChannel = create_schema_org_model()


def create_fmradiochannel_model(
    model: Union[
        FMRadioChannelProperties,
        FMRadioChannelInheritedProperties,
        FMRadioChannelAllProperties,
    ]
):
    _type = deepcopy(FMRadioChannelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FMRadioChannelAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FMRadioChannelAllProperties):
    pydantic_type = create_fmradiochannel_model(model=model)
    return pydantic_type(model).schema_json()
