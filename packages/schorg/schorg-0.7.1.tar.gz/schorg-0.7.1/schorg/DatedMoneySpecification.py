"""
A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended.

https://schema.org/DatedMoneySpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DatedMoneySpecificationInheritedProperties(TypedDict):
    """A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended.

    References:
        https://schema.org/DatedMoneySpecification
    Note:
        Model Depth 4
    Attributes:
    """

    


class DatedMoneySpecificationProperties(TypedDict):
    """A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended.

    References:
        https://schema.org/DatedMoneySpecification
    Note:
        Model Depth 4
    Attributes:
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        amount: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The amount of money.
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    amount: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    startDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    endDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    


class AllProperties(DatedMoneySpecificationInheritedProperties , DatedMoneySpecificationProperties, TypedDict):
    pass


class DatedMoneySpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DatedMoneySpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'currency': {'exclude': True}}
        fields = {'amount': {'exclude': True}}
        fields = {'startDate': {'exclude': True}}
        fields = {'endDate': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DatedMoneySpecificationProperties, DatedMoneySpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DatedMoneySpecification"
    return model
    

DatedMoneySpecification = create_schema_org_model()


def create_datedmoneyspecification_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_datedmoneyspecification_model(model=model)
    return pydantic_type(model).schema_json()


