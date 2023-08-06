"""
Cardiovascular system assessment with clinical examination.

https://schema.org/CardiovascularExam
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(CardiovascularExamInheritedProperties , CardiovascularExamProperties, TypedDict):
    pass


class CardiovascularExamBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CardiovascularExam",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CardiovascularExamProperties, CardiovascularExamInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CardiovascularExam"
    return model
    

CardiovascularExam = create_schema_org_model()


def create_cardiovascularexam_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_cardiovascularexam_model(model=model)
    return pydantic_type(model).schema_json()


