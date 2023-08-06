"""
A single item within a larger data feed.

https://schema.org/DataFeedItem
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        item: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').
        dateCreated: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date on which the CreativeWork was created or the item was added to a DataFeed.
        dateDeleted: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The datetime the item was removed from the DataFeed.
        dateModified: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
    """

    item: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    dateCreated: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    dateDeleted: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    dateModified: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]


class DataFeedItemAllProperties(
    DataFeedItemInheritedProperties, DataFeedItemProperties, TypedDict
):
    pass


class DataFeedItemBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DataFeedItem", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"item": {"exclude": True}}
        fields = {"dateCreated": {"exclude": True}}
        fields = {"dateDeleted": {"exclude": True}}
        fields = {"dateModified": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DataFeedItemProperties,
        DataFeedItemInheritedProperties,
        DataFeedItemAllProperties,
    ] = DataFeedItemAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DataFeedItem"
    return model


DataFeedItem = create_schema_org_model()


def create_datafeeditem_model(
    model: Union[
        DataFeedItemProperties,
        DataFeedItemInheritedProperties,
        DataFeedItemAllProperties,
    ]
):
    _type = deepcopy(DataFeedItemAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DataFeedItem. Please see: https://schema.org/DataFeedItem"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DataFeedItemAllProperties):
    pydantic_type = create_datafeeditem_model(model=model)
    return pydantic_type(model).schema_json()
