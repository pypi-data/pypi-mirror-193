"""
DisabilitySupport: this is a benefit for disability support.

https://schema.org/DisabilitySupport
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DisabilitySupportInheritedProperties(TypedDict):
    """DisabilitySupport: this is a benefit for disability support.

    References:
        https://schema.org/DisabilitySupport
    Note:
        Model Depth 5
    Attributes:
    """


class DisabilitySupportProperties(TypedDict):
    """DisabilitySupport: this is a benefit for disability support.

    References:
        https://schema.org/DisabilitySupport
    Note:
        Model Depth 5
    Attributes:
    """


class DisabilitySupportAllProperties(
    DisabilitySupportInheritedProperties, DisabilitySupportProperties, TypedDict
):
    pass


class DisabilitySupportBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DisabilitySupport", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DisabilitySupportProperties,
        DisabilitySupportInheritedProperties,
        DisabilitySupportAllProperties,
    ] = DisabilitySupportAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DisabilitySupport"
    return model


DisabilitySupport = create_schema_org_model()


def create_disabilitysupport_model(
    model: Union[
        DisabilitySupportProperties,
        DisabilitySupportInheritedProperties,
        DisabilitySupportAllProperties,
    ]
):
    _type = deepcopy(DisabilitySupportAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DisabilitySupportAllProperties):
    pydantic_type = create_disabilitysupport_model(model=model)
    return pydantic_type(model).schema_json()
