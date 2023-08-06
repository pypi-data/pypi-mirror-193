"""
Physical activity that is engaged to help maintain posture and balance.

https://schema.org/Balance
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BalanceInheritedProperties(TypedDict):
    """Physical activity that is engaged to help maintain posture and balance.

    References:
        https://schema.org/Balance
    Note:
        Model Depth 5
    Attributes:
    """


class BalanceProperties(TypedDict):
    """Physical activity that is engaged to help maintain posture and balance.

    References:
        https://schema.org/Balance
    Note:
        Model Depth 5
    Attributes:
    """


class BalanceAllProperties(BalanceInheritedProperties, BalanceProperties, TypedDict):
    pass


class BalanceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Balance", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BalanceProperties, BalanceInheritedProperties, BalanceAllProperties
    ] = BalanceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Balance"
    return model


Balance = create_schema_org_model()


def create_balance_model(
    model: Union[BalanceProperties, BalanceInheritedProperties, BalanceAllProperties]
):
    _type = deepcopy(BalanceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BalanceAllProperties):
    pydantic_type = create_balance_model(model=model)
    return pydantic_type(model).schema_json()
