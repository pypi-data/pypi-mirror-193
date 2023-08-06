"""
An action that has already taken place.

https://schema.org/CompletedActionStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CompletedActionStatusInheritedProperties(TypedDict):
    """An action that has already taken place.

    References:
        https://schema.org/CompletedActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class CompletedActionStatusProperties(TypedDict):
    """An action that has already taken place.

    References:
        https://schema.org/CompletedActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class CompletedActionStatusAllProperties(
    CompletedActionStatusInheritedProperties, CompletedActionStatusProperties, TypedDict
):
    pass


class CompletedActionStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CompletedActionStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CompletedActionStatusProperties,
        CompletedActionStatusInheritedProperties,
        CompletedActionStatusAllProperties,
    ] = CompletedActionStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CompletedActionStatus"
    return model


CompletedActionStatus = create_schema_org_model()


def create_completedactionstatus_model(
    model: Union[
        CompletedActionStatusProperties,
        CompletedActionStatusInheritedProperties,
        CompletedActionStatusAllProperties,
    ]
):
    _type = deepcopy(CompletedActionStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CompletedActionStatusAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CompletedActionStatusAllProperties):
    pydantic_type = create_completedactionstatus_model(model=model)
    return pydantic_type(model).schema_json()
