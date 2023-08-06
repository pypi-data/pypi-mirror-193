"""
The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:* [[ReceiveAction]]: The reciprocal of SendAction.* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).

https://schema.org/SendAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SendActionInheritedProperties(TypedDict):
    """The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:* [[ReceiveAction]]: The reciprocal of SendAction.* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    References:
        https://schema.org/SendAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fromLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class SendActionProperties(TypedDict):
    """The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:* [[ReceiveAction]]: The reciprocal of SendAction.* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    References:
        https://schema.org/SendAction
    Note:
        Model Depth 4
    Attributes:
        deliveryMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of instrument. The method of delivery.
        recipient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The participant who is at the receiving end of the action.
    """

    deliveryMethod: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    recipient: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class SendActionAllProperties(
    SendActionInheritedProperties, SendActionProperties, TypedDict
):
    pass


class SendActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SendAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}
        fields = {"deliveryMethod": {"exclude": True}}
        fields = {"recipient": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SendActionProperties, SendActionInheritedProperties, SendActionAllProperties
    ] = SendActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SendAction"
    return model


SendAction = create_schema_org_model()


def create_sendaction_model(
    model: Union[
        SendActionProperties, SendActionInheritedProperties, SendActionAllProperties
    ]
):
    _type = deepcopy(SendActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SendActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SendActionAllProperties):
    pydantic_type = create_sendaction_model(model=model)
    return pydantic_type(model).schema_json()
