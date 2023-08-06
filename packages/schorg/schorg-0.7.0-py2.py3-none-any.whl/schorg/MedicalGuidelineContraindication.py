"""
A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

https://schema.org/MedicalGuidelineContraindication
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalGuidelineContraindicationInheritedProperties(TypedDict):
    """A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

    References:
        https://schema.org/MedicalGuidelineContraindication
    Note:
        Model Depth 4
    Attributes:
        evidenceLevel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Strength of evidence of the data used to formulate the guideline (enumerated).
        guidelineSubject: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The medical conditions, treatments, etc. that are the subject of the guideline.
        guidelineDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): Date on which this guideline's recommendation was made.
        evidenceOrigin: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.
    """

    evidenceLevel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    guidelineSubject: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    guidelineDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    evidenceOrigin: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MedicalGuidelineContraindicationProperties(TypedDict):
    """A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

    References:
        https://schema.org/MedicalGuidelineContraindication
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MedicalGuidelineContraindicationInheritedProperties , MedicalGuidelineContraindicationProperties, TypedDict):
    pass


class MedicalGuidelineContraindicationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalGuidelineContraindication",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'evidenceLevel': {'exclude': True}}
        fields = {'guidelineSubject': {'exclude': True}}
        fields = {'guidelineDate': {'exclude': True}}
        fields = {'evidenceOrigin': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalGuidelineContraindicationProperties, MedicalGuidelineContraindicationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalGuidelineContraindication"
    return model
    

MedicalGuidelineContraindication = create_schema_org_model()


def create_medicalguidelinecontraindication_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalguidelinecontraindication_model(model=model)
    return pydantic_type(model).schema_json()


