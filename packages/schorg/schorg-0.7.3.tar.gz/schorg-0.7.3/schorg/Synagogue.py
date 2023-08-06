"""
A synagogue.

https://schema.org/Synagogue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SynagogueInheritedProperties(TypedDict):
    """A synagogue.

    References:
        https://schema.org/Synagogue
    Note:
        Model Depth 5
    Attributes:
    """


class SynagogueProperties(TypedDict):
    """A synagogue.

    References:
        https://schema.org/Synagogue
    Note:
        Model Depth 5
    Attributes:
    """


class SynagogueAllProperties(
    SynagogueInheritedProperties, SynagogueProperties, TypedDict
):
    pass


class SynagogueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Synagogue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SynagogueProperties, SynagogueInheritedProperties, SynagogueAllProperties
    ] = SynagogueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Synagogue"
    return model


Synagogue = create_schema_org_model()


def create_synagogue_model(
    model: Union[
        SynagogueProperties, SynagogueInheritedProperties, SynagogueAllProperties
    ]
):
    _type = deepcopy(SynagogueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SynagogueAllProperties):
    pydantic_type = create_synagogue_model(model=model)
    return pydantic_type(model).schema_json()
