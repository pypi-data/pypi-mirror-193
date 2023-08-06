"""
The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.Related actions:* [[GiveAction]]: The reciprocal of TakeAction.* [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transferred.

https://schema.org/TakeAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TakeActionInheritedProperties(TypedDict):
    """The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.Related actions:* [[GiveAction]]: The reciprocal of TakeAction.* [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transferred.

    References:
        https://schema.org/TakeAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TakeActionProperties(TypedDict):
    """The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.Related actions:* [[GiveAction]]: The reciprocal of TakeAction.* [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transferred.

    References:
        https://schema.org/TakeAction
    Note:
        Model Depth 4
    Attributes:
    """


class TakeActionAllProperties(
    TakeActionInheritedProperties, TakeActionProperties, TypedDict
):
    pass


class TakeActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TakeAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TakeActionProperties, TakeActionInheritedProperties, TakeActionAllProperties
    ] = TakeActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TakeAction"
    return model


TakeAction = create_schema_org_model()


def create_takeaction_model(
    model: Union[
        TakeActionProperties, TakeActionInheritedProperties, TakeActionAllProperties
    ]
):
    _type = deepcopy(TakeActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TakeAction. Please see: https://schema.org/TakeAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TakeActionAllProperties):
    pydantic_type = create_takeaction_model(model=model)
    return pydantic_type(model).schema_json()
