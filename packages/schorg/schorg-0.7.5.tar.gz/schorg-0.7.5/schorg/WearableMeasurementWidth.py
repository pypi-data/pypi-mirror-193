"""
Measurement of the width, for example of shoes

https://schema.org/WearableMeasurementWidth
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementWidthInheritedProperties(TypedDict):
    """Measurement of the width, for example of shoes

    References:
        https://schema.org/WearableMeasurementWidth
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementWidthProperties(TypedDict):
    """Measurement of the width, for example of shoes

    References:
        https://schema.org/WearableMeasurementWidth
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementWidthAllProperties(
    WearableMeasurementWidthInheritedProperties,
    WearableMeasurementWidthProperties,
    TypedDict,
):
    pass


class WearableMeasurementWidthBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementWidth", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementWidthProperties,
        WearableMeasurementWidthInheritedProperties,
        WearableMeasurementWidthAllProperties,
    ] = WearableMeasurementWidthAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementWidth"
    return model


WearableMeasurementWidth = create_schema_org_model()


def create_wearablemeasurementwidth_model(
    model: Union[
        WearableMeasurementWidthProperties,
        WearableMeasurementWidthInheritedProperties,
        WearableMeasurementWidthAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementWidthAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableMeasurementWidth. Please see: https://schema.org/WearableMeasurementWidth"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableMeasurementWidthAllProperties):
    pydantic_type = create_wearablemeasurementwidth_model(model=model)
    return pydantic_type(model).schema_json()
