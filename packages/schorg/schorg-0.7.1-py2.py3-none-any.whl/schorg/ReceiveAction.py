"""
The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.Related actions:* [[SendAction]]: The reciprocal of ReceiveAction.* [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transferred (e.g. I can receive a package, but it does not mean the package is now mine).

https://schema.org/ReceiveAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReceiveActionInheritedProperties(TypedDict):
    """The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.Related actions:* [[SendAction]]: The reciprocal of ReceiveAction.* [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transferred (e.g. I can receive a package, but it does not mean the package is now mine).

    References:
        https://schema.org/ReceiveAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class ReceiveActionProperties(TypedDict):
    """The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.Related actions:* [[SendAction]]: The reciprocal of ReceiveAction.* [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transferred (e.g. I can receive a package, but it does not mean the package is now mine).

    References:
        https://schema.org/ReceiveAction
    Note:
        Model Depth 4
    Attributes:
        deliveryMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The method of delivery.
        sender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the sending end of the action.
    """

    deliveryMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sender: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(ReceiveActionInheritedProperties , ReceiveActionProperties, TypedDict):
    pass


class ReceiveActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReceiveAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'deliveryMethod': {'exclude': True}}
        fields = {'sender': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ReceiveActionProperties, ReceiveActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReceiveAction"
    return model
    

ReceiveAction = create_schema_org_model()


def create_receiveaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_receiveaction_model(model=model)
    return pydantic_type(model).schema_json()


