"""
A trial design in which the researcher knows the full details of the treatment, and so does the patient.

https://schema.org/OpenTrial
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OpenTrialInheritedProperties(TypedDict):
    """A trial design in which the researcher knows the full details of the treatment, and so does the patient.

    References:
        https://schema.org/OpenTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class OpenTrialProperties(TypedDict):
    """A trial design in which the researcher knows the full details of the treatment, and so does the patient.

    References:
        https://schema.org/OpenTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(OpenTrialInheritedProperties , OpenTrialProperties, TypedDict):
    pass


class OpenTrialBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OpenTrial",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OpenTrialProperties, OpenTrialInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OpenTrial"
    return model
    

OpenTrial = create_schema_org_model()


def create_opentrial_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_opentrial_model(model=model)
    return pydantic_type(model).schema_json()


