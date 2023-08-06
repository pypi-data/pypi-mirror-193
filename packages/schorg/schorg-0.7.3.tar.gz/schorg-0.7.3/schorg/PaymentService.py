"""
A Service to transfer funds from a person or organization to a beneficiary person or organization.

https://schema.org/PaymentService
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentServiceInheritedProperties(TypedDict):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization.

    References:
        https://schema.org/PaymentService
    Note:
        Model Depth 5
    Attributes:
        annualPercentageRate: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.
        interestRate: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    annualPercentageRate: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    interestRate: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    feesAndCommissionsSpecification: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]


class PaymentServiceProperties(TypedDict):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization.

    References:
        https://schema.org/PaymentService
    Note:
        Model Depth 5
    Attributes:
    """


class PaymentServiceAllProperties(
    PaymentServiceInheritedProperties, PaymentServiceProperties, TypedDict
):
    pass


class PaymentServiceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentService", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"annualPercentageRate": {"exclude": True}}
        fields = {"interestRate": {"exclude": True}}
        fields = {"feesAndCommissionsSpecification": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PaymentServiceProperties,
        PaymentServiceInheritedProperties,
        PaymentServiceAllProperties,
    ] = PaymentServiceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentService"
    return model


PaymentService = create_schema_org_model()


def create_paymentservice_model(
    model: Union[
        PaymentServiceProperties,
        PaymentServiceInheritedProperties,
        PaymentServiceAllProperties,
    ]
):
    _type = deepcopy(PaymentServiceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PaymentServiceAllProperties):
    pydantic_type = create_paymentservice_model(model=model)
    return pydantic_type(model).schema_json()
