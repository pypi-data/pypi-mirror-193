"""
Medical researchers.

https://schema.org/MedicalResearcher
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalResearcherInheritedProperties(TypedDict):
    """Medical researchers.

    References:
        https://schema.org/MedicalResearcher
    Note:
        Model Depth 6
    Attributes:
    """


class MedicalResearcherProperties(TypedDict):
    """Medical researchers.

    References:
        https://schema.org/MedicalResearcher
    Note:
        Model Depth 6
    Attributes:
    """


class MedicalResearcherAllProperties(
    MedicalResearcherInheritedProperties, MedicalResearcherProperties, TypedDict
):
    pass


class MedicalResearcherBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalResearcher", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicalResearcherProperties,
        MedicalResearcherInheritedProperties,
        MedicalResearcherAllProperties,
    ] = MedicalResearcherAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalResearcher"
    return model


MedicalResearcher = create_schema_org_model()


def create_medicalresearcher_model(
    model: Union[
        MedicalResearcherProperties,
        MedicalResearcherInheritedProperties,
        MedicalResearcherAllProperties,
    ]
):
    _type = deepcopy(MedicalResearcherAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MedicalResearcher. Please see: https://schema.org/MedicalResearcher"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MedicalResearcherAllProperties):
    pydantic_type = create_medicalresearcher_model(model=model)
    return pydantic_type(model).schema_json()
