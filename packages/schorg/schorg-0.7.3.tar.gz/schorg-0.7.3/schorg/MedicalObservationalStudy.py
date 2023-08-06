"""
An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.

https://schema.org/MedicalObservationalStudy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalObservationalStudyInheritedProperties(TypedDict):
    """An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.

    References:
        https://schema.org/MedicalObservationalStudy
    Note:
        Model Depth 4
    Attributes:
        studySubject: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.
        studyLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location in which the study is taking/took place.
        healthCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifying the health condition(s) of a patient, medical study, or other target audience.
        status: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The status of the study (enumerated).
        sponsor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
    """

    studySubject: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    studyLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    healthCondition: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    status: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sponsor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MedicalObservationalStudyProperties(TypedDict):
    """An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.

    References:
        https://schema.org/MedicalObservationalStudy
    Note:
        Model Depth 4
    Attributes:
        studyDesign: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifics about the observational study design (enumerated).
    """

    studyDesign: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MedicalObservationalStudyAllProperties(
    MedicalObservationalStudyInheritedProperties,
    MedicalObservationalStudyProperties,
    TypedDict,
):
    pass


class MedicalObservationalStudyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalObservationalStudy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"studySubject": {"exclude": True}}
        fields = {"studyLocation": {"exclude": True}}
        fields = {"healthCondition": {"exclude": True}}
        fields = {"status": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}
        fields = {"studyDesign": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalObservationalStudyProperties,
        MedicalObservationalStudyInheritedProperties,
        MedicalObservationalStudyAllProperties,
    ] = MedicalObservationalStudyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalObservationalStudy"
    return model


MedicalObservationalStudy = create_schema_org_model()


def create_medicalobservationalstudy_model(
    model: Union[
        MedicalObservationalStudyProperties,
        MedicalObservationalStudyInheritedProperties,
        MedicalObservationalStudyAllProperties,
    ]
):
    _type = deepcopy(MedicalObservationalStudyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalObservationalStudyAllProperties):
    pydantic_type = create_medicalobservationalstudy_model(model=model)
    return pydantic_type(model).schema_json()
