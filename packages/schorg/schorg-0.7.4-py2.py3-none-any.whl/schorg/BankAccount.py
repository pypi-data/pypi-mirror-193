"""
A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.

https://schema.org/BankAccount
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BankAccountInheritedProperties(TypedDict):
    """A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.

    References:
        https://schema.org/BankAccount
    Note:
        Model Depth 5
    Attributes:
        annualPercentageRate: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.
        interestRate: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    annualPercentageRate: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    interestRate: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    feesAndCommissionsSpecification: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class BankAccountProperties(TypedDict):
    """A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.

    References:
        https://schema.org/BankAccount
    Note:
        Model Depth 5
    Attributes:
        accountMinimumInflow: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A minimum amount that has to be paid in every month.
        accountOverdraftLimit: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An overdraft is an extension of credit from a lending institution when an account reaches zero. An overdraft allows the individual to continue withdrawing money even if the account has no funds in it. Basically the bank allows people to borrow a set amount of money.
        bankAccountType: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The type of a bank account.
    """

    accountMinimumInflow: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    accountOverdraftLimit: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    bankAccountType: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class BankAccountAllProperties(
    BankAccountInheritedProperties, BankAccountProperties, TypedDict
):
    pass


class BankAccountBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BankAccount", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"annualPercentageRate": {"exclude": True}}
        fields = {"interestRate": {"exclude": True}}
        fields = {"feesAndCommissionsSpecification": {"exclude": True}}
        fields = {"accountMinimumInflow": {"exclude": True}}
        fields = {"accountOverdraftLimit": {"exclude": True}}
        fields = {"bankAccountType": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BankAccountProperties, BankAccountInheritedProperties, BankAccountAllProperties
    ] = BankAccountAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BankAccount"
    return model


BankAccount = create_schema_org_model()


def create_bankaccount_model(
    model: Union[
        BankAccountProperties, BankAccountInheritedProperties, BankAccountAllProperties
    ]
):
    _type = deepcopy(BankAccountAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BankAccountAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BankAccountAllProperties):
    pydantic_type = create_bankaccount_model(model=model)
    return pydantic_type(model).schema_json()
