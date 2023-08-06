"""
The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.Related actions:* [[BefriendAction]]: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.* [[SubscribeAction]]: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.* [[RegisterAction]]: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.* [[JoinAction]]: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.* [[TrackAction]]: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don't follow it).

https://schema.org/FollowAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FollowActionInheritedProperties(TypedDict):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.Related actions:* [[BefriendAction]]: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.* [[SubscribeAction]]: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.* [[RegisterAction]]: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.* [[JoinAction]]: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.* [[TrackAction]]: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don't follow it).

    References:
        https://schema.org/FollowAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class FollowActionProperties(TypedDict):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.Related actions:* [[BefriendAction]]: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.* [[SubscribeAction]]: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.* [[RegisterAction]]: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.* [[JoinAction]]: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.* [[TrackAction]]: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don't follow it).

    References:
        https://schema.org/FollowAction
    Note:
        Model Depth 4
    Attributes:
        followee: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of object. The person or organization being followed.
    """

    followee: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(FollowActionInheritedProperties , FollowActionProperties, TypedDict):
    pass


class FollowActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FollowAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'followee': {'exclude': True}}
        


def create_schema_org_model(type_: Union[FollowActionProperties, FollowActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FollowAction"
    return model
    

FollowAction = create_schema_org_model()


def create_followaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_followaction_model(model=model)
    return pydantic_type(model).schema_json()


