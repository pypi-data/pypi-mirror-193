"""
The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to.Related actions:* [[FollowAction]]: Unlike FollowAction, SubscribeAction implies that the subscriber acts as a passive agent being constantly/actively pushed for updates.* [[RegisterAction]]: Unlike RegisterAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.* [[JoinAction]]: Unlike JoinAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.

https://schema.org/SubscribeAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SubscribeActionInheritedProperties(TypedDict):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to.Related actions:* [[FollowAction]]: Unlike FollowAction, SubscribeAction implies that the subscriber acts as a passive agent being constantly/actively pushed for updates.* [[RegisterAction]]: Unlike RegisterAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.* [[JoinAction]]: Unlike JoinAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.

    References:
        https://schema.org/SubscribeAction
    Note:
        Model Depth 4
    Attributes:
    """


class SubscribeActionProperties(TypedDict):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to.Related actions:* [[FollowAction]]: Unlike FollowAction, SubscribeAction implies that the subscriber acts as a passive agent being constantly/actively pushed for updates.* [[RegisterAction]]: Unlike RegisterAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.* [[JoinAction]]: Unlike JoinAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.

    References:
        https://schema.org/SubscribeAction
    Note:
        Model Depth 4
    Attributes:
    """


class SubscribeActionAllProperties(
    SubscribeActionInheritedProperties, SubscribeActionProperties, TypedDict
):
    pass


class SubscribeActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SubscribeAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SubscribeActionProperties,
        SubscribeActionInheritedProperties,
        SubscribeActionAllProperties,
    ] = SubscribeActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SubscribeAction"
    return model


SubscribeAction = create_schema_org_model()


def create_subscribeaction_model(
    model: Union[
        SubscribeActionProperties,
        SubscribeActionInheritedProperties,
        SubscribeActionAllProperties,
    ]
):
    _type = deepcopy(SubscribeActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SubscribeAction. Please see: https://schema.org/SubscribeAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SubscribeActionAllProperties):
    pydantic_type = create_subscribeaction_model(model=model)
    return pydantic_type(model).schema_json()
