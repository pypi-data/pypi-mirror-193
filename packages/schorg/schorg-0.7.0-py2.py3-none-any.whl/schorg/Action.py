"""
An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.See also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html) and [Actions overview document](https://schema.org/docs/actions.html).

https://schema.org/Action
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActionInheritedProperties(TypedDict):
    """An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.See also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html) and [Actions overview document](https://schema.org/docs/actions.html).

    References:
        https://schema.org/Action
    Note:
        Model Depth 2
    Attributes:
        potentialAction: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.
        mainEntityOfPage: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.
        subjectOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A CreativeWork or Event about this Thing.
        url: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): URL of the item.
        alternateName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An alias for the item.
        sameAs: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
        description: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A description of the item.
        disambiguatingDescription: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.
        identifier: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.        
        image: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].
        name: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name of the item.
        additionalType: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.
    """

    potentialAction: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    mainEntityOfPage: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    subjectOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    url: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    alternateName: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sameAs: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    description: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    disambiguatingDescription: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    identifier: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    image: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    name: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    additionalType: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class ActionProperties(TypedDict):
    """An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.See also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html) and [Actions overview document](https://schema.org/docs/actions.html).

    References:
        https://schema.org/Action
    Note:
        Model Depth 2
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
    


class AllProperties(ActionInheritedProperties , ActionProperties, TypedDict):
    pass


class ActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Action",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'potentialAction': {'exclude': True}}
        fields = {'mainEntityOfPage': {'exclude': True}}
        fields = {'subjectOf': {'exclude': True}}
        fields = {'url': {'exclude': True}}
        fields = {'alternateName': {'exclude': True}}
        fields = {'sameAs': {'exclude': True}}
        fields = {'description': {'exclude': True}}
        fields = {'disambiguatingDescription': {'exclude': True}}
        fields = {'identifier': {'exclude': True}}
        fields = {'image': {'exclude': True}}
        fields = {'name': {'exclude': True}}
        fields = {'additionalType': {'exclude': True}}
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
        


def create_schema_org_model(type_: Union[ActionProperties, ActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Action"
    return model
    

Action = create_schema_org_model()


def create_action_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_action_model(model=model)
    return pydantic_type(model).schema_json()


