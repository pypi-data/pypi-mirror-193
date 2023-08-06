"""
The price asked for a given offer by the respective organization or person.

https://schema.org/UnitPriceSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UnitPriceSpecificationInheritedProperties(TypedDict):
    """The price asked for a given offer by the respective organization or person.

    References:
        https://schema.org/UnitPriceSpecification
    Note:
        Model Depth 5
    Attributes:
        eligibleQuantity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
        valueAddedTaxIncluded: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.
        minPrice: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The lowest price if the price is a range.
        price: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
        validThrough: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        maxPrice: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The highest price if the price is a range.
        validFrom: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The date when the item becomes valid.
        eligibleTransactionVolume: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.
        priceCurrency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    eligibleQuantity: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    valueAddedTaxIncluded: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    minPrice: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    price: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    validThrough: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    maxPrice: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    validFrom: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    eligibleTransactionVolume: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    priceCurrency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class UnitPriceSpecificationProperties(TypedDict):
    """The price asked for a given offer by the respective organization or person.

    References:
        https://schema.org/UnitPriceSpecification
    Note:
        Model Depth 5
    Attributes:
        priceType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Defines the type of a price specified for an offered product, for example a list price, a (temporary) sale price or a manufacturer suggested retail price. If multiple prices are specified for an offer the [[priceType]] property can be used to identify the type of each such specified price. The value of priceType can be specified as a value from enumeration PriceTypeEnumeration or as a free form text string for price types that are not already predefined in PriceTypeEnumeration.
        priceComponentType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifies a price component (for example, a line item on an invoice), part of the total price for an offer.
        billingStart: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Specifies after how much time this price (or price component) becomes valid and billing starts. Can be used, for example, to model a price increase after the first year of a subscription. The unit of measurement is specified by the unitCode property.
        unitCode: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
        billingDuration: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Specifies for how long this price (or price component) will be billed. Can be used, for example, to model the contractual duration of a subscription or payment plan. Type can be either a Duration or a Number (in which case the unit of measurement, for example month, is specified by the unitCode property).
        unitText: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for<a href='unitCode'>unitCode</a>.
        referenceQuantity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The reference quantity for which a certain price applies, e.g. 1 EUR per 4 kWh of electricity. This property is a replacement for unitOfMeasurement for the advanced cases where the price does not relate to a standard unit.
        billingIncrement: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.
    """

    priceType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    priceComponentType: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    billingStart: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    unitCode: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    billingDuration: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    unitText: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    referenceQuantity: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    billingIncrement: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class UnitPriceSpecificationAllProperties(
    UnitPriceSpecificationInheritedProperties,
    UnitPriceSpecificationProperties,
    TypedDict,
):
    pass


class UnitPriceSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UnitPriceSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"eligibleQuantity": {"exclude": True}}
        fields = {"valueAddedTaxIncluded": {"exclude": True}}
        fields = {"minPrice": {"exclude": True}}
        fields = {"price": {"exclude": True}}
        fields = {"validThrough": {"exclude": True}}
        fields = {"maxPrice": {"exclude": True}}
        fields = {"validFrom": {"exclude": True}}
        fields = {"eligibleTransactionVolume": {"exclude": True}}
        fields = {"priceCurrency": {"exclude": True}}
        fields = {"priceType": {"exclude": True}}
        fields = {"priceComponentType": {"exclude": True}}
        fields = {"billingStart": {"exclude": True}}
        fields = {"unitCode": {"exclude": True}}
        fields = {"billingDuration": {"exclude": True}}
        fields = {"unitText": {"exclude": True}}
        fields = {"referenceQuantity": {"exclude": True}}
        fields = {"billingIncrement": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        UnitPriceSpecificationProperties,
        UnitPriceSpecificationInheritedProperties,
        UnitPriceSpecificationAllProperties,
    ] = UnitPriceSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UnitPriceSpecification"
    return model


UnitPriceSpecification = create_schema_org_model()


def create_unitpricespecification_model(
    model: Union[
        UnitPriceSpecificationProperties,
        UnitPriceSpecificationInheritedProperties,
        UnitPriceSpecificationAllProperties,
    ]
):
    _type = deepcopy(UnitPriceSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of UnitPriceSpecificationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UnitPriceSpecificationAllProperties):
    pydantic_type = create_unitpricespecification_model(model=model)
    return pydantic_type(model).schema_json()
