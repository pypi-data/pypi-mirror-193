"""
Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.

https://schema.org/MedicalSignOrSymptom
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalSignOrSymptomInheritedProperties(TypedDict):
    """Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.

    References:
        https://schema.org/MedicalSignOrSymptom
    Note:
        Model Depth 4
    Attributes:
        riskFactor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age,  coexisting condition.
        primaryPrevention: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.
        expectedPrognosis: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The likely outcome in either the short term or long term of the medical condition.
        typicalTest: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical test typically performed given this condition.
        differentialDiagnosis: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.
        pathophysiology: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.
        status: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The status of the study (enumerated).
        naturalProgression: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The expected progression of the condition if it is not treated and allowed to progress naturally.
        drug: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifying a drug or medicine used in a medication procedure.
        secondaryPrevention: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.
        signOrSymptom: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experience of the medical condition.
        possibleTreatment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible treatment to address this condition, sign or symptom.
        epidemiology: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The characteristics of associated patients, such as age, gender, race etc.
        associatedAnatomy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The anatomy of the underlying organ system or structures associated with this entity.
        possibleComplication: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.
        stage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The stage of the condition, if applicable.
    """

    riskFactor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    primaryPrevention: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    expectedPrognosis: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    typicalTest: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    differentialDiagnosis: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    pathophysiology: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    status: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    naturalProgression: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    drug: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    secondaryPrevention: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    signOrSymptom: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    possibleTreatment: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    epidemiology: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    associatedAnatomy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    possibleComplication: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    stage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MedicalSignOrSymptomProperties(TypedDict):
    """Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.

    References:
        https://schema.org/MedicalSignOrSymptom
    Note:
        Model Depth 4
    Attributes:
        possibleTreatment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible treatment to address this condition, sign or symptom.
    """

    possibleTreatment: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalSignOrSymptomAllProperties(
    MedicalSignOrSymptomInheritedProperties, MedicalSignOrSymptomProperties, TypedDict
):
    pass


class MedicalSignOrSymptomBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalSignOrSymptom", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"riskFactor": {"exclude": True}}
        fields = {"primaryPrevention": {"exclude": True}}
        fields = {"expectedPrognosis": {"exclude": True}}
        fields = {"typicalTest": {"exclude": True}}
        fields = {"differentialDiagnosis": {"exclude": True}}
        fields = {"pathophysiology": {"exclude": True}}
        fields = {"status": {"exclude": True}}
        fields = {"naturalProgression": {"exclude": True}}
        fields = {"drug": {"exclude": True}}
        fields = {"secondaryPrevention": {"exclude": True}}
        fields = {"signOrSymptom": {"exclude": True}}
        fields = {"possibleTreatment": {"exclude": True}}
        fields = {"epidemiology": {"exclude": True}}
        fields = {"associatedAnatomy": {"exclude": True}}
        fields = {"possibleComplication": {"exclude": True}}
        fields = {"stage": {"exclude": True}}
        fields = {"possibleTreatment": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalSignOrSymptomProperties,
        MedicalSignOrSymptomInheritedProperties,
        MedicalSignOrSymptomAllProperties,
    ] = MedicalSignOrSymptomAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalSignOrSymptom"
    return model


MedicalSignOrSymptom = create_schema_org_model()


def create_medicalsignorsymptom_model(
    model: Union[
        MedicalSignOrSymptomProperties,
        MedicalSignOrSymptomInheritedProperties,
        MedicalSignOrSymptomAllProperties,
    ]
):
    _type = deepcopy(MedicalSignOrSymptomAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalSignOrSymptomAllProperties):
    pydantic_type = create_medicalsignorsymptom_model(model=model)
    return pydantic_type(model).schema_json()
