"""
A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.

https://schema.org/DepositAccount
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DepositAccountInheritedProperties(TypedDict):
    """A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.

    References:
        https://schema.org/DepositAccount
    Note:
        Model Depth 6
    Attributes:
        accountMinimumInflow: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A minimum amount that has to be paid in every month.
        accountOverdraftLimit: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An overdraft is an extension of credit from a lending institution when an account reaches zero. An overdraft allows the individual to continue withdrawing money even if the account has no funds in it. Basically the bank allows people to borrow a set amount of money.
        bankAccountType: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The type of a bank account.
        amount: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The amount of money.
    """

    accountMinimumInflow: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    accountOverdraftLimit: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    bankAccountType: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    amount: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class DepositAccountProperties(TypedDict):
    """A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.

    References:
        https://schema.org/DepositAccount
    Note:
        Model Depth 6
    Attributes:
    """


class DepositAccountAllProperties(
    DepositAccountInheritedProperties, DepositAccountProperties, TypedDict
):
    pass


class DepositAccountBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DepositAccount", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"accountMinimumInflow": {"exclude": True}}
        fields = {"accountOverdraftLimit": {"exclude": True}}
        fields = {"bankAccountType": {"exclude": True}}
        fields = {"amount": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DepositAccountProperties,
        DepositAccountInheritedProperties,
        DepositAccountAllProperties,
    ] = DepositAccountAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DepositAccount"
    return model


DepositAccount = create_schema_org_model()


def create_depositaccount_model(
    model: Union[
        DepositAccountProperties,
        DepositAccountInheritedProperties,
        DepositAccountAllProperties,
    ]
):
    _type = deepcopy(DepositAccountAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DepositAccount. Please see: https://schema.org/DepositAccount"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DepositAccountAllProperties):
    pydantic_type = create_depositaccount_model(model=model)
    return pydantic_type(model).schema_json()
