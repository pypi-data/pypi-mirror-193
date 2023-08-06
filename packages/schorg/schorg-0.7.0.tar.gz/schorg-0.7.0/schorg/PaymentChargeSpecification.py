"""
The costs of settling the payment using a particular payment method.

https://schema.org/PaymentChargeSpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentChargeSpecificationInheritedProperties(TypedDict):
    """The costs of settling the payment using a particular payment method.

    References:
        https://schema.org/PaymentChargeSpecification
    Note:
        Model Depth 5
    Attributes:
        eligibleQuantity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
        valueAddedTaxIncluded: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.
        minPrice: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The lowest price if the price is a range.
        price: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.      
        validThrough: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        maxPrice: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The highest price if the price is a range.
        validFrom: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date when the item becomes valid.
        eligibleTransactionVolume: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.
        priceCurrency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    eligibleQuantity: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    valueAddedTaxIncluded: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    minPrice: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    price: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    validThrough: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    maxPrice: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    validFrom: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    eligibleTransactionVolume: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    priceCurrency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class PaymentChargeSpecificationProperties(TypedDict):
    """The costs of settling the payment using a particular payment method.

    References:
        https://schema.org/PaymentChargeSpecification
    Note:
        Model Depth 5
    Attributes:
        appliesToPaymentMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The payment method(s) to which the payment charge specification applies.
        appliesToDeliveryMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The delivery method(s) to which the delivery charge or payment charge specification applies.
    """

    appliesToPaymentMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    appliesToDeliveryMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(PaymentChargeSpecificationInheritedProperties , PaymentChargeSpecificationProperties, TypedDict):
    pass


class PaymentChargeSpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PaymentChargeSpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'eligibleQuantity': {'exclude': True}}
        fields = {'valueAddedTaxIncluded': {'exclude': True}}
        fields = {'minPrice': {'exclude': True}}
        fields = {'price': {'exclude': True}}
        fields = {'validThrough': {'exclude': True}}
        fields = {'maxPrice': {'exclude': True}}
        fields = {'validFrom': {'exclude': True}}
        fields = {'eligibleTransactionVolume': {'exclude': True}}
        fields = {'priceCurrency': {'exclude': True}}
        fields = {'appliesToPaymentMethod': {'exclude': True}}
        fields = {'appliesToDeliveryMethod': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PaymentChargeSpecificationProperties, PaymentChargeSpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentChargeSpecification"
    return model
    

PaymentChargeSpecification = create_schema_org_model()


def create_paymentchargespecification_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_paymentchargespecification_model(model=model)
    return pydantic_type(model).schema_json()


