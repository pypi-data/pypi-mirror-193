"""
A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.

https://schema.org/SingleBlindedTrial
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SingleBlindedTrialInheritedProperties(TypedDict):
    """A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.

    References:
        https://schema.org/SingleBlindedTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class SingleBlindedTrialProperties(TypedDict):
    """A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.

    References:
        https://schema.org/SingleBlindedTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(SingleBlindedTrialInheritedProperties , SingleBlindedTrialProperties, TypedDict):
    pass


class SingleBlindedTrialBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SingleBlindedTrial",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SingleBlindedTrialProperties, SingleBlindedTrialInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SingleBlindedTrial"
    return model
    

SingleBlindedTrial = create_schema_org_model()


def create_singleblindedtrial_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_singleblindedtrial_model(model=model)
    return pydantic_type(model).schema_json()


