"""
Measurement of the collar, for example of a shirt

https://schema.org/WearableMeasurementCollar
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementCollarInheritedProperties(TypedDict):
    """Measurement of the collar, for example of a shirt

    References:
        https://schema.org/WearableMeasurementCollar
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementCollarProperties(TypedDict):
    """Measurement of the collar, for example of a shirt

    References:
        https://schema.org/WearableMeasurementCollar
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementCollarAllProperties(
    WearableMeasurementCollarInheritedProperties,
    WearableMeasurementCollarProperties,
    TypedDict,
):
    pass


class WearableMeasurementCollarBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementCollar", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementCollarProperties,
        WearableMeasurementCollarInheritedProperties,
        WearableMeasurementCollarAllProperties,
    ] = WearableMeasurementCollarAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementCollar"
    return model


WearableMeasurementCollar = create_schema_org_model()


def create_wearablemeasurementcollar_model(
    model: Union[
        WearableMeasurementCollarProperties,
        WearableMeasurementCollarInheritedProperties,
        WearableMeasurementCollarAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementCollarAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableMeasurementCollarAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableMeasurementCollarAllProperties):
    pydantic_type = create_wearablemeasurementcollar_model(model=model)
    return pydantic_type(model).schema_json()
