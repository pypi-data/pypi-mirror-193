"""
A list of possible product availability options.

https://schema.org/ItemAvailability
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ItemAvailabilityInheritedProperties(TypedDict):
    """A list of possible product availability options.

    References:
        https://schema.org/ItemAvailability
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ItemAvailabilityProperties(TypedDict):
    """A list of possible product availability options.

    References:
        https://schema.org/ItemAvailability
    Note:
        Model Depth 4
    Attributes:
    """


class ItemAvailabilityAllProperties(
    ItemAvailabilityInheritedProperties, ItemAvailabilityProperties, TypedDict
):
    pass


class ItemAvailabilityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ItemAvailability", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ItemAvailabilityProperties,
        ItemAvailabilityInheritedProperties,
        ItemAvailabilityAllProperties,
    ] = ItemAvailabilityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ItemAvailability"
    return model


ItemAvailability = create_schema_org_model()


def create_itemavailability_model(
    model: Union[
        ItemAvailabilityProperties,
        ItemAvailabilityInheritedProperties,
        ItemAvailabilityAllProperties,
    ]
):
    _type = deepcopy(ItemAvailabilityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ItemAvailabilityAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ItemAvailabilityAllProperties):
    pydantic_type = create_itemavailability_model(model=model)
    return pydantic_type(model).schema_json()
