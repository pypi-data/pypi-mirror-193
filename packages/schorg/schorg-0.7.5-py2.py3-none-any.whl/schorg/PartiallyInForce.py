"""
Indicates that parts of the legislation are in force, and parts are not.

https://schema.org/PartiallyInForce
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PartiallyInForceInheritedProperties(TypedDict):
    """Indicates that parts of the legislation are in force, and parts are not.

    References:
        https://schema.org/PartiallyInForce
    Note:
        Model Depth 6
    Attributes:
    """


class PartiallyInForceProperties(TypedDict):
    """Indicates that parts of the legislation are in force, and parts are not.

    References:
        https://schema.org/PartiallyInForce
    Note:
        Model Depth 6
    Attributes:
    """


class PartiallyInForceAllProperties(
    PartiallyInForceInheritedProperties, PartiallyInForceProperties, TypedDict
):
    pass


class PartiallyInForceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PartiallyInForce", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PartiallyInForceProperties,
        PartiallyInForceInheritedProperties,
        PartiallyInForceAllProperties,
    ] = PartiallyInForceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PartiallyInForce"
    return model


PartiallyInForce = create_schema_org_model()


def create_partiallyinforce_model(
    model: Union[
        PartiallyInForceProperties,
        PartiallyInForceInheritedProperties,
        PartiallyInForceAllProperties,
    ]
):
    _type = deepcopy(PartiallyInForceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PartiallyInForce. Please see: https://schema.org/PartiallyInForce"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PartiallyInForceAllProperties):
    pydantic_type = create_partiallyinforce_model(model=model)
    return pydantic_type(model).schema_json()
