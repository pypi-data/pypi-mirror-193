"""
The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.

https://schema.org/TransferAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TransferActionInheritedProperties(TypedDict):
    """The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.

    References:
        https://schema.org/TransferAction
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
        target: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Indicates a target EntryPoint, or url, for an Action.
        location: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        participant: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Other co-agents that participated in the action indirectly. E.g. John wrote a book with *Steve*.
    """

    endTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    startTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    result: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    actionStatus: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    agent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    instrument: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    object: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    error: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    target: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    location: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    participant: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class TransferActionProperties(TypedDict):
    """The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.

    References:
        https://schema.org/TransferAction
    Note:
        Model Depth 3
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fromLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class TransferActionAllProperties(
    TransferActionInheritedProperties, TransferActionProperties, TypedDict
):
    pass


class TransferActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TransferAction", alias="@id")
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
        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TransferActionProperties,
        TransferActionInheritedProperties,
        TransferActionAllProperties,
    ] = TransferActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TransferAction"
    return model


TransferAction = create_schema_org_model()


def create_transferaction_model(
    model: Union[
        TransferActionProperties,
        TransferActionInheritedProperties,
        TransferActionAllProperties,
    ]
):
    _type = deepcopy(TransferActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of TransferActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TransferActionAllProperties):
    pydantic_type = create_transferaction_model(model=model)
    return pydantic_type(model).schema_json()
