"""
The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

https://schema.org/SellAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SellActionInheritedProperties(TypedDict):
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

    References:
        https://schema.org/SellAction
    Note:
        Model Depth 4
    Attributes:
        price: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
        priceSpecification: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): One or more detailed price specifications, indicating the unit price and delivery or payment charges.
        priceCurrency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    price: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    priceSpecification: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    priceCurrency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class SellActionProperties(TypedDict):
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

    References:
        https://schema.org/SellAction
    Note:
        Model Depth 4
    Attributes:
        buyer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The participant/person/organization that bought the object.
        warrantyPromise: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The warranty promise(s) included in the offer.
    """

    buyer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    warrantyPromise: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class SellActionAllProperties(
    SellActionInheritedProperties, SellActionProperties, TypedDict
):
    pass


class SellActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SellAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"price": {"exclude": True}}
        fields = {"priceSpecification": {"exclude": True}}
        fields = {"priceCurrency": {"exclude": True}}
        fields = {"buyer": {"exclude": True}}
        fields = {"warrantyPromise": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SellActionProperties, SellActionInheritedProperties, SellActionAllProperties
    ] = SellActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SellAction"
    return model


SellAction = create_schema_org_model()


def create_sellaction_model(
    model: Union[
        SellActionProperties, SellActionInheritedProperties, SellActionAllProperties
    ]
):
    _type = deepcopy(SellActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SellActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SellActionAllProperties):
    pydantic_type = create_sellaction_model(model=model)
    return pydantic_type(model).schema_json()
