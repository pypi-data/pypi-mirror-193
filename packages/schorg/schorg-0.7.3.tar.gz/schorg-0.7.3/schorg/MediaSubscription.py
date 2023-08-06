"""
A subscription which allows a user to access media including audio, video, books, etc.

https://schema.org/MediaSubscription
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MediaSubscriptionInheritedProperties(TypedDict):
    """A subscription which allows a user to access media including audio, video, books, etc.

    References:
        https://schema.org/MediaSubscription
    Note:
        Model Depth 3
    Attributes:
    """


class MediaSubscriptionProperties(TypedDict):
    """A subscription which allows a user to access media including audio, video, books, etc.

    References:
        https://schema.org/MediaSubscription
    Note:
        Model Depth 3
    Attributes:
        expectsAcceptanceOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
        authenticator: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Organization responsible for authenticating the user's subscription. For example, many media apps require a cable/satellite provider to authenticate your subscription before playing media.
    """

    expectsAcceptanceOf: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    authenticator: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MediaSubscriptionAllProperties(
    MediaSubscriptionInheritedProperties, MediaSubscriptionProperties, TypedDict
):
    pass


class MediaSubscriptionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MediaSubscription", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"expectsAcceptanceOf": {"exclude": True}}
        fields = {"authenticator": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MediaSubscriptionProperties,
        MediaSubscriptionInheritedProperties,
        MediaSubscriptionAllProperties,
    ] = MediaSubscriptionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MediaSubscription"
    return model


MediaSubscription = create_schema_org_model()


def create_mediasubscription_model(
    model: Union[
        MediaSubscriptionProperties,
        MediaSubscriptionInheritedProperties,
        MediaSubscriptionAllProperties,
    ]
):
    _type = deepcopy(MediaSubscriptionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MediaSubscriptionAllProperties):
    pydantic_type = create_mediasubscription_model(model=model)
    return pydantic_type(model).schema_json()
