"""
A structured value representing repayment.

https://schema.org/RepaymentSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RepaymentSpecificationInheritedProperties(TypedDict):
    """A structured value representing repayment.

    References:
        https://schema.org/RepaymentSpecification
    Note:
        Model Depth 4
    Attributes:
    """


class RepaymentSpecificationProperties(TypedDict):
    """A structured value representing repayment.

    References:
        https://schema.org/RepaymentSpecification
    Note:
        Model Depth 4
    Attributes:
        loanPaymentAmount: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount of money to pay in a single payment.
        earlyPrepaymentPenalty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount to be paid as a penalty in the event of early payment of the loan.
        numberOfLoanPayments: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of payments contractually required at origination to repay the loan. For monthly paying loans this is the number of months from the contractual first payment date to the maturity date.
        loanPaymentFrequency: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Frequency of payments due, i.e. number of months between payments. This is defined as a frequency, i.e. the reciprocal of a period of time.
        downPayment: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): a type of payment made in cash during the onset of the purchase of an expensive good/service. The payment typically represents only a percentage of the full purchase price.
    """

    loanPaymentAmount: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    earlyPrepaymentPenalty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    numberOfLoanPayments: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    loanPaymentFrequency: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    downPayment: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]


class RepaymentSpecificationAllProperties(
    RepaymentSpecificationInheritedProperties,
    RepaymentSpecificationProperties,
    TypedDict,
):
    pass


class RepaymentSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RepaymentSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"loanPaymentAmount": {"exclude": True}}
        fields = {"earlyPrepaymentPenalty": {"exclude": True}}
        fields = {"numberOfLoanPayments": {"exclude": True}}
        fields = {"loanPaymentFrequency": {"exclude": True}}
        fields = {"downPayment": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RepaymentSpecificationProperties,
        RepaymentSpecificationInheritedProperties,
        RepaymentSpecificationAllProperties,
    ] = RepaymentSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RepaymentSpecification"
    return model


RepaymentSpecification = create_schema_org_model()


def create_repaymentspecification_model(
    model: Union[
        RepaymentSpecificationProperties,
        RepaymentSpecificationInheritedProperties,
        RepaymentSpecificationAllProperties,
    ]
):
    _type = deepcopy(RepaymentSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RepaymentSpecificationAllProperties):
    pydantic_type = create_repaymentspecification_model(model=model)
    return pydantic_type(model).schema_json()
