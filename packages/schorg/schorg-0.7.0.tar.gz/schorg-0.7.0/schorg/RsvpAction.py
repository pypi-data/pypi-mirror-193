"""
The act of notifying an event organizer as to whether you expect to attend the event.

https://schema.org/RsvpAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RsvpActionInheritedProperties(TypedDict):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    References:
        https://schema.org/RsvpAction
    Note:
        Model Depth 6
    Attributes:
        event: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Upcoming or past event associated with this place, organization, or action.
    """

    event: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class RsvpActionProperties(TypedDict):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    References:
        https://schema.org/RsvpAction
    Note:
        Model Depth 6
    Attributes:
        additionalNumberOfGuests: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): If responding yes, the number of guests who will attend in addition to the invitee.
        comment: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Comments, typically from users.
        rsvpResponse: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The response (yes, no, maybe) to the RSVP.
    """

    additionalNumberOfGuests: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    comment: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    rsvpResponse: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(RsvpActionInheritedProperties , RsvpActionProperties, TypedDict):
    pass


class RsvpActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RsvpAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'event': {'exclude': True}}
        fields = {'additionalNumberOfGuests': {'exclude': True}}
        fields = {'comment': {'exclude': True}}
        fields = {'rsvpResponse': {'exclude': True}}
        


def create_schema_org_model(type_: Union[RsvpActionProperties, RsvpActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RsvpAction"
    return model
    

RsvpAction = create_schema_org_model()


def create_rsvpaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_rsvpaction_model(model=model)
    return pydantic_type(model).schema_json()


