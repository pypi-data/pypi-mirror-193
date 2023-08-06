"""
A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.

https://schema.org/FDAnotEvaluated
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAnotEvaluatedInheritedProperties(TypedDict):
    """A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.

    References:
        https://schema.org/FDAnotEvaluated
    Note:
        Model Depth 6
    Attributes:
    """


class FDAnotEvaluatedProperties(TypedDict):
    """A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.

    References:
        https://schema.org/FDAnotEvaluated
    Note:
        Model Depth 6
    Attributes:
    """


class FDAnotEvaluatedAllProperties(
    FDAnotEvaluatedInheritedProperties, FDAnotEvaluatedProperties, TypedDict
):
    pass


class FDAnotEvaluatedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FDAnotEvaluated", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FDAnotEvaluatedProperties,
        FDAnotEvaluatedInheritedProperties,
        FDAnotEvaluatedAllProperties,
    ] = FDAnotEvaluatedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAnotEvaluated"
    return model


FDAnotEvaluated = create_schema_org_model()


def create_fdanotevaluated_model(
    model: Union[
        FDAnotEvaluatedProperties,
        FDAnotEvaluatedInheritedProperties,
        FDAnotEvaluatedAllProperties,
    ]
):
    _type = deepcopy(FDAnotEvaluatedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FDAnotEvaluatedAllProperties):
    pydantic_type = create_fdanotevaluated_model(model=model)
    return pydantic_type(model).schema_json()
