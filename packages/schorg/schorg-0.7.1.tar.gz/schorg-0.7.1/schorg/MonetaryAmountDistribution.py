"""
A statistical distribution of monetary amounts.

https://schema.org/MonetaryAmountDistribution
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MonetaryAmountDistributionInheritedProperties(TypedDict):
    """A statistical distribution of monetary amounts.

    References:
        https://schema.org/MonetaryAmountDistribution
    Note:
        Model Depth 5
    Attributes:
        percentile75: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 75th percentile value.
        percentile25: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 25th percentile value.
        duration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        median: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The median value.
        percentile90: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 90th percentile value.
        percentile10: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 10th percentile value.
    """

    percentile75: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    percentile25: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    duration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    median: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    percentile90: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    percentile10: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    


class MonetaryAmountDistributionProperties(TypedDict):
    """A statistical distribution of monetary amounts.

    References:
        https://schema.org/MonetaryAmountDistribution
    Note:
        Model Depth 5
    Attributes:
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MonetaryAmountDistributionInheritedProperties , MonetaryAmountDistributionProperties, TypedDict):
    pass


class MonetaryAmountDistributionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MonetaryAmountDistribution",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'percentile75': {'exclude': True}}
        fields = {'percentile25': {'exclude': True}}
        fields = {'duration': {'exclude': True}}
        fields = {'median': {'exclude': True}}
        fields = {'percentile90': {'exclude': True}}
        fields = {'percentile10': {'exclude': True}}
        fields = {'currency': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MonetaryAmountDistributionProperties, MonetaryAmountDistributionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MonetaryAmountDistribution"
    return model
    

MonetaryAmountDistribution = create_schema_org_model()


def create_monetaryamountdistribution_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_monetaryamountdistribution_model(model=model)
    return pydantic_type(model).schema_json()


