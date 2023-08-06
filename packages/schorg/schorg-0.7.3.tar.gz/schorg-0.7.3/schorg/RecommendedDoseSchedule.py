"""
A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.

https://schema.org/RecommendedDoseSchedule
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RecommendedDoseScheduleInheritedProperties(TypedDict):
    """A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.

    References:
        https://schema.org/RecommendedDoseSchedule
    Note:
        Model Depth 5
    Attributes:
        targetPopulation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.
        doseValue: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The value of the dose, e.g. 500.
        doseUnit: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The unit of the dose, e.g. 'mg'.
        frequency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): How often the dose is taken, e.g. 'daily'.
    """

    targetPopulation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    doseValue: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    doseUnit: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    frequency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class RecommendedDoseScheduleProperties(TypedDict):
    """A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.

    References:
        https://schema.org/RecommendedDoseSchedule
    Note:
        Model Depth 5
    Attributes:
    """


class RecommendedDoseScheduleAllProperties(
    RecommendedDoseScheduleInheritedProperties,
    RecommendedDoseScheduleProperties,
    TypedDict,
):
    pass


class RecommendedDoseScheduleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RecommendedDoseSchedule", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"targetPopulation": {"exclude": True}}
        fields = {"doseValue": {"exclude": True}}
        fields = {"doseUnit": {"exclude": True}}
        fields = {"frequency": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RecommendedDoseScheduleProperties,
        RecommendedDoseScheduleInheritedProperties,
        RecommendedDoseScheduleAllProperties,
    ] = RecommendedDoseScheduleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RecommendedDoseSchedule"
    return model


RecommendedDoseSchedule = create_schema_org_model()


def create_recommendeddoseschedule_model(
    model: Union[
        RecommendedDoseScheduleProperties,
        RecommendedDoseScheduleInheritedProperties,
        RecommendedDoseScheduleAllProperties,
    ]
):
    _type = deepcopy(RecommendedDoseScheduleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RecommendedDoseScheduleAllProperties):
    pydantic_type = create_recommendeddoseschedule_model(model=model)
    return pydantic_type(model).schema_json()
