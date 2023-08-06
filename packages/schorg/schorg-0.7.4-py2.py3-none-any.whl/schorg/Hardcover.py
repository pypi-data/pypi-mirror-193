"""
Book format: Hardcover.

https://schema.org/Hardcover
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HardcoverInheritedProperties(TypedDict):
    """Book format: Hardcover.

    References:
        https://schema.org/Hardcover
    Note:
        Model Depth 5
    Attributes:
    """


class HardcoverProperties(TypedDict):
    """Book format: Hardcover.

    References:
        https://schema.org/Hardcover
    Note:
        Model Depth 5
    Attributes:
    """


class HardcoverAllProperties(
    HardcoverInheritedProperties, HardcoverProperties, TypedDict
):
    pass


class HardcoverBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Hardcover", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HardcoverProperties, HardcoverInheritedProperties, HardcoverAllProperties
    ] = HardcoverAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Hardcover"
    return model


Hardcover = create_schema_org_model()


def create_hardcover_model(
    model: Union[
        HardcoverProperties, HardcoverInheritedProperties, HardcoverAllProperties
    ]
):
    _type = deepcopy(HardcoverAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of HardcoverAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HardcoverAllProperties):
    pydantic_type = create_hardcover_model(model=model)
    return pydantic_type(model).schema_json()
