"""
Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.

https://schema.org/MedicalTherapy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalTherapyInheritedProperties(TypedDict):
    """Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.

    References:
        https://schema.org/MedicalTherapy
    Note:
        Model Depth 5
    Attributes:
        doseSchedule: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
        drug: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifying a drug or medicine used in a medication procedure.
        adverseOutcome: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.
    """

    doseSchedule: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    drug: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    adverseOutcome: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class MedicalTherapyProperties(TypedDict):
    """Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.

    References:
        https://schema.org/MedicalTherapy
    Note:
        Model Depth 5
    Attributes:
        seriousAdverseOutcome: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.
        duplicateTherapy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A therapy that duplicates or overlaps this one.
        contraindication: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A contraindication for this therapy.
    """

    seriousAdverseOutcome: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    duplicateTherapy: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    contraindication: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class MedicalTherapyAllProperties(
    MedicalTherapyInheritedProperties, MedicalTherapyProperties, TypedDict
):
    pass


class MedicalTherapyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalTherapy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"doseSchedule": {"exclude": True}}
        fields = {"drug": {"exclude": True}}
        fields = {"adverseOutcome": {"exclude": True}}
        fields = {"seriousAdverseOutcome": {"exclude": True}}
        fields = {"duplicateTherapy": {"exclude": True}}
        fields = {"contraindication": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalTherapyProperties,
        MedicalTherapyInheritedProperties,
        MedicalTherapyAllProperties,
    ] = MedicalTherapyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalTherapy"
    return model


MedicalTherapy = create_schema_org_model()


def create_medicaltherapy_model(
    model: Union[
        MedicalTherapyProperties,
        MedicalTherapyInheritedProperties,
        MedicalTherapyAllProperties,
    ]
):
    _type = deepcopy(MedicalTherapyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalTherapyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalTherapyAllProperties):
    pydantic_type = create_medicaltherapy_model(model=model)
    return pydantic_type(model).schema_json()
