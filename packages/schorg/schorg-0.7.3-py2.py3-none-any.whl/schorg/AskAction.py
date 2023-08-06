"""
The act of posing a question / favor to someone.Related actions:* [[ReplyAction]]: Appears generally as a response to AskAction.

https://schema.org/AskAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AskActionInheritedProperties(TypedDict):
    """The act of posing a question / favor to someone.Related actions:* [[ReplyAction]]: Appears generally as a response to AskAction.

    References:
        https://schema.org/AskAction
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


class AskActionProperties(TypedDict):
    """The act of posing a question / favor to someone.Related actions:* [[ReplyAction]]: Appears generally as a response to AskAction.

    References:
        https://schema.org/AskAction
    Note:
        Model Depth 5
    Attributes:
        question: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. A question.
    """

    question: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class AskActionAllProperties(
    AskActionInheritedProperties, AskActionProperties, TypedDict
):
    pass


class AskActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AskAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"about": {"exclude": True}}
        fields = {"recipient": {"exclude": True}}
        fields = {"language": {"exclude": True}}
        fields = {"inLanguage": {"exclude": True}}
        fields = {"question": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AskActionProperties, AskActionInheritedProperties, AskActionAllProperties
    ] = AskActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AskAction"
    return model


AskAction = create_schema_org_model()


def create_askaction_model(
    model: Union[
        AskActionProperties, AskActionInheritedProperties, AskActionAllProperties
    ]
):
    _type = deepcopy(AskActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AskActionAllProperties):
    pydantic_type = create_askaction_model(model=model)
    return pydantic_type(model).schema_json()
