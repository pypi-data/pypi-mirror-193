"""
An item used as either a tool or supply when performing the instructions for how to achieve a result.

https://schema.org/HowToItem
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HowToItemInheritedProperties(TypedDict):
    """An item used as either a tool or supply when performing the instructions for how to achieve a result.

    References:
        https://schema.org/HowToItem
    Note:
        Model Depth 4
    Attributes:
        item: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').
        nextItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A link to the ListItem that follows the current one.
        previousItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A link to the ListItem that precedes the current one.
        position: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The position of an item in a series or sequence of items.
    """

    item: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nextItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    previousItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    position: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]


class HowToItemProperties(TypedDict):
    """An item used as either a tool or supply when performing the instructions for how to achieve a result.

    References:
        https://schema.org/HowToItem
    Note:
        Model Depth 4
    Attributes:
        requiredQuantity: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The required quantity of the item(s).
    """

    requiredQuantity: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]


class HowToItemAllProperties(
    HowToItemInheritedProperties, HowToItemProperties, TypedDict
):
    pass


class HowToItemBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HowToItem", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"item": {"exclude": True}}
        fields = {"nextItem": {"exclude": True}}
        fields = {"previousItem": {"exclude": True}}
        fields = {"position": {"exclude": True}}
        fields = {"requiredQuantity": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HowToItemProperties, HowToItemInheritedProperties, HowToItemAllProperties
    ] = HowToItemAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HowToItem"
    return model


HowToItem = create_schema_org_model()


def create_howtoitem_model(
    model: Union[
        HowToItemProperties, HowToItemInheritedProperties, HowToItemAllProperties
    ]
):
    _type = deepcopy(HowToItemAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HowToItemAllProperties):
    pydantic_type = create_howtoitem_model(model=model)
    return pydantic_type(model).schema_json()
