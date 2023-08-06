"""
The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.Related actions:* [[TakeAction]]: Reciprocal of GiveAction.* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).

https://schema.org/GiveAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GiveActionInheritedProperties(TypedDict):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.Related actions:* [[TakeAction]]: Reciprocal of GiveAction.* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).

    References:
        https://schema.org/GiveAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fromLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class GiveActionProperties(TypedDict):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.Related actions:* [[TakeAction]]: Reciprocal of GiveAction.* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).

    References:
        https://schema.org/GiveAction
    Note:
        Model Depth 4
    Attributes:
        recipient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The participant who is at the receiving end of the action.
    """

    recipient: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(GiveActionInheritedProperties , GiveActionProperties, TypedDict):
    pass


class GiveActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GiveAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'recipient': {'exclude': True}}
        


def create_schema_org_model(type_: Union[GiveActionProperties, GiveActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GiveAction"
    return model
    

GiveAction = create_schema_org_model()


def create_giveaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_giveaction_model(model=model)
    return pydantic_type(model).schema_json()


