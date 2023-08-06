"""
The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:* [[ReceiveAction]]: The reciprocal of SendAction.* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).

https://schema.org/SendAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SendActionInheritedProperties(TypedDict):
    """The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:* [[ReceiveAction]]: The reciprocal of SendAction.* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    References:
        https://schema.org/SendAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class SendActionProperties(TypedDict):
    """The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:* [[ReceiveAction]]: The reciprocal of SendAction.* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    References:
        https://schema.org/SendAction
    Note:
        Model Depth 4
    Attributes:
        deliveryMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The method of delivery.
        recipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the receiving end of the action.
    """

    deliveryMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    recipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(SendActionInheritedProperties , SendActionProperties, TypedDict):
    pass


class SendActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SendAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'deliveryMethod': {'exclude': True}}
        fields = {'recipient': {'exclude': True}}
        


def create_schema_org_model(type_: Union[SendActionProperties, SendActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SendAction"
    return model
    

SendAction = create_schema_org_model()


def create_sendaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_sendaction_model(model=model)
    return pydantic_type(model).schema_json()


