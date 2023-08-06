"""
A description of an action that is supported.

https://schema.org/PotentialActionStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PotentialActionStatusInheritedProperties(TypedDict):
    """A description of an action that is supported.

    References:
        https://schema.org/PotentialActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class PotentialActionStatusProperties(TypedDict):
    """A description of an action that is supported.

    References:
        https://schema.org/PotentialActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class PotentialActionStatusAllProperties(
    PotentialActionStatusInheritedProperties, PotentialActionStatusProperties, TypedDict
):
    pass


class PotentialActionStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PotentialActionStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PotentialActionStatusProperties,
        PotentialActionStatusInheritedProperties,
        PotentialActionStatusAllProperties,
    ] = PotentialActionStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PotentialActionStatus"
    return model


PotentialActionStatus = create_schema_org_model()


def create_potentialactionstatus_model(
    model: Union[
        PotentialActionStatusProperties,
        PotentialActionStatusInheritedProperties,
        PotentialActionStatusAllProperties,
    ]
):
    _type = deepcopy(PotentialActionStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PotentialActionStatusAllProperties):
    pydantic_type = create_potentialactionstatus_model(model=model)
    return pydantic_type(model).schema_json()
