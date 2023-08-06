"""
The act of finding an object.Related actions:* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.

https://schema.org/FindAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FindActionInheritedProperties(TypedDict):
    """The act of finding an object.Related actions:* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.

    References:
        https://schema.org/FindAction
    Note:
        Model Depth 3
    Attributes:
        endTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        startTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        result: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The result produced in the action. E.g. John wrote *a book*.
        actionStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the current disposition of the Action.
        agent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote a book.
        instrument: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.
        object: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). E.g. John read *a book*.
        error: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): For failed actions, more information on the cause of the failure.
        target: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates a target EntryPoint, or url, for an Action.
        location: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        participant: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Other co-agents that participated in the action indirectly. E.g. John wrote a book with *Steve*.
    """

    endTime: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startTime: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    result: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    agent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    instrument: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    object: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    error: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    target: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    location: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    participant: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class FindActionProperties(TypedDict):
    """The act of finding an object.Related actions:* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.

    References:
        https://schema.org/FindAction
    Note:
        Model Depth 3
    Attributes:
    """


class FindActionAllProperties(
    FindActionInheritedProperties, FindActionProperties, TypedDict
):
    pass


class FindActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FindAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"endTime": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"startTime": {"exclude": True}}
        fields = {"result": {"exclude": True}}
        fields = {"actionStatus": {"exclude": True}}
        fields = {"agent": {"exclude": True}}
        fields = {"instrument": {"exclude": True}}
        fields = {"object": {"exclude": True}}
        fields = {"error": {"exclude": True}}
        fields = {"target": {"exclude": True}}
        fields = {"location": {"exclude": True}}
        fields = {"participant": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        FindActionProperties, FindActionInheritedProperties, FindActionAllProperties
    ] = FindActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FindAction"
    return model


FindAction = create_schema_org_model()


def create_findaction_model(
    model: Union[
        FindActionProperties, FindActionInheritedProperties, FindActionAllProperties
    ]
):
    _type = deepcopy(FindActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FindActionAllProperties):
    pydantic_type = create_findaction_model(model=model)
    return pydantic_type(model).schema_json()
