"""
HealthCare: this is a benefit for health care.

https://schema.org/HealthCare
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthCareInheritedProperties(TypedDict):
    """HealthCare: this is a benefit for health care.

    References:
        https://schema.org/HealthCare
    Note:
        Model Depth 5
    Attributes:
    """


class HealthCareProperties(TypedDict):
    """HealthCare: this is a benefit for health care.

    References:
        https://schema.org/HealthCare
    Note:
        Model Depth 5
    Attributes:
    """


class HealthCareAllProperties(
    HealthCareInheritedProperties, HealthCareProperties, TypedDict
):
    pass


class HealthCareBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HealthCare", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HealthCareProperties, HealthCareInheritedProperties, HealthCareAllProperties
    ] = HealthCareAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthCare"
    return model


HealthCare = create_schema_org_model()


def create_healthcare_model(
    model: Union[
        HealthCareProperties, HealthCareInheritedProperties, HealthCareAllProperties
    ]
):
    _type = deepcopy(HealthCareAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HealthCareAllProperties):
    pydantic_type = create_healthcare_model(model=model)
    return pydantic_type(model).schema_json()
