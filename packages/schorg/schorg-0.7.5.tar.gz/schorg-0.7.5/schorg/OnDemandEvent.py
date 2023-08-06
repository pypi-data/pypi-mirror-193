"""
A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.

https://schema.org/OnDemandEvent
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnDemandEventInheritedProperties(TypedDict):
    """A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.

    References:
        https://schema.org/OnDemandEvent
    Note:
        Model Depth 4
    Attributes:
        publishedBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An agent associated with the publication event.
        free: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): A flag to signal that the item, event, or place is accessible for free.
        publishedOn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A broadcast service associated with the publication event.
    """

    publishedBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    free: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]
    publishedOn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class OnDemandEventProperties(TypedDict):
    """A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.

    References:
        https://schema.org/OnDemandEvent
    Note:
        Model Depth 4
    Attributes:
    """


class OnDemandEventAllProperties(
    OnDemandEventInheritedProperties, OnDemandEventProperties, TypedDict
):
    pass


class OnDemandEventBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OnDemandEvent", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"publishedBy": {"exclude": True}}
        fields = {"free": {"exclude": True}}
        fields = {"publishedOn": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OnDemandEventProperties,
        OnDemandEventInheritedProperties,
        OnDemandEventAllProperties,
    ] = OnDemandEventAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnDemandEvent"
    return model


OnDemandEvent = create_schema_org_model()


def create_ondemandevent_model(
    model: Union[
        OnDemandEventProperties,
        OnDemandEventInheritedProperties,
        OnDemandEventAllProperties,
    ]
):
    _type = deepcopy(OnDemandEventAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OnDemandEvent. Please see: https://schema.org/OnDemandEvent"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OnDemandEventAllProperties):
    pydantic_type = create_ondemandevent_model(model=model)
    return pydantic_type(model).schema_json()
