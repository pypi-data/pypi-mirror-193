"""
Original definition: "provider of professional services."The general [[ProfessionalService]] type for local businesses was deprecated due to confusion with [[Service]]. For reference, the types that it included were: [[Dentist]],        [[AccountingService]], [[Attorney]], [[Notary]], as well as types for several kinds of [[HomeAndConstructionBusiness]]: [[Electrician]], [[GeneralContractor]],        [[HousePainter]], [[Locksmith]], [[Plumber]], [[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive supertype of [[Attorney]].

https://schema.org/ProfessionalService
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ProfessionalServiceInheritedProperties(TypedDict):
    """Original definition: "provider of professional services."The general [[ProfessionalService]] type for local businesses was deprecated due to confusion with [[Service]]. For reference, the types that it included were: [[Dentist]],        [[AccountingService]], [[Attorney]], [[Notary]], as well as types for several kinds of [[HomeAndConstructionBusiness]]: [[Electrician]], [[GeneralContractor]],        [[HousePainter]], [[Locksmith]], [[Plumber]], [[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive supertype of [[Attorney]].

    References:
        https://schema.org/ProfessionalService
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


class ProfessionalServiceProperties(TypedDict):
    """Original definition: "provider of professional services."The general [[ProfessionalService]] type for local businesses was deprecated due to confusion with [[Service]]. For reference, the types that it included were: [[Dentist]],        [[AccountingService]], [[Attorney]], [[Notary]], as well as types for several kinds of [[HomeAndConstructionBusiness]]: [[Electrician]], [[GeneralContractor]],        [[HousePainter]], [[Locksmith]], [[Plumber]], [[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive supertype of [[Attorney]].

    References:
        https://schema.org/ProfessionalService
    Note:
        Model Depth 4
    Attributes:
    """


class ProfessionalServiceAllProperties(
    ProfessionalServiceInheritedProperties, ProfessionalServiceProperties, TypedDict
):
    pass


class ProfessionalServiceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ProfessionalService", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"priceRange": {"exclude": True}}
        fields = {"currenciesAccepted": {"exclude": True}}
        fields = {"branchOf": {"exclude": True}}
        fields = {"paymentAccepted": {"exclude": True}}
        fields = {"openingHours": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ProfessionalServiceProperties,
        ProfessionalServiceInheritedProperties,
        ProfessionalServiceAllProperties,
    ] = ProfessionalServiceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ProfessionalService"
    return model


ProfessionalService = create_schema_org_model()


def create_professionalservice_model(
    model: Union[
        ProfessionalServiceProperties,
        ProfessionalServiceInheritedProperties,
        ProfessionalServiceAllProperties,
    ]
):
    _type = deepcopy(ProfessionalServiceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ProfessionalServiceAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ProfessionalServiceAllProperties):
    pydantic_type = create_professionalservice_model(model=model)
    return pydantic_type(model).schema_json()
