"""
An email message.

https://schema.org/EmailMessage
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EmailMessageInheritedProperties(TypedDict):
    """An email message.

    References:
        https://schema.org/EmailMessage
    Note:
        Model Depth 4
    Attributes:
        dateReceived: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The date/time the message was received if a single recipient exists.
        recipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the receiving end of the action.
        messageAttachment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A CreativeWork attached to the message.
        ccRecipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of recipient. The recipient copied on a message.
        bccRecipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of recipient. The recipient blind copied on a message.
        dateRead: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date/time at which the message has been read by the recipient if a single recipient exists.
        dateSent: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The date/time at which the message was sent.
        sender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the sending end of the action.
        toRecipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of recipient. The recipient who was directly sent the message.
    """

    dateReceived: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    recipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    messageAttachment: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ccRecipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bccRecipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    dateRead: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    dateSent: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    sender: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    toRecipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class EmailMessageProperties(TypedDict):
    """An email message.

    References:
        https://schema.org/EmailMessage
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(EmailMessageInheritedProperties , EmailMessageProperties, TypedDict):
    pass


class EmailMessageBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EmailMessage",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'dateReceived': {'exclude': True}}
        fields = {'recipient': {'exclude': True}}
        fields = {'messageAttachment': {'exclude': True}}
        fields = {'ccRecipient': {'exclude': True}}
        fields = {'bccRecipient': {'exclude': True}}
        fields = {'dateRead': {'exclude': True}}
        fields = {'dateSent': {'exclude': True}}
        fields = {'sender': {'exclude': True}}
        fields = {'toRecipient': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EmailMessageProperties, EmailMessageInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EmailMessage"
    return model
    

EmailMessage = create_schema_org_model()


def create_emailmessage_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_emailmessage_model(model=model)
    return pydantic_type(model).schema_json()


