"""
A [[comment]] that corrects [[CreativeWork]].

https://schema.org/CorrectionComment
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CorrectionCommentInheritedProperties(TypedDict):
    """A [[comment]] that corrects [[CreativeWork]].

    References:
        https://schema.org/CorrectionComment
    Note:
        Model Depth 4
    Attributes:
        parentItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The parent of a question, answer or item in general.
        downvoteCount: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of downvotes this question, answer or comment has received from the community.
        upvoteCount: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of upvotes this question, answer or comment has received from the community.
    """

    parentItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    downvoteCount: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    upvoteCount: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    


class CorrectionCommentProperties(TypedDict):
    """A [[comment]] that corrects [[CreativeWork]].

    References:
        https://schema.org/CorrectionComment
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(CorrectionCommentInheritedProperties , CorrectionCommentProperties, TypedDict):
    pass


class CorrectionCommentBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CorrectionComment",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'parentItem': {'exclude': True}}
        fields = {'downvoteCount': {'exclude': True}}
        fields = {'upvoteCount': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CorrectionCommentProperties, CorrectionCommentInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CorrectionComment"
    return model
    

CorrectionComment = create_schema_org_model()


def create_correctioncomment_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_correctioncomment_model(model=model)
    return pydantic_type(model).schema_json()


