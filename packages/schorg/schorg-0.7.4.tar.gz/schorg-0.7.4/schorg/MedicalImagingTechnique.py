"""
Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

https://schema.org/MedicalImagingTechnique
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalImagingTechniqueInheritedProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    References:
        https://schema.org/MedicalImagingTechnique
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalImagingTechniqueProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    References:
        https://schema.org/MedicalImagingTechnique
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalImagingTechniqueAllProperties(
    MedicalImagingTechniqueInheritedProperties,
    MedicalImagingTechniqueProperties,
    TypedDict,
):
    pass


class MedicalImagingTechniqueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalImagingTechnique", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicalImagingTechniqueProperties,
        MedicalImagingTechniqueInheritedProperties,
        MedicalImagingTechniqueAllProperties,
    ] = MedicalImagingTechniqueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalImagingTechnique"
    return model


MedicalImagingTechnique = create_schema_org_model()


def create_medicalimagingtechnique_model(
    model: Union[
        MedicalImagingTechniqueProperties,
        MedicalImagingTechniqueInheritedProperties,
        MedicalImagingTechniqueAllProperties,
    ]
):
    _type = deepcopy(MedicalImagingTechniqueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalImagingTechniqueAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalImagingTechniqueAllProperties):
    pydantic_type = create_medicalimagingtechnique_model(model=model)
    return pydantic_type(model).schema_json()
