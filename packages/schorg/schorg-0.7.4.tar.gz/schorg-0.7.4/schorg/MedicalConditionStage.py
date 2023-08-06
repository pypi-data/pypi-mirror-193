"""
A stage of a medical condition, such as 'Stage IIIa'.

https://schema.org/MedicalConditionStage
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalConditionStageInheritedProperties(TypedDict):
    """A stage of a medical condition, such as 'Stage IIIa'.

    References:
        https://schema.org/MedicalConditionStage
    Note:
        Model Depth 4
    Attributes:
    """


class MedicalConditionStageProperties(TypedDict):
    """A stage of a medical condition, such as 'Stage IIIa'.

    References:
        https://schema.org/MedicalConditionStage
    Note:
        Model Depth 4
    Attributes:
        subStageSuffix: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The substage, e.g. 'a' for Stage IIIa.
        stageAsNumber: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The stage represented as a number, e.g. 3.
    """

    subStageSuffix: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    stageAsNumber: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class MedicalConditionStageAllProperties(
    MedicalConditionStageInheritedProperties, MedicalConditionStageProperties, TypedDict
):
    pass


class MedicalConditionStageBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalConditionStage", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"subStageSuffix": {"exclude": True}}
        fields = {"stageAsNumber": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalConditionStageProperties,
        MedicalConditionStageInheritedProperties,
        MedicalConditionStageAllProperties,
    ] = MedicalConditionStageAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalConditionStage"
    return model


MedicalConditionStage = create_schema_org_model()


def create_medicalconditionstage_model(
    model: Union[
        MedicalConditionStageProperties,
        MedicalConditionStageInheritedProperties,
        MedicalConditionStageAllProperties,
    ]
):
    _type = deepcopy(MedicalConditionStageAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalConditionStageAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalConditionStageAllProperties):
    pydantic_type = create_medicalconditionstage_model(model=model)
    return pydantic_type(model).schema_json()
