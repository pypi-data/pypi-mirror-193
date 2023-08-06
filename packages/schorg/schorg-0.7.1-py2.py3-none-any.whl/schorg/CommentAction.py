"""
The act of generating a comment about a subject.

https://schema.org/CommentAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CommentActionInheritedProperties(TypedDict):
    """The act of generating a comment about a subject.

    References:
        https://schema.org/CommentAction
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
    


class CommentActionProperties(TypedDict):
    """The act of generating a comment about a subject.

    References:
        https://schema.org/CommentAction
    Note:
        Model Depth 5
    Attributes:
        resultComment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of result. The Comment created or sent as a result of this action.
    """

    resultComment: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(CommentActionInheritedProperties , CommentActionProperties, TypedDict):
    pass


class CommentActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CommentAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'about': {'exclude': True}}
        fields = {'recipient': {'exclude': True}}
        fields = {'language': {'exclude': True}}
        fields = {'inLanguage': {'exclude': True}}
        fields = {'resultComment': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CommentActionProperties, CommentActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CommentAction"
    return model
    

CommentAction = create_schema_org_model()


def create_commentaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_commentaction_model(model=model)
    return pydantic_type(model).schema_json()


