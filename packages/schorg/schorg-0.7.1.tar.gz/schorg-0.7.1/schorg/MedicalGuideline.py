"""
Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.

https://schema.org/MedicalGuideline
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalGuidelineInheritedProperties(TypedDict):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.

    References:
        https://schema.org/MedicalGuideline
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

    recognizingAuthority: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relevantSpecialty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    medicineSystem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    legalStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    study: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    guideline: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    code: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class MedicalGuidelineProperties(TypedDict):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.

    References:
        https://schema.org/MedicalGuideline
    Note:
        Model Depth 3
    Attributes:
        evidenceLevel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Strength of evidence of the data used to formulate the guideline (enumerated).
        guidelineSubject: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The medical conditions, treatments, etc. that are the subject of the guideline.
        guidelineDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): Date on which this guideline's recommendation was made.
        evidenceOrigin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.
    """

    evidenceLevel: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    guidelineSubject: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    guidelineDate: NotRequired[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]
    evidenceOrigin: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MedicalGuidelineInheritedProperties , MedicalGuidelineProperties, TypedDict):
    pass


class MedicalGuidelineBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalGuideline",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'recognizingAuthority': {'exclude': True}}
        fields = {'relevantSpecialty': {'exclude': True}}
        fields = {'medicineSystem': {'exclude': True}}
        fields = {'funding': {'exclude': True}}
        fields = {'legalStatus': {'exclude': True}}
        fields = {'study': {'exclude': True}}
        fields = {'guideline': {'exclude': True}}
        fields = {'code': {'exclude': True}}
        fields = {'evidenceLevel': {'exclude': True}}
        fields = {'guidelineSubject': {'exclude': True}}
        fields = {'guidelineDate': {'exclude': True}}
        fields = {'evidenceOrigin': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalGuidelineProperties, MedicalGuidelineInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalGuideline"
    return model
    

MedicalGuideline = create_schema_org_model()


def create_medicalguideline_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalguideline_model(model=model)
    return pydantic_type(model).schema_json()


