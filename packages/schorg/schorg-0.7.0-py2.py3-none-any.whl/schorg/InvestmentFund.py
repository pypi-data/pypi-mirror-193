"""
A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.

https://schema.org/InvestmentFund
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InvestmentFundInheritedProperties(TypedDict):
    """A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.

    References:
        https://schema.org/InvestmentFund
    Note:
        Model Depth 6
    Attributes:
        amount: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The amount of money.
    """

    amount: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class InvestmentFundProperties(TypedDict):
    """A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.

    References:
        https://schema.org/InvestmentFund
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(InvestmentFundInheritedProperties , InvestmentFundProperties, TypedDict):
    pass


class InvestmentFundBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InvestmentFund",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'amount': {'exclude': True}}
        


def create_schema_org_model(type_: Union[InvestmentFundProperties, InvestmentFundInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InvestmentFund"
    return model
    

InvestmentFund = create_schema_org_model()


def create_investmentfund_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_investmentfund_model(model=model)
    return pydantic_type(model).schema_json()


