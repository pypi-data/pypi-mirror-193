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
        confirmationNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A number that confirms the given order or payment has been received.
        broker: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        paymentDueDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The date that payment is due.
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        totalPaymentDue: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The total amount due.
        accountId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The identifier for the account the payment will be applied to.
        customer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Party placing the order or paying the invoice.
        paymentDue: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The date that payment is due.
        billingPeriod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The time interval used to compute the invoice.
        paymentMethodId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An identifier for the method of payment used (e.g. the last 4 digits of the credit card).
        paymentStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The status of payment; whether the invoice has been paid or not.
        paymentMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The name of the credit card or other method of payment for the order.
        scheduledPaymentDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date the invoice is scheduled to be paid.
        referencesOrder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice.
        category: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        minimumPaymentDue: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The minimum payment required at this time.
    """

    confirmationNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    broker: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    paymentDueDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    totalPaymentDue: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    accountId: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    customer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    paymentDue: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    billingPeriod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    paymentMethodId: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    paymentStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    paymentMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    scheduledPaymentDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    referencesOrder: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    category: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    minimumPaymentDue: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
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
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: InvoiceAllProperties):
    pydantic_type = create_invoice_model(model=model)
    return pydantic_type(model).schema_json()
