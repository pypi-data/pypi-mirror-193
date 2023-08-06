"""
Medical researchers.

https://schema.org/MedicalResearcher
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(MedicalResearcherInheritedProperties , MedicalResearcherProperties, TypedDict):
    pass


class MedicalResearcherBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalResearcher",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalResearcherProperties, MedicalResearcherInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalResearcher"
    return model
    

MedicalResearcher = create_schema_org_model()


def create_medicalresearcher_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalresearcher_model(model=model)
    return pydantic_type(model).schema_json()


