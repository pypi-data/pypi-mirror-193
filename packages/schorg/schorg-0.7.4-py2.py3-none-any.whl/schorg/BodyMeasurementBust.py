"""
Maximum girth of bust. Used, for example, to fit women's suits.

https://schema.org/BodyMeasurementBust
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementBustInheritedProperties(TypedDict):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    References:
        https://schema.org/BodyMeasurementBust
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementBustProperties(TypedDict):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    References:
        https://schema.org/BodyMeasurementBust
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementBustAllProperties(
    BodyMeasurementBustInheritedProperties, BodyMeasurementBustProperties, TypedDict
):
    pass


class BodyMeasurementBustBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementBust", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementBustProperties,
        BodyMeasurementBustInheritedProperties,
        BodyMeasurementBustAllProperties,
    ] = BodyMeasurementBustAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementBust"
    return model


BodyMeasurementBust = create_schema_org_model()


def create_bodymeasurementbust_model(
    model: Union[
        BodyMeasurementBustProperties,
        BodyMeasurementBustInheritedProperties,
        BodyMeasurementBustAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementBustAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BodyMeasurementBustAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BodyMeasurementBustAllProperties):
    pydantic_type = create_bodymeasurementbust_model(model=model)
    return pydantic_type(model).schema_json()
