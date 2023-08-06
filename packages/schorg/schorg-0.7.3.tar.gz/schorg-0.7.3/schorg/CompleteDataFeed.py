"""
A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes content for every item currently in the feed.This is the equivalent of Atom's element as defined in Feed Paging and Archiving [RFC 5005](https://tools.ietf.org/html/rfc5005), for example (and as defined for Atom), when using data from a feed that represents a collection of items that varies over time (e.g. "Top Twenty Records") there is no need to have newer entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed, old entries can be safely discarded when the feed is refreshed, since we can assume the feed has provided descriptions for all current items.

https://schema.org/CompleteDataFeed
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CompleteDataFeedInheritedProperties(TypedDict):
    """A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes content for every item currently in the feed.This is the equivalent of Atom's element as defined in Feed Paging and Archiving [RFC 5005](https://tools.ietf.org/html/rfc5005), for example (and as defined for Atom), when using data from a feed that represents a collection of items that varies over time (e.g. "Top Twenty Records") there is no need to have newer entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed, old entries can be safely discarded when the feed is refreshed, since we can assume the feed has provided descriptions for all current items.

    References:
        https://schema.org/CompleteDataFeed
    Note:
        Model Depth 5
    Attributes:
        dataFeedElement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An item within a data feed. Data feeds may have many elements.
    """

    dataFeedElement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class CompleteDataFeedProperties(TypedDict):
    """A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes content for every item currently in the feed.This is the equivalent of Atom's element as defined in Feed Paging and Archiving [RFC 5005](https://tools.ietf.org/html/rfc5005), for example (and as defined for Atom), when using data from a feed that represents a collection of items that varies over time (e.g. "Top Twenty Records") there is no need to have newer entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed, old entries can be safely discarded when the feed is refreshed, since we can assume the feed has provided descriptions for all current items.

    References:
        https://schema.org/CompleteDataFeed
    Note:
        Model Depth 5
    Attributes:
    """


class CompleteDataFeedAllProperties(
    CompleteDataFeedInheritedProperties, CompleteDataFeedProperties, TypedDict
):
    pass


class CompleteDataFeedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CompleteDataFeed", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"dataFeedElement": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CompleteDataFeedProperties,
        CompleteDataFeedInheritedProperties,
        CompleteDataFeedAllProperties,
    ] = CompleteDataFeedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CompleteDataFeed"
    return model


CompleteDataFeed = create_schema_org_model()


def create_completedatafeed_model(
    model: Union[
        CompleteDataFeedProperties,
        CompleteDataFeedInheritedProperties,
        CompleteDataFeedAllProperties,
    ]
):
    _type = deepcopy(CompleteDataFeedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CompleteDataFeedAllProperties):
    pydantic_type = create_completedatafeed_model(model=model)
    return pydantic_type(model).schema_json()
