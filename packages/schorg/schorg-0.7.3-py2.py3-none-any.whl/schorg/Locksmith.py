"""
A locksmith.

https://schema.org/Locksmith
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LocksmithInheritedProperties(TypedDict):
    """A locksmith.

    References:
        https://schema.org/Locksmith
    Note:
        Model Depth 5
    Attributes:
    """


class LocksmithProperties(TypedDict):
    """A locksmith.

    References:
        https://schema.org/Locksmith
    Note:
        Model Depth 5
    Attributes:
    """


class LocksmithAllProperties(
    LocksmithInheritedProperties, LocksmithProperties, TypedDict
):
    pass


class LocksmithBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Locksmith", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LocksmithProperties, LocksmithInheritedProperties, LocksmithAllProperties
    ] = LocksmithAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Locksmith"
    return model


Locksmith = create_schema_org_model()


def create_locksmith_model(
    model: Union[
        LocksmithProperties, LocksmithInheritedProperties, LocksmithAllProperties
    ]
):
    _type = deepcopy(LocksmithAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LocksmithAllProperties):
    pydantic_type = create_locksmith_model(model=model)
    return pydantic_type(model).schema_json()
