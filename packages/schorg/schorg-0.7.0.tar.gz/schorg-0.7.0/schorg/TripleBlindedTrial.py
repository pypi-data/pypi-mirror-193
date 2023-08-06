"""
A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.

https://schema.org/TripleBlindedTrial
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TripleBlindedTrialInheritedProperties(TypedDict):
    """A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.

    References:
        https://schema.org/TripleBlindedTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class TripleBlindedTrialProperties(TypedDict):
    """A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.

    References:
        https://schema.org/TripleBlindedTrial
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(TripleBlindedTrialInheritedProperties , TripleBlindedTrialProperties, TypedDict):
    pass


class TripleBlindedTrialBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TripleBlindedTrial",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TripleBlindedTrialProperties, TripleBlindedTrialInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TripleBlindedTrial"
    return model
    

TripleBlindedTrial = create_schema_org_model()


def create_tripleblindedtrial_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_tripleblindedtrial_model(model=model)
    return pydantic_type(model).schema_json()


