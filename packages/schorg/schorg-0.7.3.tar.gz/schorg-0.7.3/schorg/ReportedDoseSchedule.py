"""
A patient-reported or observed dosing schedule for a drug or supplement.

https://schema.org/ReportedDoseSchedule
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReportedDoseScheduleInheritedProperties(TypedDict):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    References:
        https://schema.org/ReportedDoseSchedule
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


class ReportedDoseScheduleProperties(TypedDict):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    References:
        https://schema.org/ReportedDoseSchedule
    Note:
        Model Depth 5
    Attributes:
    """


class ReportedDoseScheduleAllProperties(
    ReportedDoseScheduleInheritedProperties, ReportedDoseScheduleProperties, TypedDict
):
    pass


class ReportedDoseScheduleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReportedDoseSchedule", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"targetPopulation": {"exclude": True}}
        fields = {"doseValue": {"exclude": True}}
        fields = {"doseUnit": {"exclude": True}}
        fields = {"frequency": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReportedDoseScheduleProperties,
        ReportedDoseScheduleInheritedProperties,
        ReportedDoseScheduleAllProperties,
    ] = ReportedDoseScheduleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReportedDoseSchedule"
    return model


ReportedDoseSchedule = create_schema_org_model()


def create_reporteddoseschedule_model(
    model: Union[
        ReportedDoseScheduleProperties,
        ReportedDoseScheduleInheritedProperties,
        ReportedDoseScheduleAllProperties,
    ]
):
    _type = deepcopy(ReportedDoseScheduleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReportedDoseScheduleAllProperties):
    pydantic_type = create_reporteddoseschedule_model(model=model)
    return pydantic_type(model).schema_json()
