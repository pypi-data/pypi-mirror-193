"""
Design models for medical trials. Enumerated type.

https://schema.org/MedicalTrialDesign
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalTrialDesignInheritedProperties(TypedDict):
    """Design models for medical trials. Enumerated type.

    References:
        https://schema.org/MedicalTrialDesign
    Note:
        Model Depth 5
    Attributes:
    """

    


class MedicalTrialDesignProperties(TypedDict):
    """Design models for medical trials. Enumerated type.

    References:
        https://schema.org/MedicalTrialDesign
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalTrialDesignInheritedProperties , MedicalTrialDesignProperties, TypedDict):
    pass


class MedicalTrialDesignBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalTrialDesign",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalTrialDesignProperties, MedicalTrialDesignInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalTrialDesign"
    return model
    

MedicalTrialDesign = create_schema_org_model()


def create_medicaltrialdesign_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicaltrialdesign_model(model=model)
    return pydantic_type(model).schema_json()


