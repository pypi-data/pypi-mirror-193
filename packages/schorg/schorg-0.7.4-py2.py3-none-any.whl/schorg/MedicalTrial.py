"""
A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.

https://schema.org/MedicalTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalTrialInheritedProperties(TypedDict):
    """A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.

    References:
        https://schema.org/MedicalTrial
    Note:
        Model Depth 4
    Attributes:
        studySubject: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.
        studyLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location in which the study is taking/took place.
        healthCondition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifying the health condition(s) of a patient, medical study, or other target audience.
        status: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The status of the study (enumerated).
        sponsor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
    """

    studySubject: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    studyLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    healthCondition: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    status: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sponsor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class MedicalTrialProperties(TypedDict):
    """A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.

    References:
        https://schema.org/MedicalTrial
    Note:
        Model Depth 4
    Attributes:
        trialDesign: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifics about the trial design (enumerated).
    """

    trialDesign: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class MedicalTrialAllProperties(
    MedicalTrialInheritedProperties, MedicalTrialProperties, TypedDict
):
    pass


class MedicalTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"studySubject": {"exclude": True}}
        fields = {"studyLocation": {"exclude": True}}
        fields = {"healthCondition": {"exclude": True}}
        fields = {"status": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}
        fields = {"trialDesign": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalTrialProperties,
        MedicalTrialInheritedProperties,
        MedicalTrialAllProperties,
    ] = MedicalTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalTrial"
    return model


MedicalTrial = create_schema_org_model()


def create_medicaltrial_model(
    model: Union[
        MedicalTrialProperties,
        MedicalTrialInheritedProperties,
        MedicalTrialAllProperties,
    ]
):
    _type = deepcopy(MedicalTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalTrialAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalTrialAllProperties):
    pydantic_type = create_medicaltrial_model(model=model)
    return pydantic_type(model).schema_json()
