"""
A food or drink item listed in a menu or menu section.

https://schema.org/MenuItem
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MenuItemInheritedProperties(TypedDict):
    """A food or drink item listed in a menu or menu section.

    References:
        https://schema.org/MenuItem
    Note:
        Model Depth 3
    Attributes:
    """


class MenuItemProperties(TypedDict):
    """A food or drink item listed in a menu or menu section.

    References:
        https://schema.org/MenuItem
    Note:
        Model Depth 3
    Attributes:
        nutrition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Nutrition information about the recipe or menu item.
        suitableForDiet: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a dietary restriction or guideline for which this recipe or menu item is suitable, e.g. diabetic, halal etc.
        menuAddOn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Additional menu item(s) such as a side dish of salad or side order of fries that can be added to this menu item. Additionally it can be a menu section containing allowed add-on menu items for this menu item.
        offers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
    """

    nutrition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    suitableForDiet: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    menuAddOn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class MenuItemAllProperties(MenuItemInheritedProperties, MenuItemProperties, TypedDict):
    pass


class MenuItemBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MenuItem", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"nutrition": {"exclude": True}}
        fields = {"suitableForDiet": {"exclude": True}}
        fields = {"menuAddOn": {"exclude": True}}
        fields = {"offers": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MenuItemProperties, MenuItemInheritedProperties, MenuItemAllProperties
    ] = MenuItemAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MenuItem"
    return model


MenuItem = create_schema_org_model()


def create_menuitem_model(
    model: Union[MenuItemProperties, MenuItemInheritedProperties, MenuItemAllProperties]
):
    _type = deepcopy(MenuItemAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MenuItemAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MenuItemAllProperties):
    pydantic_type = create_menuitem_model(model=model)
    return pydantic_type(model).schema_json()
