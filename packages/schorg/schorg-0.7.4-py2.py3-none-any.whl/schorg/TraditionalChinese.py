"""
A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions.

https://schema.org/TraditionalChinese
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TraditionalChineseInheritedProperties(TypedDict):
    """A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions.

    References:
        https://schema.org/TraditionalChinese
    Note:
        Model Depth 6
    Attributes:
    """


class TraditionalChineseProperties(TypedDict):
    """A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions.

    References:
        https://schema.org/TraditionalChinese
    Note:
        Model Depth 6
    Attributes:
    """


class TraditionalChineseAllProperties(
    TraditionalChineseInheritedProperties, TraditionalChineseProperties, TypedDict
):
    pass


class TraditionalChineseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TraditionalChinese", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TraditionalChineseProperties,
        TraditionalChineseInheritedProperties,
        TraditionalChineseAllProperties,
    ] = TraditionalChineseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TraditionalChinese"
    return model


TraditionalChinese = create_schema_org_model()


def create_traditionalchinese_model(
    model: Union[
        TraditionalChineseProperties,
        TraditionalChineseInheritedProperties,
        TraditionalChineseAllProperties,
    ]
):
    _type = deepcopy(TraditionalChineseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of TraditionalChineseAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TraditionalChineseAllProperties):
    pydantic_type = create_traditionalchinese_model(model=model)
    return pydantic_type(model).schema_json()
