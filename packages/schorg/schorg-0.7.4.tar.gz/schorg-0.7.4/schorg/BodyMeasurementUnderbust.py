"""
Girth of body just below the bust. Used, for example, to fit women's swimwear.

https://schema.org/BodyMeasurementUnderbust
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementUnderbustInheritedProperties(TypedDict):
    """Girth of body just below the bust. Used, for example, to fit women's swimwear.

    References:
        https://schema.org/BodyMeasurementUnderbust
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementUnderbustProperties(TypedDict):
    """Girth of body just below the bust. Used, for example, to fit women's swimwear.

    References:
        https://schema.org/BodyMeasurementUnderbust
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementUnderbustAllProperties(
    BodyMeasurementUnderbustInheritedProperties,
    BodyMeasurementUnderbustProperties,
    TypedDict,
):
    pass


class BodyMeasurementUnderbustBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementUnderbust", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementUnderbustProperties,
        BodyMeasurementUnderbustInheritedProperties,
        BodyMeasurementUnderbustAllProperties,
    ] = BodyMeasurementUnderbustAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementUnderbust"
    return model


BodyMeasurementUnderbust = create_schema_org_model()


def create_bodymeasurementunderbust_model(
    model: Union[
        BodyMeasurementUnderbustProperties,
        BodyMeasurementUnderbustInheritedProperties,
        BodyMeasurementUnderbustAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementUnderbustAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BodyMeasurementUnderbustAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BodyMeasurementUnderbustAllProperties):
    pydantic_type = create_bodymeasurementunderbust_model(model=model)
    return pydantic_type(model).schema_json()
