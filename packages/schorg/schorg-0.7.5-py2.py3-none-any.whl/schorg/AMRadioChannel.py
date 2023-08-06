"""
A radio channel that uses AM.

https://schema.org/AMRadioChannel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AMRadioChannelInheritedProperties(TypedDict):
    """A radio channel that uses AM.

    References:
        https://schema.org/AMRadioChannel
    Note:
        Model Depth 5
    Attributes:
    """


class AMRadioChannelProperties(TypedDict):
    """A radio channel that uses AM.

    References:
        https://schema.org/AMRadioChannel
    Note:
        Model Depth 5
    Attributes:
    """


class AMRadioChannelAllProperties(
    AMRadioChannelInheritedProperties, AMRadioChannelProperties, TypedDict
):
    pass


class AMRadioChannelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AMRadioChannel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AMRadioChannelProperties,
        AMRadioChannelInheritedProperties,
        AMRadioChannelAllProperties,
    ] = AMRadioChannelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AMRadioChannel"
    return model


AMRadioChannel = create_schema_org_model()


def create_amradiochannel_model(
    model: Union[
        AMRadioChannelProperties,
        AMRadioChannelInheritedProperties,
        AMRadioChannelAllProperties,
    ]
):
    _type = deepcopy(AMRadioChannelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of AMRadioChannel. Please see: https://schema.org/AMRadioChannel"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: AMRadioChannelAllProperties):
    pydantic_type = create_amradiochannel_model(model=model)
    return pydantic_type(model).schema_json()
