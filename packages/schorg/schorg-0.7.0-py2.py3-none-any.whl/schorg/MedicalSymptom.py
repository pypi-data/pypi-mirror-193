"""
Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.

https://schema.org/MedicalSymptom
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalSymptomInheritedProperties(TypedDict):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.

    References:
        https://schema.org/MedicalSymptom
    Note:
        Model Depth 5
    Attributes:
        possibleTreatment: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible treatment to address this condition, sign or symptom.
    """

    possibleTreatment: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MedicalSymptomProperties(TypedDict):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.

    References:
        https://schema.org/MedicalSymptom
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalSymptomInheritedProperties , MedicalSymptomProperties, TypedDict):
    pass


class MedicalSymptomBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalSymptom",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'possibleTreatment': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalSymptomProperties, MedicalSymptomInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalSymptom"
    return model
    

MedicalSymptom = create_schema_org_model()


def create_medicalsymptom_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalsymptom_model(model=model)
    return pydantic_type(model).schema_json()


