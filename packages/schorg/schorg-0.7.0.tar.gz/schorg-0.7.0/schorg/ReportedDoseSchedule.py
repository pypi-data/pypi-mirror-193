"""
A patient-reported or observed dosing schedule for a drug or supplement.

https://schema.org/ReportedDoseSchedule
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReportedDoseScheduleInheritedProperties(TypedDict):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    References:
        https://schema.org/ReportedDoseSchedule
    Note:
        Model Depth 5
    Attributes:
        targetPopulation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.
        doseValue: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The value of the dose, e.g. 500.
        doseUnit: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The unit of the dose, e.g. 'mg'.
        frequency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): How often the dose is taken, e.g. 'daily'.
    """

    targetPopulation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    doseValue: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    doseUnit: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    frequency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class ReportedDoseScheduleProperties(TypedDict):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    References:
        https://schema.org/ReportedDoseSchedule
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReportedDoseScheduleInheritedProperties , ReportedDoseScheduleProperties, TypedDict):
    pass


class ReportedDoseScheduleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReportedDoseSchedule",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'targetPopulation': {'exclude': True}}
        fields = {'doseValue': {'exclude': True}}
        fields = {'doseUnit': {'exclude': True}}
        fields = {'frequency': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ReportedDoseScheduleProperties, ReportedDoseScheduleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReportedDoseSchedule"
    return model
    

ReportedDoseSchedule = create_schema_org_model()


def create_reporteddoseschedule_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reporteddoseschedule_model(model=model)
    return pydantic_type(model).schema_json()


