"""
The act of ingesting information/resources/food.

https://schema.org/ConsumeAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ConsumeActionInheritedProperties(TypedDict):
    """The act of ingesting information/resources/food.

    References:
        https://schema.org/ConsumeAction
    Note:
        Model Depth 3
    Attributes:
        endTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        provider: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        startTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        result: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The result produced in the action. E.g. John wrote *a book*.
        actionStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the current disposition of the Action.
        agent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote a book.
        instrument: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.
        object: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). E.g. John read *a book*.
        error: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): For failed actions, more information on the cause of the failure.
        target: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Indicates a target EntryPoint, or url, for an Action.
        location: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        participant: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Other co-agents that participated in the action indirectly. E.g. John wrote a book with *Steve*.
    """

    endTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    startTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    result: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    actionStatus: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    agent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    instrument: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    object: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    error: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    target: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    location: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    participant: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class ConsumeActionProperties(TypedDict):
    """The act of ingesting information/resources/food.

    References:
        https://schema.org/ConsumeAction
    Note:
        Model Depth 3
    Attributes:
        actionAccessibilityRequirement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    """

    actionAccessibilityRequirement: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    expectsAcceptanceOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(ConsumeActionInheritedProperties , ConsumeActionProperties, TypedDict):
    pass


class ConsumeActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ConsumeAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'endTime': {'exclude': True}}
        fields = {'provider': {'exclude': True}}
        fields = {'startTime': {'exclude': True}}
        fields = {'result': {'exclude': True}}
        fields = {'actionStatus': {'exclude': True}}
        fields = {'agent': {'exclude': True}}
        fields = {'instrument': {'exclude': True}}
        fields = {'object': {'exclude': True}}
        fields = {'error': {'exclude': True}}
        fields = {'target': {'exclude': True}}
        fields = {'location': {'exclude': True}}
        fields = {'participant': {'exclude': True}}
        fields = {'actionAccessibilityRequirement': {'exclude': True}}
        fields = {'expectsAcceptanceOf': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ConsumeActionProperties, ConsumeActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ConsumeAction"
    return model
    

ConsumeAction = create_schema_org_model()


def create_consumeaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_consumeaction_model(model=model)
    return pydantic_type(model).schema_json()


