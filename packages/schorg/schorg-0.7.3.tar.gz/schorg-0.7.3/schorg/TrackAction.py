"""
An agent tracks an object for updates.Related actions:* [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.

https://schema.org/TrackAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TrackActionInheritedProperties(TypedDict):
    """An agent tracks an object for updates.Related actions:* [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.

    References:
        https://schema.org/TrackAction
    Note:
        Model Depth 4
    Attributes:
    """


class TrackActionProperties(TypedDict):
    """An agent tracks an object for updates.Related actions:* [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.

    References:
        https://schema.org/TrackAction
    Note:
        Model Depth 4
    Attributes:
        deliveryMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The method of delivery.
    """

    deliveryMethod: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class TrackActionAllProperties(
    TrackActionInheritedProperties, TrackActionProperties, TypedDict
):
    pass


class TrackActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TrackAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"deliveryMethod": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TrackActionProperties, TrackActionInheritedProperties, TrackActionAllProperties
    ] = TrackActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TrackAction"
    return model


TrackAction = create_schema_org_model()


def create_trackaction_model(
    model: Union[
        TrackActionProperties, TrackActionInheritedProperties, TrackActionAllProperties
    ]
):
    _type = deepcopy(TrackActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TrackActionAllProperties):
    pydantic_type = create_trackaction_model(model=model)
    return pydantic_type(model).schema_json()
