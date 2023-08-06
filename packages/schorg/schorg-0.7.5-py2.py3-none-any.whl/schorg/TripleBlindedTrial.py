"""
A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.

https://schema.org/TripleBlindedTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class TripleBlindedTrialAllProperties(
    TripleBlindedTrialInheritedProperties, TripleBlindedTrialProperties, TypedDict
):
    pass


class TripleBlindedTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TripleBlindedTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TripleBlindedTrialProperties,
        TripleBlindedTrialInheritedProperties,
        TripleBlindedTrialAllProperties,
    ] = TripleBlindedTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TripleBlindedTrial"
    return model


TripleBlindedTrial = create_schema_org_model()


def create_tripleblindedtrial_model(
    model: Union[
        TripleBlindedTrialProperties,
        TripleBlindedTrialInheritedProperties,
        TripleBlindedTrialAllProperties,
    ]
):
    _type = deepcopy(TripleBlindedTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TripleBlindedTrial. Please see: https://schema.org/TripleBlindedTrial"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TripleBlindedTrialAllProperties):
    pydantic_type = create_tripleblindedtrial_model(model=model)
    return pydantic_type(model).schema_json()
