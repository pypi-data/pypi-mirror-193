"""
A lodging business, such as a motel, hotel, or inn.

https://schema.org/LodgingBusiness
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LodgingBusinessInheritedProperties(TypedDict):
    """A lodging business, such as a motel, hotel, or inn.

    References:
        https://schema.org/LodgingBusiness
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
    currenciesAccepted: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    branchOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentAccepted: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    openingHours: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class LodgingBusinessProperties(TypedDict):
    """A lodging business, such as a motel, hotel, or inn.

    References:
        https://schema.org/LodgingBusiness
    Note:
        Model Depth 4
    Attributes:
        numberOfRooms: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        availableLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        amenityFeature: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        checkoutTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The latest someone may check out of a lodging establishment.
        starRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).
        audience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An intended audience, i.e. a group for whom something was created.
        petsAllowed: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        checkinTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The earliest someone may check into a lodging establishment.
    """

    numberOfRooms: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    availableLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    amenityFeature: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    checkoutTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    starRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    audience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    petsAllowed: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    checkinTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    


class AllProperties(LodgingBusinessInheritedProperties , LodgingBusinessProperties, TypedDict):
    pass


class LodgingBusinessBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LodgingBusiness",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'priceRange': {'exclude': True}}
        fields = {'currenciesAccepted': {'exclude': True}}
        fields = {'branchOf': {'exclude': True}}
        fields = {'paymentAccepted': {'exclude': True}}
        fields = {'openingHours': {'exclude': True}}
        fields = {'numberOfRooms': {'exclude': True}}
        fields = {'availableLanguage': {'exclude': True}}
        fields = {'amenityFeature': {'exclude': True}}
        fields = {'checkoutTime': {'exclude': True}}
        fields = {'starRating': {'exclude': True}}
        fields = {'audience': {'exclude': True}}
        fields = {'petsAllowed': {'exclude': True}}
        fields = {'checkinTime': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LodgingBusinessProperties, LodgingBusinessInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LodgingBusiness"
    return model
    

LodgingBusiness = create_schema_org_model()


def create_lodgingbusiness_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_lodgingbusiness_model(model=model)
    return pydantic_type(model).schema_json()


