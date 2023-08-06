"""
An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.

https://schema.org/InfectiousDisease
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InfectiousDiseaseInheritedProperties(TypedDict):
    """An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.

    References:
        https://schema.org/InfectiousDisease
    Note:
        Model Depth 4
    Attributes:
        riskFactor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age,  coexisting condition.
        primaryPrevention: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.
        expectedPrognosis: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The likely outcome in either the short term or long term of the medical condition.
        typicalTest: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical test typically performed given this condition.
        differentialDiagnosis: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.
        pathophysiology: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.
        status: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The status of the study (enumerated).
        naturalProgression: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The expected progression of the condition if it is not treated and allowed to progress naturally.
        drug: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifying a drug or medicine used in a medication procedure.
        secondaryPrevention: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.
        signOrSymptom: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experience of the medical condition.
        possibleTreatment: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible treatment to address this condition, sign or symptom.
        epidemiology: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The characteristics of associated patients, such as age, gender, race etc.
        associatedAnatomy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The anatomy of the underlying organ system or structures associated with this entity.
        possibleComplication: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.
        stage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The stage of the condition, if applicable.
    """

    riskFactor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    primaryPrevention: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    expectedPrognosis: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    typicalTest: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    differentialDiagnosis: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    pathophysiology: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    status: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    naturalProgression: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    drug: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    secondaryPrevention: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    signOrSymptom: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    possibleTreatment: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    epidemiology: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    associatedAnatomy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    possibleComplication: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    stage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class InfectiousDiseaseProperties(TypedDict):
    """An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.

    References:
        https://schema.org/InfectiousDisease
    Note:
        Model Depth 4
    Attributes:
        infectiousAgent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The actual infectious agent, such as a specific bacterium.
        infectiousAgentClass: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The class of infectious agent (bacteria, prion, etc.) that causes the disease.
        transmissionMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes aegypti', etc.
    """

    infectiousAgent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    infectiousAgentClass: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    transmissionMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(InfectiousDiseaseInheritedProperties , InfectiousDiseaseProperties, TypedDict):
    pass


class InfectiousDiseaseBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InfectiousDisease",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'riskFactor': {'exclude': True}}
        fields = {'primaryPrevention': {'exclude': True}}
        fields = {'expectedPrognosis': {'exclude': True}}
        fields = {'typicalTest': {'exclude': True}}
        fields = {'differentialDiagnosis': {'exclude': True}}
        fields = {'pathophysiology': {'exclude': True}}
        fields = {'status': {'exclude': True}}
        fields = {'naturalProgression': {'exclude': True}}
        fields = {'drug': {'exclude': True}}
        fields = {'secondaryPrevention': {'exclude': True}}
        fields = {'signOrSymptom': {'exclude': True}}
        fields = {'possibleTreatment': {'exclude': True}}
        fields = {'epidemiology': {'exclude': True}}
        fields = {'associatedAnatomy': {'exclude': True}}
        fields = {'possibleComplication': {'exclude': True}}
        fields = {'stage': {'exclude': True}}
        fields = {'infectiousAgent': {'exclude': True}}
        fields = {'infectiousAgentClass': {'exclude': True}}
        fields = {'transmissionMethod': {'exclude': True}}
        


def create_schema_org_model(type_: Union[InfectiousDiseaseProperties, InfectiousDiseaseInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InfectiousDisease"
    return model
    

InfectiousDisease = create_schema_org_model()


def create_infectiousdisease_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_infectiousdisease_model(model=model)
    return pydantic_type(model).schema_json()


