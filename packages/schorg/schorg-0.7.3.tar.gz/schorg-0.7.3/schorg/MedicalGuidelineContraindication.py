"""
A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

https://schema.org/MedicalGuidelineContraindication
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalGuidelineContraindicationInheritedProperties(TypedDict):
    """A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

    References:
        https://schema.org/MedicalGuidelineContraindication
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


class MedicalGuidelineContraindicationProperties(TypedDict):
    """A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

    References:
        https://schema.org/MedicalGuidelineContraindication
    Note:
        Model Depth 4
    Attributes:
    """


class MedicalGuidelineContraindicationAllProperties(
    MedicalGuidelineContraindicationInheritedProperties,
    MedicalGuidelineContraindicationProperties,
    TypedDict,
):
    pass


class MedicalGuidelineContraindicationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalGuidelineContraindication", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"evidenceLevel": {"exclude": True}}
        fields = {"guidelineSubject": {"exclude": True}}
        fields = {"guidelineDate": {"exclude": True}}
        fields = {"evidenceOrigin": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalGuidelineContraindicationProperties,
        MedicalGuidelineContraindicationInheritedProperties,
        MedicalGuidelineContraindicationAllProperties,
    ] = MedicalGuidelineContraindicationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalGuidelineContraindication"
    return model


MedicalGuidelineContraindication = create_schema_org_model()


def create_medicalguidelinecontraindication_model(
    model: Union[
        MedicalGuidelineContraindicationProperties,
        MedicalGuidelineContraindicationInheritedProperties,
        MedicalGuidelineContraindicationAllProperties,
    ]
):
    _type = deepcopy(MedicalGuidelineContraindicationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalGuidelineContraindicationAllProperties):
    pydantic_type = create_medicalguidelinecontraindication_model(model=model)
    return pydantic_type(model).schema_json()
