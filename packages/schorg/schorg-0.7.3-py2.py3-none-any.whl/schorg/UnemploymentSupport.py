"""
UnemploymentSupport: this is a benefit for unemployment support.

https://schema.org/UnemploymentSupport
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UnemploymentSupportInheritedProperties(TypedDict):
    """UnemploymentSupport: this is a benefit for unemployment support.

    References:
        https://schema.org/UnemploymentSupport
    Note:
        Model Depth 5
    Attributes:
    """


class UnemploymentSupportProperties(TypedDict):
    """UnemploymentSupport: this is a benefit for unemployment support.

    References:
        https://schema.org/UnemploymentSupport
    Note:
        Model Depth 5
    Attributes:
    """


class UnemploymentSupportAllProperties(
    UnemploymentSupportInheritedProperties, UnemploymentSupportProperties, TypedDict
):
    pass


class UnemploymentSupportBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UnemploymentSupport", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UnemploymentSupportProperties,
        UnemploymentSupportInheritedProperties,
        UnemploymentSupportAllProperties,
    ] = UnemploymentSupportAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UnemploymentSupport"
    return model


UnemploymentSupport = create_schema_org_model()


def create_unemploymentsupport_model(
    model: Union[
        UnemploymentSupportProperties,
        UnemploymentSupportInheritedProperties,
        UnemploymentSupportAllProperties,
    ]
):
    _type = deepcopy(UnemploymentSupportAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UnemploymentSupportAllProperties):
    pydantic_type = create_unemploymentsupport_model(model=model)
    return pydantic_type(model).schema_json()
