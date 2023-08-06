"""
UKNonprofitType: Non-profit organization type originating from the United Kingdom.

https://schema.org/UKNonprofitType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UKNonprofitTypeInheritedProperties(TypedDict):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    References:
        https://schema.org/UKNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """


class UKNonprofitTypeProperties(TypedDict):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    References:
        https://schema.org/UKNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """


class UKNonprofitTypeAllProperties(
    UKNonprofitTypeInheritedProperties, UKNonprofitTypeProperties, TypedDict
):
    pass


class UKNonprofitTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UKNonprofitType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UKNonprofitTypeProperties,
        UKNonprofitTypeInheritedProperties,
        UKNonprofitTypeAllProperties,
    ] = UKNonprofitTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UKNonprofitType"
    return model


UKNonprofitType = create_schema_org_model()


def create_uknonprofittype_model(
    model: Union[
        UKNonprofitTypeProperties,
        UKNonprofitTypeInheritedProperties,
        UKNonprofitTypeAllProperties,
    ]
):
    _type = deepcopy(UKNonprofitTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of UKNonprofitTypeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UKNonprofitTypeAllProperties):
    pydantic_type = create_uknonprofittype_model(model=model)
    return pydantic_type(model).schema_json()
