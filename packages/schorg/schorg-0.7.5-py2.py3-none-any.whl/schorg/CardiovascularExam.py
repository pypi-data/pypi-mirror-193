"""
Cardiovascular system assessment with clinical examination.

https://schema.org/CardiovascularExam
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CardiovascularExamInheritedProperties(TypedDict):
    """Cardiovascular system assessment with clinical examination.

    References:
        https://schema.org/CardiovascularExam
    Note:
        Model Depth 5
    Attributes:
    """


class CardiovascularExamProperties(TypedDict):
    """Cardiovascular system assessment with clinical examination.

    References:
        https://schema.org/CardiovascularExam
    Note:
        Model Depth 5
    Attributes:
    """


class CardiovascularExamAllProperties(
    CardiovascularExamInheritedProperties, CardiovascularExamProperties, TypedDict
):
    pass


class CardiovascularExamBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CardiovascularExam", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CardiovascularExamProperties,
        CardiovascularExamInheritedProperties,
        CardiovascularExamAllProperties,
    ] = CardiovascularExamAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CardiovascularExam"
    return model


CardiovascularExam = create_schema_org_model()


def create_cardiovascularexam_model(
    model: Union[
        CardiovascularExamProperties,
        CardiovascularExamInheritedProperties,
        CardiovascularExamAllProperties,
    ]
):
    _type = deepcopy(CardiovascularExamAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CardiovascularExam. Please see: https://schema.org/CardiovascularExam"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CardiovascularExamAllProperties):
    pydantic_type = create_cardiovascularexam_model(model=model)
    return pydantic_type(model).schema_json()
