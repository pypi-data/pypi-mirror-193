"""
The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).Related actions:* [[CheckOutAction]]: The antonym of CheckInAction.* [[ArriveAction]]: Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.* [[ConfirmAction]]: Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the *start* of a previously reserved service rather than its validity/existence.

https://schema.org/CheckInAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CheckInActionInheritedProperties(TypedDict):
    """The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).Related actions:* [[CheckOutAction]]: The antonym of CheckInAction.* [[ArriveAction]]: Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.* [[ConfirmAction]]: Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the *start* of a previously reserved service rather than its validity/existence.

    References:
        https://schema.org/CheckInAction
    Note:
        Model Depth 5
    Attributes:
        about: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The subject matter of the content.
        recipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the receiving end of the action.
        language: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The language used on this action.
        inLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
    """

    about: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    recipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    language: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    inLanguage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class CheckInActionProperties(TypedDict):
    """The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).Related actions:* [[CheckOutAction]]: The antonym of CheckInAction.* [[ArriveAction]]: Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.* [[ConfirmAction]]: Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the *start* of a previously reserved service rather than its validity/existence.

    References:
        https://schema.org/CheckInAction
    Note:
        Model Depth 5
    Attributes:
    """


class CheckInActionAllProperties(
    CheckInActionInheritedProperties, CheckInActionProperties, TypedDict
):
    pass


class CheckInActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CheckInAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"about": {"exclude": True}}
        fields = {"recipient": {"exclude": True}}
        fields = {"language": {"exclude": True}}
        fields = {"inLanguage": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CheckInActionProperties,
        CheckInActionInheritedProperties,
        CheckInActionAllProperties,
    ] = CheckInActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CheckInAction"
    return model


CheckInAction = create_schema_org_model()


def create_checkinaction_model(
    model: Union[
        CheckInActionProperties,
        CheckInActionInheritedProperties,
        CheckInActionAllProperties,
    ]
):
    _type = deepcopy(CheckInActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CheckInActionAllProperties):
    pydantic_type = create_checkinaction_model(model=model)
    return pydantic_type(model).schema_json()
