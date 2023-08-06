"""
A statistical distribution of values.

https://schema.org/QuantitativeValueDistribution
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class QuantitativeValueDistributionInheritedProperties(TypedDict):
    """A statistical distribution of values.

    References:
        https://schema.org/QuantitativeValueDistribution
    Note:
        Model Depth 4
    Attributes:
    """

    


class QuantitativeValueDistributionProperties(TypedDict):
    """A statistical distribution of values.

    References:
        https://schema.org/QuantitativeValueDistribution
    Note:
        Model Depth 4
    Attributes:
        percentile75: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The 75th percentile value.
        percentile25: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The 25th percentile value.
        duration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        median: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The median value.
        percentile90: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The 90th percentile value.
        percentile10: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The 10th percentile value.
    """

    percentile75: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    percentile25: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    duration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    median: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    percentile90: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    percentile10: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class AllProperties(QuantitativeValueDistributionInheritedProperties , QuantitativeValueDistributionProperties, TypedDict):
    pass


class QuantitativeValueDistributionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="QuantitativeValueDistribution",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'percentile75': {'exclude': True}}
        fields = {'percentile25': {'exclude': True}}
        fields = {'duration': {'exclude': True}}
        fields = {'median': {'exclude': True}}
        fields = {'percentile90': {'exclude': True}}
        fields = {'percentile10': {'exclude': True}}
        


def create_schema_org_model(type_: Union[QuantitativeValueDistributionProperties, QuantitativeValueDistributionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "QuantitativeValueDistribution"
    return model
    

QuantitativeValueDistribution = create_schema_org_model()


def create_quantitativevaluedistribution_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_quantitativevaluedistribution_model(model=model)
    return pydantic_type(model).schema_json()


