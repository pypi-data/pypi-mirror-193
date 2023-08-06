"""
Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.

https://schema.org/MedicalSign
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalSignInheritedProperties(TypedDict):
    """Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.

    References:
        https://schema.org/MedicalSign
    Note:
        Model Depth 5
    Attributes:
        possibleTreatment: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible treatment to address this condition, sign or symptom.
    """

    possibleTreatment: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MedicalSignProperties(TypedDict):
    """Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.

    References:
        https://schema.org/MedicalSign
    Note:
        Model Depth 5
    Attributes:
        identifyingExam: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A physical examination that can identify this sign.
        identifyingTest: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A diagnostic test that can identify this sign.
    """

    identifyingExam: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    identifyingTest: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(MedicalSignInheritedProperties , MedicalSignProperties, TypedDict):
    pass


class MedicalSignBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalSign",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'possibleTreatment': {'exclude': True}}
        fields = {'identifyingExam': {'exclude': True}}
        fields = {'identifyingTest': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalSignProperties, MedicalSignInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalSign"
    return model
    

MedicalSign = create_schema_org_model()


def create_medicalsign_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalsign_model(model=model)
    return pydantic_type(model).schema_json()


