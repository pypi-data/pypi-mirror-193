"""
The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.Related actions:* [[TakeAction]]: Reciprocal of GiveAction.* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).

https://schema.org/GiveAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GiveActionInheritedProperties(TypedDict):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.Related actions:* [[TakeAction]]: Reciprocal of GiveAction.* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).

    References:
        https://schema.org/GiveAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GiveActionProperties(TypedDict):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.Related actions:* [[TakeAction]]: Reciprocal of GiveAction.* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).

    References:
        https://schema.org/GiveAction
    Note:
        Model Depth 4
    Attributes:
        recipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the receiving end of the action.
    """

    recipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GiveActionAllProperties(
    GiveActionInheritedProperties, GiveActionProperties, TypedDict
):
    pass


class GiveActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GiveAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}
        fields = {"recipient": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GiveActionProperties, GiveActionInheritedProperties, GiveActionAllProperties
    ] = GiveActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GiveAction"
    return model


GiveAction = create_schema_org_model()


def create_giveaction_model(
    model: Union[
        GiveActionProperties, GiveActionInheritedProperties, GiveActionAllProperties
    ]
):
    _type = deepcopy(GiveActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GiveAction. Please see: https://schema.org/GiveAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GiveActionAllProperties):
    pydantic_type = create_giveaction_model(model=model)
    return pydantic_type(model).schema_json()
