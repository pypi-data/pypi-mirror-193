"""
A medical science pertaining to chemical, hematological, immunologic, microscopic, or bacteriological diagnostic analyses or research.

https://schema.org/LaboratoryScience
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LaboratoryScienceInheritedProperties(TypedDict):
    """A medical science pertaining to chemical, hematological, immunologic, microscopic, or bacteriological diagnostic analyses or research.

    References:
        https://schema.org/LaboratoryScience
    Note:
        Model Depth 6
    Attributes:
    """


class LaboratoryScienceProperties(TypedDict):
    """A medical science pertaining to chemical, hematological, immunologic, microscopic, or bacteriological diagnostic analyses or research.

    References:
        https://schema.org/LaboratoryScience
    Note:
        Model Depth 6
    Attributes:
    """


class LaboratoryScienceAllProperties(
    LaboratoryScienceInheritedProperties, LaboratoryScienceProperties, TypedDict
):
    pass


class LaboratoryScienceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LaboratoryScience", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LaboratoryScienceProperties,
        LaboratoryScienceInheritedProperties,
        LaboratoryScienceAllProperties,
    ] = LaboratoryScienceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LaboratoryScience"
    return model


LaboratoryScience = create_schema_org_model()


def create_laboratoryscience_model(
    model: Union[
        LaboratoryScienceProperties,
        LaboratoryScienceInheritedProperties,
        LaboratoryScienceAllProperties,
    ]
):
    _type = deepcopy(LaboratoryScienceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LaboratoryScienceAllProperties):
    pydantic_type = create_laboratoryscience_model(model=model)
    return pydantic_type(model).schema_json()
