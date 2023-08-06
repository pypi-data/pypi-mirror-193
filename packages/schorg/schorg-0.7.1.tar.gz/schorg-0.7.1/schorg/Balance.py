"""
Physical activity that is engaged to help maintain posture and balance.

https://schema.org/Balance
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(BalanceInheritedProperties , BalanceProperties, TypedDict):
    pass


class BalanceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Balance",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BalanceProperties, BalanceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Balance"
    return model
    

Balance = create_schema_org_model()


def create_balance_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_balance_model(model=model)
    return pydantic_type(model).schema_json()


