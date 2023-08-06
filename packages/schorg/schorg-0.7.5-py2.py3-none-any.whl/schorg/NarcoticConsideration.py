"""
Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin.

https://schema.org/NarcoticConsideration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NarcoticConsiderationInheritedProperties(TypedDict):
    """Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin.

    References:
        https://schema.org/NarcoticConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class NarcoticConsiderationProperties(TypedDict):
    """Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin.

    References:
        https://schema.org/NarcoticConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class NarcoticConsiderationAllProperties(
    NarcoticConsiderationInheritedProperties, NarcoticConsiderationProperties, TypedDict
):
    pass


class NarcoticConsiderationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NarcoticConsideration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NarcoticConsiderationProperties,
        NarcoticConsiderationInheritedProperties,
        NarcoticConsiderationAllProperties,
    ] = NarcoticConsiderationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NarcoticConsideration"
    return model


NarcoticConsideration = create_schema_org_model()


def create_narcoticconsideration_model(
    model: Union[
        NarcoticConsiderationProperties,
        NarcoticConsiderationInheritedProperties,
        NarcoticConsiderationAllProperties,
    ]
):
    _type = deepcopy(NarcoticConsiderationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of NarcoticConsideration. Please see: https://schema.org/NarcoticConsideration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: NarcoticConsiderationAllProperties):
    pydantic_type = create_narcoticconsideration_model(model=model)
    return pydantic_type(model).schema_json()
