"""
A delivery service through which radio content is provided via broadcast over the air or online.

https://schema.org/RadioBroadcastService
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadioBroadcastServiceInheritedProperties(TypedDict):
    """A delivery service through which radio content is provided via broadcast over the air or online.

    References:
        https://schema.org/RadioBroadcastService
    Note:
        Model Depth 5
    Attributes:
        hasBroadcastChannel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A broadcast channel of a broadcast service.
        parentService: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A broadcast service to which the broadcast service may belong to such as regional variations of a national channel.
        broadcastAffiliateOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The media network(s) whose content is broadcast on this station.
        broadcaster: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The organization owning or operating the broadcast service.
        videoFormat: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).
        broadcastTimezone: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The timezone in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) for which the service bases its broadcasts.
        broadcastDisplayName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name displayed in the channel guide. For many US affiliates, it is the network name.
        broadcastFrequency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g. 87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels, e.g. "87 FM".
        inLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        area: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The area within which users can expect to reach the broadcast service.
        callSign: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
    """

    hasBroadcastChannel: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    parentService: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    broadcastAffiliateOf: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    broadcaster: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    videoFormat: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    broadcastTimezone: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    broadcastDisplayName: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    broadcastFrequency: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    inLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    area: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    callSign: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class RadioBroadcastServiceProperties(TypedDict):
    """A delivery service through which radio content is provided via broadcast over the air or online.

    References:
        https://schema.org/RadioBroadcastService
    Note:
        Model Depth 5
    Attributes:
    """


class RadioBroadcastServiceAllProperties(
    RadioBroadcastServiceInheritedProperties, RadioBroadcastServiceProperties, TypedDict
):
    pass


class RadioBroadcastServiceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RadioBroadcastService", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasBroadcastChannel": {"exclude": True}}
        fields = {"parentService": {"exclude": True}}
        fields = {"broadcastAffiliateOf": {"exclude": True}}
        fields = {"broadcaster": {"exclude": True}}
        fields = {"videoFormat": {"exclude": True}}
        fields = {"broadcastTimezone": {"exclude": True}}
        fields = {"broadcastDisplayName": {"exclude": True}}
        fields = {"broadcastFrequency": {"exclude": True}}
        fields = {"inLanguage": {"exclude": True}}
        fields = {"area": {"exclude": True}}
        fields = {"callSign": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RadioBroadcastServiceProperties,
        RadioBroadcastServiceInheritedProperties,
        RadioBroadcastServiceAllProperties,
    ] = RadioBroadcastServiceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RadioBroadcastService"
    return model


RadioBroadcastService = create_schema_org_model()


def create_radiobroadcastservice_model(
    model: Union[
        RadioBroadcastServiceProperties,
        RadioBroadcastServiceInheritedProperties,
        RadioBroadcastServiceAllProperties,
    ]
):
    _type = deepcopy(RadioBroadcastServiceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RadioBroadcastServiceAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RadioBroadcastServiceAllProperties):
    pydantic_type = create_radiobroadcastservice_model(model=model)
    return pydantic_type(model).schema_json()
