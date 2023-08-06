"""
Measurement of the inseam, for example of pants

https://schema.org/WearableMeasurementInseam
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementInseamInheritedProperties(TypedDict):
    """Measurement of the inseam, for example of pants

    References:
        https://schema.org/WearableMeasurementInseam
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementInseamProperties(TypedDict):
    """Measurement of the inseam, for example of pants

    References:
        https://schema.org/WearableMeasurementInseam
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementInseamAllProperties(
    WearableMeasurementInseamInheritedProperties,
    WearableMeasurementInseamProperties,
    TypedDict,
):
    pass


class WearableMeasurementInseamBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementInseam", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementInseamProperties,
        WearableMeasurementInseamInheritedProperties,
        WearableMeasurementInseamAllProperties,
    ] = WearableMeasurementInseamAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementInseam"
    return model


WearableMeasurementInseam = create_schema_org_model()


def create_wearablemeasurementinseam_model(
    model: Union[
        WearableMeasurementInseamProperties,
        WearableMeasurementInseamInheritedProperties,
        WearableMeasurementInseamAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementInseamAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableMeasurementInseamAllProperties):
    pydantic_type = create_wearablemeasurementinseam_model(model=model)
    return pydantic_type(model).schema_json()
