"""
A service to convert funds from one currency to another currency.

https://schema.org/CurrencyConversionService
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CurrencyConversionServiceInheritedProperties(TypedDict):
    """A service to convert funds from one currency to another currency.

    References:
        https://schema.org/CurrencyConversionService
    Note:
        Model Depth 5
    Attributes:
        annualPercentageRate: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.
        interestRate: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.
        feesAndCommissionsSpecification: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    annualPercentageRate: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    interestRate: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    feesAndCommissionsSpecification: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class CurrencyConversionServiceProperties(TypedDict):
    """A service to convert funds from one currency to another currency.

    References:
        https://schema.org/CurrencyConversionService
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CurrencyConversionServiceInheritedProperties , CurrencyConversionServiceProperties, TypedDict):
    pass


class CurrencyConversionServiceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CurrencyConversionService",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'annualPercentageRate': {'exclude': True}}
        fields = {'interestRate': {'exclude': True}}
        fields = {'feesAndCommissionsSpecification': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CurrencyConversionServiceProperties, CurrencyConversionServiceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CurrencyConversionService"
    return model
    

CurrencyConversionService = create_schema_org_model()


def create_currencyconversionservice_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_currencyconversionservice_model(model=model)
    return pydantic_type(model).schema_json()


