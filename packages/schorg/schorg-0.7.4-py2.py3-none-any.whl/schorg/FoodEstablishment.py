"""
A food-related business.

https://schema.org/FoodEstablishment
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FoodEstablishmentInheritedProperties(TypedDict):
    """A food-related business.

    References:
        https://schema.org/FoodEstablishment
    Note:
        Model Depth 4
    Attributes:
        priceRange: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The price range of the business, for example ```$$$```.
        currenciesAccepted: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency accepted.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        branchOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The larger organization that this local business is a branch of, if any. Not to be confused with (anatomical) [[branch]].
        paymentAccepted: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc.
        openingHours: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. * Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>.
    """

    priceRange: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    currenciesAccepted: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    branchOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentAccepted: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    openingHours: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class FoodEstablishmentProperties(TypedDict):
    """A food-related business.

    References:
        https://schema.org/FoodEstablishment
    Note:
        Model Depth 4
    Attributes:
        starRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).
        servesCuisine: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The cuisine of the restaurant.
        acceptsReservations: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str, StrictBool]], AnyUrl, SchemaOrgObj, str, StrictBool]]): Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings ```Yes``` or ```No```.
        menu: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Either the actual menu as a structured representation, as text, or a URL of the menu.
        hasMenu: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Either the actual menu as a structured representation, as text, or a URL of the menu.
    """

    starRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    servesCuisine: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    acceptsReservations: NotRequired[
        Union[
            List[Union[AnyUrl, SchemaOrgObj, str, StrictBool]],
            AnyUrl,
            SchemaOrgObj,
            str,
            StrictBool,
        ]
    ]
    menu: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    hasMenu: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class FoodEstablishmentAllProperties(
    FoodEstablishmentInheritedProperties, FoodEstablishmentProperties, TypedDict
):
    pass


class FoodEstablishmentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FoodEstablishment", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"priceRange": {"exclude": True}}
        fields = {"currenciesAccepted": {"exclude": True}}
        fields = {"branchOf": {"exclude": True}}
        fields = {"paymentAccepted": {"exclude": True}}
        fields = {"openingHours": {"exclude": True}}
        fields = {"starRating": {"exclude": True}}
        fields = {"servesCuisine": {"exclude": True}}
        fields = {"acceptsReservations": {"exclude": True}}
        fields = {"menu": {"exclude": True}}
        fields = {"hasMenu": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        FoodEstablishmentProperties,
        FoodEstablishmentInheritedProperties,
        FoodEstablishmentAllProperties,
    ] = FoodEstablishmentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FoodEstablishment"
    return model


FoodEstablishment = create_schema_org_model()


def create_foodestablishment_model(
    model: Union[
        FoodEstablishmentProperties,
        FoodEstablishmentInheritedProperties,
        FoodEstablishmentAllProperties,
    ]
):
    _type = deepcopy(FoodEstablishmentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FoodEstablishmentAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FoodEstablishmentAllProperties):
    pydantic_type = create_foodestablishment_model(model=model)
    return pydantic_type(model).schema_json()
