"""
The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.

https://schema.org/CommunicateAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CommunicateActionInheritedProperties(TypedDict):
    """The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.

    References:
        https://schema.org/CommunicateAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class CommunicateActionProperties(TypedDict):
    """The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.

    References:
        https://schema.org/CommunicateAction
    Note:
        Model Depth 4
    Attributes:
        about: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The subject matter of the content.
        recipient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The participant who is at the receiving end of the action.
        language: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of instrument. The language used on this action.
        inLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
    """

    about: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recipient: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    language: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(CommunicateActionInheritedProperties , CommunicateActionProperties, TypedDict):
    pass


class CommunicateActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CommunicateAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'about': {'exclude': True}}
        fields = {'recipient': {'exclude': True}}
        fields = {'language': {'exclude': True}}
        fields = {'inLanguage': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CommunicateActionProperties, CommunicateActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CommunicateAction"
    return model
    

CommunicateAction = create_schema_org_model()


def create_communicateaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_communicateaction_model(model=model)
    return pydantic_type(model).schema_json()


