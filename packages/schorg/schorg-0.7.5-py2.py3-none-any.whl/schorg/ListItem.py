"""
An list item, e.g. a step in a checklist or how-to description.

https://schema.org/ListItem
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ListItemInheritedProperties(TypedDict):
    """An list item, e.g. a step in a checklist or how-to description.

    References:
        https://schema.org/ListItem
    Note:
        Model Depth 3
    Attributes:
    """


class ListItemProperties(TypedDict):
    """An list item, e.g. a step in a checklist or how-to description.

    References:
        https://schema.org/ListItem
    Note:
        Model Depth 3
    Attributes:
        item: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').
        nextItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A link to the ListItem that follows the current one.
        previousItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A link to the ListItem that precedes the current one.
        position: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The position of an item in a series or sequence of items.
    """

    item: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nextItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    previousItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    position: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]


class ListItemAllProperties(ListItemInheritedProperties, ListItemProperties, TypedDict):
    pass


class ListItemBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ListItem", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"item": {"exclude": True}}
        fields = {"nextItem": {"exclude": True}}
        fields = {"previousItem": {"exclude": True}}
        fields = {"position": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ListItemProperties, ListItemInheritedProperties, ListItemAllProperties
    ] = ListItemAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ListItem"
    return model


ListItem = create_schema_org_model()


def create_listitem_model(
    model: Union[ListItemProperties, ListItemInheritedProperties, ListItemAllProperties]
):
    _type = deepcopy(ListItemAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ListItem. Please see: https://schema.org/ListItem"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ListItemAllProperties):
    pydantic_type = create_listitem_model(model=model)
    return pydantic_type(model).schema_json()
