"""
A business that provides Heating, Ventilation and Air Conditioning services.

https://schema.org/HVACBusiness
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HVACBusinessInheritedProperties(TypedDict):
    """A business that provides Heating, Ventilation and Air Conditioning services.

    References:
        https://schema.org/HVACBusiness
    Note:
        Model Depth 5
    Attributes:
    """


class HVACBusinessProperties(TypedDict):
    """A business that provides Heating, Ventilation and Air Conditioning services.

    References:
        https://schema.org/HVACBusiness
    Note:
        Model Depth 5
    Attributes:
    """


class HVACBusinessAllProperties(
    HVACBusinessInheritedProperties, HVACBusinessProperties, TypedDict
):
    pass


class HVACBusinessBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HVACBusiness", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HVACBusinessProperties,
        HVACBusinessInheritedProperties,
        HVACBusinessAllProperties,
    ] = HVACBusinessAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HVACBusiness"
    return model


HVACBusiness = create_schema_org_model()


def create_hvacbusiness_model(
    model: Union[
        HVACBusinessProperties,
        HVACBusinessInheritedProperties,
        HVACBusinessAllProperties,
    ]
):
    _type = deepcopy(HVACBusinessAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HVACBusinessAllProperties):
    pydantic_type = create_hvacbusiness_model(model=model)
    return pydantic_type(model).schema_json()
