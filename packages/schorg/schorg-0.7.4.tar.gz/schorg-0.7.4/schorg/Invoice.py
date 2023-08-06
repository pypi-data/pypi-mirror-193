"""
A statement of the money due for goods or services; a bill.

https://schema.org/Invoice
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InvoiceInheritedProperties(TypedDict):
    """A statement of the money due for goods or services; a bill.

    References:
        https://schema.org/Invoice
    Note:
        Model Depth 3
    Attributes:
    """


class InvoiceProperties(TypedDict):
    """A statement of the money due for goods or services; a bill.

    References:
        https://schema.org/Invoice
    Note:
        Model Depth 3
    Attributes:
        confirmationNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A number that confirms the given order or payment has been received.
        broker: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        paymentDueDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The date that payment is due.
        provider: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        totalPaymentDue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The total amount due.
        accountId: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The identifier for the account the payment will be applied to.
        customer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Party placing the order or paying the invoice.
        paymentDue: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The date that payment is due.
        billingPeriod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The time interval used to compute the invoice.
        paymentMethodId: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An identifier for the method of payment used (e.g. the last 4 digits of the credit card).
        paymentStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The status of payment; whether the invoice has been paid or not.
        paymentMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name of the credit card or other method of payment for the order.
        scheduledPaymentDate: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): The date the invoice is scheduled to be paid.
        referencesOrder: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice.
        category: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        minimumPaymentDue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The minimum payment required at this time.
    """

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
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    totalPaymentDue: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    accountId: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    customer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentDue: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    billingPeriod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentMethodId: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    paymentStatus: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    paymentMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    scheduledPaymentDate: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]
    referencesOrder: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    category: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    minimumPaymentDue: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class InvoiceAllProperties(InvoiceInheritedProperties, InvoiceProperties, TypedDict):
    pass


class InvoiceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Invoice", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"confirmationNumber": {"exclude": True}}
        fields = {"broker": {"exclude": True}}
        fields = {"paymentDueDate": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"totalPaymentDue": {"exclude": True}}
        fields = {"accountId": {"exclude": True}}
        fields = {"customer": {"exclude": True}}
        fields = {"paymentDue": {"exclude": True}}
        fields = {"billingPeriod": {"exclude": True}}
        fields = {"paymentMethodId": {"exclude": True}}
        fields = {"paymentStatus": {"exclude": True}}
        fields = {"paymentMethod": {"exclude": True}}
        fields = {"scheduledPaymentDate": {"exclude": True}}
        fields = {"referencesOrder": {"exclude": True}}
        fields = {"category": {"exclude": True}}
        fields = {"minimumPaymentDue": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        InvoiceProperties, InvoiceInheritedProperties, InvoiceAllProperties
    ] = InvoiceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Invoice"
    return model


Invoice = create_schema_org_model()


def create_invoice_model(
    model: Union[InvoiceProperties, InvoiceInheritedProperties, InvoiceAllProperties]
):
    _type = deepcopy(InvoiceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of InvoiceAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: InvoiceAllProperties):
    pydantic_type = create_invoice_model(model=model)
    return pydantic_type(model).schema_json()
