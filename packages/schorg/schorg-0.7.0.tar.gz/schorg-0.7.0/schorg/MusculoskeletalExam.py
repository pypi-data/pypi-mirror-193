"""
Musculoskeletal system clinical examination.

https://schema.org/MusculoskeletalExam
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(MusculoskeletalExamInheritedProperties , MusculoskeletalExamProperties, TypedDict):
    pass


class MusculoskeletalExamBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MusculoskeletalExam",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MusculoskeletalExamProperties, MusculoskeletalExamInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusculoskeletalExam"
    return model
    

MusculoskeletalExam = create_schema_org_model()


def create_musculoskeletalexam_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_musculoskeletalexam_model(model=model)
    return pydantic_type(model).schema_json()


