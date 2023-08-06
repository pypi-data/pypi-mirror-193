"""
Enumerates common types of measurement for wearables products.

https://schema.org/WearableMeasurementTypeEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementTypeEnumerationInheritedProperties(TypedDict):
    """Enumerates common types of measurement for wearables products.

    References:
        https://schema.org/WearableMeasurementTypeEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class WearableMeasurementTypeEnumerationProperties(TypedDict):
    """Enumerates common types of measurement for wearables products.

    References:
        https://schema.org/WearableMeasurementTypeEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class WearableMeasurementTypeEnumerationAllProperties(
    WearableMeasurementTypeEnumerationInheritedProperties,
    WearableMeasurementTypeEnumerationProperties,
    TypedDict,
):
    pass


class WearableMeasurementTypeEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(
        default="WearableMeasurementTypeEnumeration", alias="@id"
    )
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementTypeEnumerationProperties,
        WearableMeasurementTypeEnumerationInheritedProperties,
        WearableMeasurementTypeEnumerationAllProperties,
    ] = WearableMeasurementTypeEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementTypeEnumeration"
    return model


WearableMeasurementTypeEnumeration = create_schema_org_model()


def create_wearablemeasurementtypeenumeration_model(
    model: Union[
        WearableMeasurementTypeEnumerationProperties,
        WearableMeasurementTypeEnumerationInheritedProperties,
        WearableMeasurementTypeEnumerationAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementTypeEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableMeasurementTypeEnumerationAllProperties"
            )
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableMeasurementTypeEnumerationAllProperties):
    pydantic_type = create_wearablemeasurementtypeenumeration_model(model=model)
    return pydantic_type(model).schema_json()
