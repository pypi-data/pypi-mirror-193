"""
An agent bookmarks/flags/labels/tags/marks an object.

https://schema.org/BookmarkAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BookmarkActionInheritedProperties(TypedDict):
    """An agent bookmarks/flags/labels/tags/marks an object.

    References:
        https://schema.org/BookmarkAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class BookmarkActionProperties(TypedDict):
    """An agent bookmarks/flags/labels/tags/marks an object.

    References:
        https://schema.org/BookmarkAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(BookmarkActionInheritedProperties , BookmarkActionProperties, TypedDict):
    pass


class BookmarkActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BookmarkAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BookmarkActionProperties, BookmarkActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BookmarkAction"
    return model
    

BookmarkAction = create_schema_org_model()


def create_bookmarkaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bookmarkaction_model(model=model)
    return pydantic_type(model).schema_json()


