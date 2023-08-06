"""
Data type: Floating number.

https://schema.org/Float
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FloatInheritedProperties(TypedDict):
    """Data type: Floating number.

    References:
        https://schema.org/Float
    Note:
        Model Depth 6
    Attributes:
    """


class FloatProperties(TypedDict):
    """Data type: Floating number.

    References:
        https://schema.org/Float
    Note:
        Model Depth 6
    Attributes:
    """


class FloatAllProperties(FloatInheritedProperties, FloatProperties, TypedDict):
    pass


class FloatBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Float", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FloatProperties, FloatInheritedProperties, FloatAllProperties
    ] = FloatAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Float"
    return model


Float = create_schema_org_model()


def create_float_model(
    model: Union[FloatProperties, FloatInheritedProperties, FloatAllProperties]
):
    _type = deepcopy(FloatAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FloatAllProperties):
    pydantic_type = create_float_model(model=model)
    return pydantic_type(model).schema_json()
