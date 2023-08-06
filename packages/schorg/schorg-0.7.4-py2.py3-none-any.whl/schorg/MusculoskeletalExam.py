"""
Musculoskeletal system clinical examination.

https://schema.org/MusculoskeletalExam
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MusculoskeletalExamInheritedProperties(TypedDict):
    """Musculoskeletal system clinical examination.

    References:
        https://schema.org/MusculoskeletalExam
    Note:
        Model Depth 5
    Attributes:
    """


class MusculoskeletalExamProperties(TypedDict):
    """Musculoskeletal system clinical examination.

    References:
        https://schema.org/MusculoskeletalExam
    Note:
        Model Depth 5
    Attributes:
    """


class MusculoskeletalExamAllProperties(
    MusculoskeletalExamInheritedProperties, MusculoskeletalExamProperties, TypedDict
):
    pass


class MusculoskeletalExamBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MusculoskeletalExam", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MusculoskeletalExamProperties,
        MusculoskeletalExamInheritedProperties,
        MusculoskeletalExamAllProperties,
    ] = MusculoskeletalExamAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusculoskeletalExam"
    return model


MusculoskeletalExam = create_schema_org_model()


def create_musculoskeletalexam_model(
    model: Union[
        MusculoskeletalExamProperties,
        MusculoskeletalExamInheritedProperties,
        MusculoskeletalExamAllProperties,
    ]
):
    _type = deepcopy(MusculoskeletalExamAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MusculoskeletalExamAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MusculoskeletalExamAllProperties):
    pydantic_type = create_musculoskeletalexam_model(model=model)
    return pydantic_type(model).schema_json()
