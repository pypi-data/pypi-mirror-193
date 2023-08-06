"""
A statistical distribution of values.

https://schema.org/QuantitativeValueDistribution
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        percentile75: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 75th percentile value.
        percentile25: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 25th percentile value.
        duration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        median: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The median value.
        percentile90: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 90th percentile value.
        percentile10: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The 10th percentile value.
    """

    percentile75: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    percentile25: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    duration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    median: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    percentile90: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    percentile10: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]


class QuantitativeValueDistributionAllProperties(
    QuantitativeValueDistributionInheritedProperties,
    QuantitativeValueDistributionProperties,
    TypedDict,
):
    pass


class QuantitativeValueDistributionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="QuantitativeValueDistribution", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"percentile75": {"exclude": True}}
        fields = {"percentile25": {"exclude": True}}
        fields = {"duration": {"exclude": True}}
        fields = {"median": {"exclude": True}}
        fields = {"percentile90": {"exclude": True}}
        fields = {"percentile10": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        QuantitativeValueDistributionProperties,
        QuantitativeValueDistributionInheritedProperties,
        QuantitativeValueDistributionAllProperties,
    ] = QuantitativeValueDistributionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "QuantitativeValueDistribution"
    return model


QuantitativeValueDistribution = create_schema_org_model()


def create_quantitativevaluedistribution_model(
    model: Union[
        QuantitativeValueDistributionProperties,
        QuantitativeValueDistributionInheritedProperties,
        QuantitativeValueDistributionAllProperties,
    ]
):
    _type = deepcopy(QuantitativeValueDistributionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: QuantitativeValueDistributionAllProperties):
    pydantic_type = create_quantitativevaluedistribution_model(model=model)
    return pydantic_type(model).schema_json()
