"""
Represents the length, for example of a dress

https://schema.org/WearableMeasurementLength
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementLengthInheritedProperties(TypedDict):
    """Represents the length, for example of a dress

    References:
        https://schema.org/WearableMeasurementLength
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementLengthProperties(TypedDict):
    """Represents the length, for example of a dress

    References:
        https://schema.org/WearableMeasurementLength
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementLengthAllProperties(
    WearableMeasurementLengthInheritedProperties,
    WearableMeasurementLengthProperties,
    TypedDict,
):
    pass


class WearableMeasurementLengthBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementLength", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementLengthProperties,
        WearableMeasurementLengthInheritedProperties,
        WearableMeasurementLengthAllProperties,
    ] = WearableMeasurementLengthAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementLength"
    return model


WearableMeasurementLength = create_schema_org_model()


def create_wearablemeasurementlength_model(
    model: Union[
        WearableMeasurementLengthProperties,
        WearableMeasurementLengthInheritedProperties,
        WearableMeasurementLengthAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementLengthAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableMeasurementLength. Please see: https://schema.org/WearableMeasurementLength"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableMeasurementLengthAllProperties):
    pydantic_type = create_wearablemeasurementlength_model(model=model)
    return pydantic_type(model).schema_json()
