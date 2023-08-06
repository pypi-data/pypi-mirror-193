"""
The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.

https://schema.org/MaximumDoseSchedule
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MaximumDoseScheduleInheritedProperties(TypedDict):
    """The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.

    References:
        https://schema.org/MaximumDoseSchedule
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
    


class MaximumDoseScheduleProperties(TypedDict):
    """The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.

    References:
        https://schema.org/MaximumDoseSchedule
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MaximumDoseScheduleInheritedProperties , MaximumDoseScheduleProperties, TypedDict):
    pass


class MaximumDoseScheduleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MaximumDoseSchedule",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'targetPopulation': {'exclude': True}}
        fields = {'doseValue': {'exclude': True}}
        fields = {'doseUnit': {'exclude': True}}
        fields = {'frequency': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MaximumDoseScheduleProperties, MaximumDoseScheduleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MaximumDoseSchedule"
    return model
    

MaximumDoseSchedule = create_schema_org_model()


def create_maximumdoseschedule_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_maximumdoseschedule_model(model=model)
    return pydantic_type(model).schema_json()


