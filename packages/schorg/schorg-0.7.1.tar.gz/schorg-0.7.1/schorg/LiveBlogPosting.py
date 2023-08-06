"""
A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates.

https://schema.org/LiveBlogPosting
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LiveBlogPostingInheritedProperties(TypedDict):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates.

    References:
        https://schema.org/LiveBlogPosting
    Note:
        Model Depth 6
    Attributes:
    """

    


class LiveBlogPostingProperties(TypedDict):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates.

    References:
        https://schema.org/LiveBlogPosting
    Note:
        Model Depth 6
    Attributes:
        liveBlogUpdate: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An update to the LiveBlog.
        coverageStartTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The time when the live blog will begin covering the Event. Note that coverage may begin before the Event's start time. The LiveBlogPosting may also be created before coverage begins.
        coverageEndTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The time when the live blog will stop covering the Event. Note that coverage may continue after the Event concludes.
    """

    liveBlogUpdate: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    coverageStartTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    coverageEndTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    


class AllProperties(LiveBlogPostingInheritedProperties , LiveBlogPostingProperties, TypedDict):
    pass


class LiveBlogPostingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LiveBlogPosting",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'liveBlogUpdate': {'exclude': True}}
        fields = {'coverageStartTime': {'exclude': True}}
        fields = {'coverageEndTime': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LiveBlogPostingProperties, LiveBlogPostingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LiveBlogPosting"
    return model
    

LiveBlogPosting = create_schema_org_model()


def create_liveblogposting_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_liveblogposting_model(model=model)
    return pydantic_type(model).schema_json()


