"""
The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

https://schema.org/ReturnAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnActionInheritedProperties(TypedDict):
    """The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

    References:
        https://schema.org/ReturnAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fromLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class ReturnActionProperties(TypedDict):
    """The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

    References:
        https://schema.org/ReturnAction
    Note:
        Model Depth 4
    Attributes:
        recipient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The participant who is at the receiving end of the action.
    """

    recipient: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(ReturnActionInheritedProperties , ReturnActionProperties, TypedDict):
    pass


class ReturnActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReturnAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'recipient': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ReturnActionProperties, ReturnActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnAction"
    return model
    

ReturnAction = create_schema_org_model()


def create_returnaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_returnaction_model(model=model)
    return pydantic_type(model).schema_json()


