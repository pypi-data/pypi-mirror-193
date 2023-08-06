"""
The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.

https://schema.org/ArriveAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ArriveActionInheritedProperties(TypedDict):
    """The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.

    References:
        https://schema.org/ArriveAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ArriveActionProperties(TypedDict):
    """The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.

    References:
        https://schema.org/ArriveAction
    Note:
        Model Depth 4
    Attributes:
    """


class ArriveActionAllProperties(
    ArriveActionInheritedProperties, ArriveActionProperties, TypedDict
):
    pass


class ArriveActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ArriveAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ArriveActionProperties,
        ArriveActionInheritedProperties,
        ArriveActionAllProperties,
    ] = ArriveActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ArriveAction"
    return model


ArriveAction = create_schema_org_model()


def create_arriveaction_model(
    model: Union[
        ArriveActionProperties,
        ArriveActionInheritedProperties,
        ArriveActionAllProperties,
    ]
):
    _type = deepcopy(ArriveActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ArriveAction. Please see: https://schema.org/ArriveAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ArriveActionAllProperties):
    pydantic_type = create_arriveaction_model(model=model)
    return pydantic_type(model).schema_json()
