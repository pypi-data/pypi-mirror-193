"""
An over the air or online broadcast event.

https://schema.org/BroadcastEvent
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BroadcastEventInheritedProperties(TypedDict):
    """An over the air or online broadcast event.

    References:
        https://schema.org/BroadcastEvent
    Note:
        Model Depth 4
    Attributes:
        publishedBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An agent associated with the publication event.
        free: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): A flag to signal that the item, event, or place is accessible for free.
        publishedOn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A broadcast service associated with the publication event.
    """

    publishedBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    free: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    publishedOn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class BroadcastEventProperties(TypedDict):
    """An over the air or online broadcast event.

    References:
        https://schema.org/BroadcastEvent
    Note:
        Model Depth 4
    Attributes:
        subtitleLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).
        broadcastOfEvent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The event being broadcast such as a sporting event or awards ceremony.
        videoFormat: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).
        isLiveBroadcast: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): True if the broadcast is of a live event.
    """

    subtitleLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    broadcastOfEvent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    videoFormat: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isLiveBroadcast: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    


class AllProperties(BroadcastEventInheritedProperties , BroadcastEventProperties, TypedDict):
    pass


class BroadcastEventBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BroadcastEvent",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'publishedBy': {'exclude': True}}
        fields = {'free': {'exclude': True}}
        fields = {'publishedOn': {'exclude': True}}
        fields = {'subtitleLanguage': {'exclude': True}}
        fields = {'broadcastOfEvent': {'exclude': True}}
        fields = {'videoFormat': {'exclude': True}}
        fields = {'isLiveBroadcast': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BroadcastEventProperties, BroadcastEventInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BroadcastEvent"
    return model
    

BroadcastEvent = create_schema_org_model()


def create_broadcastevent_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_broadcastevent_model(model=model)
    return pydantic_type(model).schema_json()


