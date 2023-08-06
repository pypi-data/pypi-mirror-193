"""
A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.

https://schema.org/InteractionCounter
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InteractionCounterInheritedProperties(TypedDict):
    """A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.

    References:
        https://schema.org/InteractionCounter
    Note:
        Model Depth 4
    Attributes:
    """

    


class InteractionCounterProperties(TypedDict):
    """A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.

    References:
        https://schema.org/InteractionCounter
    Note:
        Model Depth 4
    Attributes:
        endTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        startTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        interactionType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Action representing the type of interaction. For up votes, +1s, etc. use [[LikeAction]]. For down votes use [[DislikeAction]]. Otherwise, use the most specific Action.
        interactionService: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The WebSite or SoftwareApplication where the interactions took place.
        userInteractionCount: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.
        location: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
    """

    endTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    startTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    interactionType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    interactionService: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    userInteractionCount: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    location: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(InteractionCounterInheritedProperties , InteractionCounterProperties, TypedDict):
    pass


class InteractionCounterBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InteractionCounter",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'endTime': {'exclude': True}}
        fields = {'startTime': {'exclude': True}}
        fields = {'interactionType': {'exclude': True}}
        fields = {'interactionService': {'exclude': True}}
        fields = {'userInteractionCount': {'exclude': True}}
        fields = {'location': {'exclude': True}}
        


def create_schema_org_model(type_: Union[InteractionCounterProperties, InteractionCounterInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InteractionCounter"
    return model
    

InteractionCounter = create_schema_org_model()


def create_interactioncounter_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_interactioncounter_model(model=model)
    return pydantic_type(model).schema_json()


