"""
An agent leaves an event / group with participants/friends at a location.Related actions:* [[JoinAction]]: The antonym of LeaveAction.* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.

https://schema.org/LeaveAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LeaveActionInheritedProperties(TypedDict):
    """An agent leaves an event / group with participants/friends at a location.Related actions:* [[JoinAction]]: The antonym of LeaveAction.* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.

    References:
        https://schema.org/LeaveAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class LeaveActionProperties(TypedDict):
    """An agent leaves an event / group with participants/friends at a location.Related actions:* [[JoinAction]]: The antonym of LeaveAction.* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.

    References:
        https://schema.org/LeaveAction
    Note:
        Model Depth 4
    Attributes:
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
    """

    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(LeaveActionInheritedProperties , LeaveActionProperties, TypedDict):
    pass


class LeaveActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LeaveAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'event': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LeaveActionProperties, LeaveActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LeaveAction"
    return model
    

LeaveAction = create_schema_org_model()


def create_leaveaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_leaveaction_model(model=model)
    return pydantic_type(model).schema_json()


