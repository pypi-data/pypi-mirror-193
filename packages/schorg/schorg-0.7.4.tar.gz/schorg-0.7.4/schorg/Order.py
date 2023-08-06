"""
An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.

https://schema.org/Order
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderInheritedProperties(TypedDict):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.

    References:
        https://schema.org/Order
    Note:
        Model Depth 3
    Attributes:
    """


class OrderProperties(TypedDict):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.

    References:
        https://schema.org/Order
    Note:
        Model Depth 3
    Attributes:
        orderStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The current status of the order.
        isGift: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether the offer was accepted as a gift for someone other than the buyer.
        confirmationNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A number that confirms the given order or payment has been received.
        broker: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        paymentDueDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The date that payment is due.
        seller: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        discount: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Any discount applied (to an Order).
        discountCurrency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency of the discount.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        customer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Party placing the order or paying the invoice.
        paymentDue: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The date that payment is due.
        acceptedOffer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The offer(s) -- e.g., product, quantity and price combinations -- included in the order.
        paymentMethodId: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An identifier for the method of payment used (e.g. the last 4 digits of the credit card).
        merchant: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): 'merchant' is an out-dated term for 'seller'.
        partOfInvoice: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The order is being paid as part of the referenced Invoice.
        orderNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The identifier of the transaction.
        paymentMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name of the credit card or other method of payment for the order.
        discountCode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Code used to redeem a discount.
        orderDelivery: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The delivery of the parcel related to this order or order item.
        orderedItem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The item ordered.
        billingAddress: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The billing address for the order.
        paymentUrl: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The URL for sending a payment.
        orderDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): Date order was placed.
    """

    orderStatus: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isGift: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    confirmationNumber: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    broker: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentDueDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    seller: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    discount: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    discountCurrency: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    customer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentDue: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    acceptedOffer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentMethodId: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    merchant: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfInvoice: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    orderNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    discountCode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    orderDelivery: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    orderedItem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    billingAddress: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    paymentUrl: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    orderDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]


class OrderAllProperties(OrderInheritedProperties, OrderProperties, TypedDict):
    pass


class OrderBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Order", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"orderStatus": {"exclude": True}}
        fields = {"isGift": {"exclude": True}}
        fields = {"confirmationNumber": {"exclude": True}}
        fields = {"broker": {"exclude": True}}
        fields = {"paymentDueDate": {"exclude": True}}
        fields = {"seller": {"exclude": True}}
        fields = {"discount": {"exclude": True}}
        fields = {"discountCurrency": {"exclude": True}}
        fields = {"customer": {"exclude": True}}
        fields = {"paymentDue": {"exclude": True}}
        fields = {"acceptedOffer": {"exclude": True}}
        fields = {"paymentMethodId": {"exclude": True}}
        fields = {"merchant": {"exclude": True}}
        fields = {"partOfInvoice": {"exclude": True}}
        fields = {"orderNumber": {"exclude": True}}
        fields = {"paymentMethod": {"exclude": True}}
        fields = {"discountCode": {"exclude": True}}
        fields = {"orderDelivery": {"exclude": True}}
        fields = {"orderedItem": {"exclude": True}}
        fields = {"billingAddress": {"exclude": True}}
        fields = {"paymentUrl": {"exclude": True}}
        fields = {"orderDate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OrderProperties, OrderInheritedProperties, OrderAllProperties
    ] = OrderAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Order"
    return model


Order = create_schema_org_model()


def create_order_model(
    model: Union[OrderProperties, OrderInheritedProperties, OrderAllProperties]
):
    _type = deepcopy(OrderAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OrderAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OrderAllProperties):
    pydantic_type = create_order_model(model=model)
    return pydantic_type(model).schema_json()
