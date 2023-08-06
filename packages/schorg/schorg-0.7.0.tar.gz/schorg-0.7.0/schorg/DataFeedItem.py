"""
A single item within a larger data feed.

https://schema.org/DataFeedItem
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DataFeedItemInheritedProperties(TypedDict):
    """A single item within a larger data feed.

    References:
        https://schema.org/DataFeedItem
    Note:
        Model Depth 3
    Attributes:
    """

    


class DataFeedItemProperties(TypedDict):
    """A single item within a larger data feed.

    References:
        https://schema.org/DataFeedItem
    Note:
        Model Depth 3
    Attributes:
        item: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').
        dateCreated: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date on which the CreativeWork was created or the item was added to a DataFeed.
        dateDeleted: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The datetime the item was removed from the DataFeed.
        dateModified: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
    """

    item: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    dateCreated: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    dateDeleted: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    dateModified: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    


class AllProperties(DataFeedItemInheritedProperties , DataFeedItemProperties, TypedDict):
    pass


class DataFeedItemBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DataFeedItem",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'item': {'exclude': True}}
        fields = {'dateCreated': {'exclude': True}}
        fields = {'dateDeleted': {'exclude': True}}
        fields = {'dateModified': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DataFeedItemProperties, DataFeedItemInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DataFeedItem"
    return model
    

DataFeedItem = create_schema_org_model()


def create_datafeeditem_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_datafeeditem_model(model=model)
    return pydantic_type(model).schema_json()


