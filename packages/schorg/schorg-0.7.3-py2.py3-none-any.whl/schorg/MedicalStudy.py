"""
A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.

https://schema.org/MedicalStudy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalStudyInheritedProperties(TypedDict):
    """A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.

    References:
        https://schema.org/MedicalStudy
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


class MedicalStudyProperties(TypedDict):
    """A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.

    References:
        https://schema.org/MedicalStudy
    Note:
        Model Depth 3
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


class MedicalStudyAllProperties(
    MedicalStudyInheritedProperties, MedicalStudyProperties, TypedDict
):
    pass


class MedicalStudyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalStudy", alias="@id")
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
        fields = {"studySubject": {"exclude": True}}
        fields = {"studyLocation": {"exclude": True}}
        fields = {"healthCondition": {"exclude": True}}
        fields = {"status": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalStudyProperties,
        MedicalStudyInheritedProperties,
        MedicalStudyAllProperties,
    ] = MedicalStudyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalStudy"
    return model


MedicalStudy = create_schema_org_model()


def create_medicalstudy_model(
    model: Union[
        MedicalStudyProperties,
        MedicalStudyInheritedProperties,
        MedicalStudyAllProperties,
    ]
):
    _type = deepcopy(MedicalStudyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalStudyAllProperties):
    pydantic_type = create_medicalstudy_model(model=model)
    return pydantic_type(model).schema_json()
