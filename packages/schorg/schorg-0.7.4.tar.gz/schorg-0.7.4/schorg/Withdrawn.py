"""
Withdrawn.

https://schema.org/Withdrawn
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WithdrawnInheritedProperties(TypedDict):
    """Withdrawn.

    References:
        https://schema.org/Withdrawn
    Note:
        Model Depth 6
    Attributes:
    """


class WithdrawnProperties(TypedDict):
    """Withdrawn.

    References:
        https://schema.org/Withdrawn
    Note:
        Model Depth 6
    Attributes:
    """


class WithdrawnAllProperties(
    WithdrawnInheritedProperties, WithdrawnProperties, TypedDict
):
    pass


class WithdrawnBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Withdrawn", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WithdrawnProperties, WithdrawnInheritedProperties, WithdrawnAllProperties
    ] = WithdrawnAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Withdrawn"
    return model


Withdrawn = create_schema_org_model()


def create_withdrawn_model(
    model: Union[
        WithdrawnProperties, WithdrawnInheritedProperties, WithdrawnAllProperties
    ]
):
    _type = deepcopy(WithdrawnAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WithdrawnAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WithdrawnAllProperties):
    pydantic_type = create_withdrawn_model(model=model)
    return pydantic_type(model).schema_json()
