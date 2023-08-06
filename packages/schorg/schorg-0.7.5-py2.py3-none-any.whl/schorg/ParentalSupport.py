"""
ParentalSupport: this is a benefit for parental support.

https://schema.org/ParentalSupport
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ParentalSupportInheritedProperties(TypedDict):
    """ParentalSupport: this is a benefit for parental support.

    References:
        https://schema.org/ParentalSupport
    Note:
        Model Depth 5
    Attributes:
    """


class ParentalSupportProperties(TypedDict):
    """ParentalSupport: this is a benefit for parental support.

    References:
        https://schema.org/ParentalSupport
    Note:
        Model Depth 5
    Attributes:
    """


class ParentalSupportAllProperties(
    ParentalSupportInheritedProperties, ParentalSupportProperties, TypedDict
):
    pass


class ParentalSupportBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ParentalSupport", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ParentalSupportProperties,
        ParentalSupportInheritedProperties,
        ParentalSupportAllProperties,
    ] = ParentalSupportAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParentalSupport"
    return model


ParentalSupport = create_schema_org_model()


def create_parentalsupport_model(
    model: Union[
        ParentalSupportProperties,
        ParentalSupportInheritedProperties,
        ParentalSupportAllProperties,
    ]
):
    _type = deepcopy(ParentalSupportAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ParentalSupport. Please see: https://schema.org/ParentalSupport"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ParentalSupportAllProperties):
    pydantic_type = create_parentalsupport_model(model=model)
    return pydantic_type(model).schema_json()
