"""
A general code for cases where relevance to children is reduced, e.g. adult education, mortgages, retirement-related products, etc.

https://schema.org/ReducedRelevanceForChildrenConsideration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReducedRelevanceForChildrenConsiderationInheritedProperties(TypedDict):
    """A general code for cases where relevance to children is reduced, e.g. adult education, mortgages, retirement-related products, etc.

    References:
        https://schema.org/ReducedRelevanceForChildrenConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class ReducedRelevanceForChildrenConsiderationProperties(TypedDict):
    """A general code for cases where relevance to children is reduced, e.g. adult education, mortgages, retirement-related products, etc.

    References:
        https://schema.org/ReducedRelevanceForChildrenConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class ReducedRelevanceForChildrenConsiderationAllProperties(
    ReducedRelevanceForChildrenConsiderationInheritedProperties,
    ReducedRelevanceForChildrenConsiderationProperties,
    TypedDict,
):
    pass


class ReducedRelevanceForChildrenConsiderationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(
        default="ReducedRelevanceForChildrenConsideration", alias="@id"
    )
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReducedRelevanceForChildrenConsiderationProperties,
        ReducedRelevanceForChildrenConsiderationInheritedProperties,
        ReducedRelevanceForChildrenConsiderationAllProperties,
    ] = ReducedRelevanceForChildrenConsiderationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReducedRelevanceForChildrenConsideration"
    return model


ReducedRelevanceForChildrenConsideration = create_schema_org_model()


def create_reducedrelevanceforchildrenconsideration_model(
    model: Union[
        ReducedRelevanceForChildrenConsiderationProperties,
        ReducedRelevanceForChildrenConsiderationInheritedProperties,
        ReducedRelevanceForChildrenConsiderationAllProperties,
    ]
):
    _type = deepcopy(ReducedRelevanceForChildrenConsiderationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReducedRelevanceForChildrenConsideration. Please see: https://schema.org/ReducedRelevanceForChildrenConsideration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReducedRelevanceForChildrenConsiderationAllProperties):
    pydantic_type = create_reducedrelevanceforchildrenconsideration_model(model=model)
    return pydantic_type(model).schema_json()
