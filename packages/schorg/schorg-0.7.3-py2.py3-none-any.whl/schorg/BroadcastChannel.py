"""
A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

https://schema.org/BroadcastChannel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BroadcastChannelInheritedProperties(TypedDict):
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

    References:
        https://schema.org/BroadcastChannel
    Note:
        Model Depth 3
    Attributes:
    """


class BroadcastChannelProperties(TypedDict):
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

    References:
        https://schema.org/BroadcastChannel
    Note:
        Model Depth 3
    Attributes:
        broadcastChannelId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The unique address by which the BroadcastService can be identified in a provider lineup. In US, this is typically a number.
        providesBroadcastService: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The BroadcastService offered on this channel.
        genre: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Genre of the creative work, broadcast channel or group.
        broadcastServiceTier: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of service required to have access to the channel (e.g. Standard or Premium).
        inBroadcastLineup: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The CableOrSatelliteService offering the channel.
        broadcastFrequency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g. 87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels, e.g. "87 FM".
    """

    broadcastChannelId: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    providesBroadcastService: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    genre: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    broadcastServiceTier: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    inBroadcastLineup: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    broadcastFrequency: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class BroadcastChannelAllProperties(
    BroadcastChannelInheritedProperties, BroadcastChannelProperties, TypedDict
):
    pass


class BroadcastChannelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BroadcastChannel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"broadcastChannelId": {"exclude": True}}
        fields = {"providesBroadcastService": {"exclude": True}}
        fields = {"genre": {"exclude": True}}
        fields = {"broadcastServiceTier": {"exclude": True}}
        fields = {"inBroadcastLineup": {"exclude": True}}
        fields = {"broadcastFrequency": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BroadcastChannelProperties,
        BroadcastChannelInheritedProperties,
        BroadcastChannelAllProperties,
    ] = BroadcastChannelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BroadcastChannel"
    return model


BroadcastChannel = create_schema_org_model()


def create_broadcastchannel_model(
    model: Union[
        BroadcastChannelProperties,
        BroadcastChannelInheritedProperties,
        BroadcastChannelAllProperties,
    ]
):
    _type = deepcopy(BroadcastChannelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BroadcastChannelAllProperties):
    pydantic_type = create_broadcastchannel_model(model=model)
    return pydantic_type(model).schema_json()
