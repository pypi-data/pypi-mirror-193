"""
Level of evidence for a medical guideline. Enumerated type.

https://schema.org/MedicalEvidenceLevel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalEvidenceLevelInheritedProperties(TypedDict):
    """Level of evidence for a medical guideline. Enumerated type.

    References:
        https://schema.org/MedicalEvidenceLevel
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalEvidenceLevelProperties(TypedDict):
    """Level of evidence for a medical guideline. Enumerated type.

    References:
        https://schema.org/MedicalEvidenceLevel
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalEvidenceLevelAllProperties(
    MedicalEvidenceLevelInheritedProperties, MedicalEvidenceLevelProperties, TypedDict
):
    pass


class MedicalEvidenceLevelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalEvidenceLevel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicalEvidenceLevelProperties,
        MedicalEvidenceLevelInheritedProperties,
        MedicalEvidenceLevelAllProperties,
    ] = MedicalEvidenceLevelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalEvidenceLevel"
    return model


MedicalEvidenceLevel = create_schema_org_model()


def create_medicalevidencelevel_model(
    model: Union[
        MedicalEvidenceLevelProperties,
        MedicalEvidenceLevelInheritedProperties,
        MedicalEvidenceLevelAllProperties,
    ]
):
    _type = deepcopy(MedicalEvidenceLevelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalEvidenceLevelAllProperties):
    pydantic_type = create_medicalevidencelevel_model(model=model)
    return pydantic_type(model).schema_json()
