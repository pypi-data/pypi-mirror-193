"""
A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.

https://schema.org/MedicalIndication
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalIndicationInheritedProperties(TypedDict):
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.

    References:
        https://schema.org/MedicalIndication
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


class MedicalIndicationProperties(TypedDict):
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.

    References:
        https://schema.org/MedicalIndication
    Note:
        Model Depth 3
    Attributes:
    """


class MedicalIndicationAllProperties(
    MedicalIndicationInheritedProperties, MedicalIndicationProperties, TypedDict
):
    pass


class MedicalIndicationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalIndication", alias="@id")
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


def create_schema_org_model(
    type_: Union[
        MedicalIndicationProperties,
        MedicalIndicationInheritedProperties,
        MedicalIndicationAllProperties,
    ] = MedicalIndicationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalIndication"
    return model


MedicalIndication = create_schema_org_model()


def create_medicalindication_model(
    model: Union[
        MedicalIndicationProperties,
        MedicalIndicationInheritedProperties,
        MedicalIndicationAllProperties,
    ]
):
    _type = deepcopy(MedicalIndicationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalIndicationAllProperties):
    pydantic_type = create_medicalindication_model(model=model)
    return pydantic_type(model).schema_json()
