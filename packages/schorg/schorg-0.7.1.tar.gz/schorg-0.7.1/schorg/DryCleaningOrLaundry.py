"""
A dry-cleaning business.

https://schema.org/DryCleaningOrLaundry
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DryCleaningOrLaundryInheritedProperties(TypedDict):
    """A dry-cleaning business.

    References:
        https://schema.org/DryCleaningOrLaundry
    Note:
        Model Depth 4
    Attributes:
        priceRange: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The price range of the business, for example ```$$$```.
        currenciesAccepted: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency accepted.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        branchOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The larger organization that this local business is a branch of, if any. Not to be confused with (anatomical) [[branch]].
        paymentAccepted: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc.
        openingHours: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. * Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>.
    """

    priceRange: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    currenciesAccepted: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    branchOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    paymentAccepted: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    openingHours: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class DryCleaningOrLaundryProperties(TypedDict):
    """A dry-cleaning business.

    References:
        https://schema.org/DryCleaningOrLaundry
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DryCleaningOrLaundryInheritedProperties , DryCleaningOrLaundryProperties, TypedDict):
    pass


class DryCleaningOrLaundryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DryCleaningOrLaundry",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'priceRange': {'exclude': True}}
        fields = {'currenciesAccepted': {'exclude': True}}
        fields = {'branchOf': {'exclude': True}}
        fields = {'paymentAccepted': {'exclude': True}}
        fields = {'openingHours': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DryCleaningOrLaundryProperties, DryCleaningOrLaundryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DryCleaningOrLaundry"
    return model
    

DryCleaningOrLaundry = create_schema_org_model()


def create_drycleaningorlaundry_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_drycleaningorlaundry_model(model=model)
    return pydantic_type(model).schema_json()


