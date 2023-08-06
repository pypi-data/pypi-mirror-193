"""
A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.

https://schema.org/SingleBlindedTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class SingleBlindedTrialAllProperties(
    SingleBlindedTrialInheritedProperties, SingleBlindedTrialProperties, TypedDict
):
    pass


class SingleBlindedTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SingleBlindedTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SingleBlindedTrialProperties,
        SingleBlindedTrialInheritedProperties,
        SingleBlindedTrialAllProperties,
    ] = SingleBlindedTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SingleBlindedTrial"
    return model


SingleBlindedTrial = create_schema_org_model()


def create_singleblindedtrial_model(
    model: Union[
        SingleBlindedTrialProperties,
        SingleBlindedTrialInheritedProperties,
        SingleBlindedTrialAllProperties,
    ]
):
    _type = deepcopy(SingleBlindedTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SingleBlindedTrialAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SingleBlindedTrialAllProperties):
    pydantic_type = create_singleblindedtrial_model(model=model)
    return pydantic_type(model).schema_json()
