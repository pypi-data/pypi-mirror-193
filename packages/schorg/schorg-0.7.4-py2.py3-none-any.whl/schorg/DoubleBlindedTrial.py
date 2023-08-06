"""
A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to.

https://schema.org/DoubleBlindedTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DoubleBlindedTrialInheritedProperties(TypedDict):
    """A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to.

    References:
        https://schema.org/DoubleBlindedTrial
    Note:
        Model Depth 6
    Attributes:
    """


class DoubleBlindedTrialProperties(TypedDict):
    """A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to.

    References:
        https://schema.org/DoubleBlindedTrial
    Note:
        Model Depth 6
    Attributes:
    """


class DoubleBlindedTrialAllProperties(
    DoubleBlindedTrialInheritedProperties, DoubleBlindedTrialProperties, TypedDict
):
    pass


class DoubleBlindedTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DoubleBlindedTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DoubleBlindedTrialProperties,
        DoubleBlindedTrialInheritedProperties,
        DoubleBlindedTrialAllProperties,
    ] = DoubleBlindedTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DoubleBlindedTrial"
    return model


DoubleBlindedTrial = create_schema_org_model()


def create_doubleblindedtrial_model(
    model: Union[
        DoubleBlindedTrialProperties,
        DoubleBlindedTrialInheritedProperties,
        DoubleBlindedTrialAllProperties,
    ]
):
    _type = deepcopy(DoubleBlindedTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DoubleBlindedTrialAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DoubleBlindedTrialAllProperties):
    pydantic_type = create_doubleblindedtrial_model(model=model)
    return pydantic_type(model).schema_json()
