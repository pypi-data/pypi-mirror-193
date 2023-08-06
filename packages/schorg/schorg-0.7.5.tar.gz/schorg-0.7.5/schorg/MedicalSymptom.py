"""
Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.

https://schema.org/MedicalSymptom
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalSymptomInheritedProperties(TypedDict):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.

    References:
        https://schema.org/MedicalSymptom
    Note:
        Model Depth 5
    Attributes:
        possibleTreatment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible treatment to address this condition, sign or symptom.
    """

    possibleTreatment: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalSymptomProperties(TypedDict):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.

    References:
        https://schema.org/MedicalSymptom
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalSymptomAllProperties(
    MedicalSymptomInheritedProperties, MedicalSymptomProperties, TypedDict
):
    pass


class MedicalSymptomBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalSymptom", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"possibleTreatment": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalSymptomProperties,
        MedicalSymptomInheritedProperties,
        MedicalSymptomAllProperties,
    ] = MedicalSymptomAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalSymptom"
    return model


MedicalSymptom = create_schema_org_model()


def create_medicalsymptom_model(
    model: Union[
        MedicalSymptomProperties,
        MedicalSymptomInheritedProperties,
        MedicalSymptomAllProperties,
    ]
):
    _type = deepcopy(MedicalSymptomAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MedicalSymptom. Please see: https://schema.org/MedicalSymptom"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MedicalSymptomAllProperties):
    pydantic_type = create_medicalsymptom_model(model=model)
    return pydantic_type(model).schema_json()
