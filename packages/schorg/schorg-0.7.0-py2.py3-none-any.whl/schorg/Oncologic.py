"""
A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.

https://schema.org/Oncologic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OncologicInheritedProperties(TypedDict):
    """A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.

    References:
        https://schema.org/Oncologic
    Note:
        Model Depth 5
    Attributes:
    """

    


class OncologicProperties(TypedDict):
    """A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.

    References:
        https://schema.org/Oncologic
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(OncologicInheritedProperties , OncologicProperties, TypedDict):
    pass


class OncologicBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Oncologic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OncologicProperties, OncologicInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Oncologic"
    return model
    

Oncologic = create_schema_org_model()


def create_oncologic_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_oncologic_model(model=model)
    return pydantic_type(model).schema_json()


