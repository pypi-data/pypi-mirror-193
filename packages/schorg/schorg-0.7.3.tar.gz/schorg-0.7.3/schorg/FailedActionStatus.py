"""
An action that failed to complete. The action's error property and the HTTP return code contain more information about the failure.

https://schema.org/FailedActionStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FailedActionStatusInheritedProperties(TypedDict):
    """An action that failed to complete. The action's error property and the HTTP return code contain more information about the failure.

    References:
        https://schema.org/FailedActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class FailedActionStatusProperties(TypedDict):
    """An action that failed to complete. The action's error property and the HTTP return code contain more information about the failure.

    References:
        https://schema.org/FailedActionStatus
    Note:
        Model Depth 6
    Attributes:
    """


class FailedActionStatusAllProperties(
    FailedActionStatusInheritedProperties, FailedActionStatusProperties, TypedDict
):
    pass


class FailedActionStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FailedActionStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FailedActionStatusProperties,
        FailedActionStatusInheritedProperties,
        FailedActionStatusAllProperties,
    ] = FailedActionStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FailedActionStatus"
    return model


FailedActionStatus = create_schema_org_model()


def create_failedactionstatus_model(
    model: Union[
        FailedActionStatusProperties,
        FailedActionStatusInheritedProperties,
        FailedActionStatusAllProperties,
    ]
):
    _type = deepcopy(FailedActionStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FailedActionStatusAllProperties):
    pydantic_type = create_failedactionstatus_model(model=model)
    return pydantic_type(model).schema_json()
