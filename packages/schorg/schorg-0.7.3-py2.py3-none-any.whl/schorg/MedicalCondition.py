"""
Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.

https://schema.org/MedicalCondition
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalConditionInheritedProperties(TypedDict):
    """Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.

    References:
        https://schema.org/MedicalCondition
    Note:
        Model Depth 3
    Attributes:
        recognizingAuthority: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.
        relevantSpecialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If applicable, a medical specialty in which this entity is relevant.
        medicineSystem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        legalStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The drug or supplement's legal status, including any controlled substance schedules that apply.
        study: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical study or trial related to this entity.
        guideline: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical guideline related to this entity.
        code: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.
    """

    recognizingAuthority: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    relevantSpecialty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    medicineSystem: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    legalStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    study: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    guideline: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    code: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MedicalConditionProperties(TypedDict):
    """Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.

    References:
        https://schema.org/MedicalCondition
    Note:
        Model Depth 3
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


class MedicalConditionAllProperties(
    MedicalConditionInheritedProperties, MedicalConditionProperties, TypedDict
):
    pass


class MedicalConditionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalCondition", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"recognizingAuthority": {"exclude": True}}
        fields = {"relevantSpecialty": {"exclude": True}}
        fields = {"medicineSystem": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"legalStatus": {"exclude": True}}
        fields = {"study": {"exclude": True}}
        fields = {"guideline": {"exclude": True}}
        fields = {"code": {"exclude": True}}
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


def create_schema_org_model(
    type_: Union[
        MedicalConditionProperties,
        MedicalConditionInheritedProperties,
        MedicalConditionAllProperties,
    ] = MedicalConditionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalCondition"
    return model


MedicalCondition = create_schema_org_model()


def create_medicalcondition_model(
    model: Union[
        MedicalConditionProperties,
        MedicalConditionInheritedProperties,
        MedicalConditionAllProperties,
    ]
):
    _type = deepcopy(MedicalConditionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalConditionAllProperties):
    pydantic_type = create_medicalcondition_model(model=model)
    return pydantic_type(model).schema_json()
