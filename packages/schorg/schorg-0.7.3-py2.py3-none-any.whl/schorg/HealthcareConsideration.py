"""
Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

https://schema.org/HealthcareConsideration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthcareConsiderationInheritedProperties(TypedDict):
    """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

    References:
        https://schema.org/HealthcareConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class HealthcareConsiderationProperties(TypedDict):
    """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

    References:
        https://schema.org/HealthcareConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class HealthcareConsiderationAllProperties(
    HealthcareConsiderationInheritedProperties,
    HealthcareConsiderationProperties,
    TypedDict,
):
    pass


class HealthcareConsiderationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HealthcareConsideration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HealthcareConsiderationProperties,
        HealthcareConsiderationInheritedProperties,
        HealthcareConsiderationAllProperties,
    ] = HealthcareConsiderationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthcareConsideration"
    return model


HealthcareConsideration = create_schema_org_model()


def create_healthcareconsideration_model(
    model: Union[
        HealthcareConsiderationProperties,
        HealthcareConsiderationInheritedProperties,
        HealthcareConsiderationAllProperties,
    ]
):
    _type = deepcopy(HealthcareConsiderationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HealthcareConsiderationAllProperties):
    pydantic_type = create_healthcareconsideration_model(model=model)
    return pydantic_type(model).schema_json()
