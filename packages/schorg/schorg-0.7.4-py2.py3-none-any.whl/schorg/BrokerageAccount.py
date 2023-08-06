"""
An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.

https://schema.org/BrokerageAccount
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BrokerageAccountInheritedProperties(TypedDict):
    """An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.

    References:
        https://schema.org/BrokerageAccount
    Note:
        Model Depth 6
    Attributes:
        amount: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The amount of money.
    """

    amount: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class BrokerageAccountProperties(TypedDict):
    """An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.

    References:
        https://schema.org/BrokerageAccount
    Note:
        Model Depth 6
    Attributes:
    """


class BrokerageAccountAllProperties(
    BrokerageAccountInheritedProperties, BrokerageAccountProperties, TypedDict
):
    pass


class BrokerageAccountBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BrokerageAccount", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"amount": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BrokerageAccountProperties,
        BrokerageAccountInheritedProperties,
        BrokerageAccountAllProperties,
    ] = BrokerageAccountAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BrokerageAccount"
    return model


BrokerageAccount = create_schema_org_model()


def create_brokerageaccount_model(
    model: Union[
        BrokerageAccountProperties,
        BrokerageAccountInheritedProperties,
        BrokerageAccountAllProperties,
    ]
):
    _type = deepcopy(BrokerageAccountAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BrokerageAccountAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BrokerageAccountAllProperties):
    pydantic_type = create_brokerageaccount_model(model=model)
    return pydantic_type(model).schema_json()
