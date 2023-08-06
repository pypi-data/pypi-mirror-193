"""
A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.

https://schema.org/MedicalGuidelineRecommendation
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalGuidelineRecommendationInheritedProperties(TypedDict):
    """A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.

    References:
        https://schema.org/MedicalGuidelineRecommendation
    Note:
        Model Depth 4
    Attributes:
        evidenceLevel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Strength of evidence of the data used to formulate the guideline (enumerated).
        guidelineSubject: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The medical conditions, treatments, etc. that are the subject of the guideline.
        guidelineDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): Date on which this guideline's recommendation was made.
        evidenceOrigin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.
    """

    evidenceLevel: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    guidelineSubject: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    guidelineDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    evidenceOrigin: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalGuidelineRecommendationProperties(TypedDict):
    """A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.

    References:
        https://schema.org/MedicalGuidelineRecommendation
    Note:
        Model Depth 4
    Attributes:
        recommendationStrength: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Strength of the guideline's recommendation (e.g. 'class I').
    """

    recommendationStrength: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalGuidelineRecommendationAllProperties(
    MedicalGuidelineRecommendationInheritedProperties,
    MedicalGuidelineRecommendationProperties,
    TypedDict,
):
    pass


class MedicalGuidelineRecommendationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalGuidelineRecommendation", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"evidenceLevel": {"exclude": True}}
        fields = {"guidelineSubject": {"exclude": True}}
        fields = {"guidelineDate": {"exclude": True}}
        fields = {"evidenceOrigin": {"exclude": True}}
        fields = {"recommendationStrength": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalGuidelineRecommendationProperties,
        MedicalGuidelineRecommendationInheritedProperties,
        MedicalGuidelineRecommendationAllProperties,
    ] = MedicalGuidelineRecommendationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalGuidelineRecommendation"
    return model


MedicalGuidelineRecommendation = create_schema_org_model()


def create_medicalguidelinerecommendation_model(
    model: Union[
        MedicalGuidelineRecommendationProperties,
        MedicalGuidelineRecommendationInheritedProperties,
        MedicalGuidelineRecommendationAllProperties,
    ]
):
    _type = deepcopy(MedicalGuidelineRecommendationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalGuidelineRecommendationAllProperties):
    pydantic_type = create_medicalguidelinerecommendation_model(model=model)
    return pydantic_type(model).schema_json()
