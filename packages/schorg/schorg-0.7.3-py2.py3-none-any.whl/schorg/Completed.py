"""
Completed.

https://schema.org/Completed
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CompletedInheritedProperties(TypedDict):
    """Completed.

    References:
        https://schema.org/Completed
    Note:
        Model Depth 6
    Attributes:
    """


class CompletedProperties(TypedDict):
    """Completed.

    References:
        https://schema.org/Completed
    Note:
        Model Depth 6
    Attributes:
    """


class CompletedAllProperties(
    CompletedInheritedProperties, CompletedProperties, TypedDict
):
    pass


class CompletedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Completed", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CompletedProperties, CompletedInheritedProperties, CompletedAllProperties
    ] = CompletedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Completed"
    return model


Completed = create_schema_org_model()


def create_completed_model(
    model: Union[
        CompletedProperties, CompletedInheritedProperties, CompletedAllProperties
    ]
):
    _type = deepcopy(CompletedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CompletedAllProperties):
    pydantic_type = create_completed_model(model=model)
    return pydantic_type(model).schema_json()
