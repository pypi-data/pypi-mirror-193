"""
Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs.

https://schema.org/TobaccoNicotineConsideration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TobaccoNicotineConsiderationInheritedProperties(TypedDict):
    """Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs.

    References:
        https://schema.org/TobaccoNicotineConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class TobaccoNicotineConsiderationProperties(TypedDict):
    """Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs.

    References:
        https://schema.org/TobaccoNicotineConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class TobaccoNicotineConsiderationAllProperties(
    TobaccoNicotineConsiderationInheritedProperties,
    TobaccoNicotineConsiderationProperties,
    TypedDict,
):
    pass


class TobaccoNicotineConsiderationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TobaccoNicotineConsideration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TobaccoNicotineConsiderationProperties,
        TobaccoNicotineConsiderationInheritedProperties,
        TobaccoNicotineConsiderationAllProperties,
    ] = TobaccoNicotineConsiderationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TobaccoNicotineConsideration"
    return model


TobaccoNicotineConsideration = create_schema_org_model()


def create_tobacconicotineconsideration_model(
    model: Union[
        TobaccoNicotineConsiderationProperties,
        TobaccoNicotineConsiderationInheritedProperties,
        TobaccoNicotineConsiderationAllProperties,
    ]
):
    _type = deepcopy(TobaccoNicotineConsiderationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TobaccoNicotineConsiderationAllProperties):
    pydantic_type = create_tobacconicotineconsideration_model(model=model)
    return pydantic_type(model).schema_json()
