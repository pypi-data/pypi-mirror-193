"""
A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Conference_hall">http://en.wikipedia.org/wiki/Conference_hall</a>).<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

https://schema.org/MeetingRoom
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MeetingRoomInheritedProperties(TypedDict):
    """A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Conference_hall">http://en.wikipedia.org/wiki/Conference_hall</a>).<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/MeetingRoom
    Note:
        Model Depth 5
    Attributes:
    """


class MeetingRoomProperties(TypedDict):
    """A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Conference_hall">http://en.wikipedia.org/wiki/Conference_hall</a>).<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/MeetingRoom
    Note:
        Model Depth 5
    Attributes:
    """


class MeetingRoomAllProperties(
    MeetingRoomInheritedProperties, MeetingRoomProperties, TypedDict
):
    pass


class MeetingRoomBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MeetingRoom", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MeetingRoomProperties, MeetingRoomInheritedProperties, MeetingRoomAllProperties
    ] = MeetingRoomAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MeetingRoom"
    return model


MeetingRoom = create_schema_org_model()


def create_meetingroom_model(
    model: Union[
        MeetingRoomProperties, MeetingRoomInheritedProperties, MeetingRoomAllProperties
    ]
):
    _type = deepcopy(MeetingRoomAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MeetingRoom. Please see: https://schema.org/MeetingRoom"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MeetingRoomAllProperties):
    pydantic_type = create_meetingroom_model(model=model)
    return pydantic_type(model).schema_json()
