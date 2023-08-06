"""
An in-progress action (e.g., while watching the movie, or driving to a location).

https://schema.org/ActiveActionStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActiveActionStatusInheritedProperties(TypedDict):
    """An in-progress action (e.g., while watching the movie, or driving to a location).

    References:
        https://schema.org/ActiveActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class ActiveActionStatusProperties(TypedDict):
    """An in-progress action (e.g., while watching the movie, or driving to a location).

    References:
        https://schema.org/ActiveActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class ActiveActionStatusAllProperties(
    ActiveActionStatusInheritedProperties, ActiveActionStatusProperties, TypedDict
):
    pass


class ActiveActionStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ActiveActionStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ActiveActionStatusProperties,
        ActiveActionStatusInheritedProperties,
        ActiveActionStatusAllProperties,
    ] = ActiveActionStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActiveActionStatus"
    return model


ActiveActionStatus = create_schema_org_model()


def create_activeactionstatus_model(
    model: Union[
        ActiveActionStatusProperties,
        ActiveActionStatusInheritedProperties,
        ActiveActionStatusAllProperties,
    ]
):
    _type = deepcopy(ActiveActionStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ActiveActionStatusAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ActiveActionStatusAllProperties):
    pydantic_type = create_activeactionstatus_model(model=model)
    return pydantic_type(model).schema_json()
