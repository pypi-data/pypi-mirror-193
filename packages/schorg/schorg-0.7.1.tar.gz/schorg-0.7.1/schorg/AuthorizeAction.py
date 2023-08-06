"""
The act of granting permission to an object.

https://schema.org/AuthorizeAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AuthorizeActionInheritedProperties(TypedDict):
    """The act of granting permission to an object.

    References:
        https://schema.org/AuthorizeAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AuthorizeActionProperties(TypedDict):
    """The act of granting permission to an object.

    References:
        https://schema.org/AuthorizeAction
    Note:
        Model Depth 5
    Attributes:
        recipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the receiving end of the action.
    """

    recipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(AuthorizeActionInheritedProperties , AuthorizeActionProperties, TypedDict):
    pass


class AuthorizeActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AuthorizeAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'recipient': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AuthorizeActionProperties, AuthorizeActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AuthorizeAction"
    return model
    

AuthorizeAction = create_schema_org_model()


def create_authorizeaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_authorizeaction_model(model=model)
    return pydantic_type(model).schema_json()


