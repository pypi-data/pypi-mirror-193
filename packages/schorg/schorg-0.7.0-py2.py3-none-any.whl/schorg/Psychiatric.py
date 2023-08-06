"""
A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.

https://schema.org/Psychiatric
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PsychiatricInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.

    References:
        https://schema.org/Psychiatric
    Note:
        Model Depth 5
    Attributes:
    """

    


class PsychiatricProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.

    References:
        https://schema.org/Psychiatric
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PsychiatricInheritedProperties , PsychiatricProperties, TypedDict):
    pass


class PsychiatricBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Psychiatric",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PsychiatricProperties, PsychiatricInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Psychiatric"
    return model
    

Psychiatric = create_schema_org_model()


def create_psychiatric_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_psychiatric_model(model=model)
    return pydantic_type(model).schema_json()


