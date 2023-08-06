"""
Results are available.

https://schema.org/ResultsAvailable
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ResultsAvailableInheritedProperties(TypedDict):
    """Results are available.

    References:
        https://schema.org/ResultsAvailable
    Note:
        Model Depth 6
    Attributes:
    """


class ResultsAvailableProperties(TypedDict):
    """Results are available.

    References:
        https://schema.org/ResultsAvailable
    Note:
        Model Depth 6
    Attributes:
    """


class ResultsAvailableAllProperties(
    ResultsAvailableInheritedProperties, ResultsAvailableProperties, TypedDict
):
    pass


class ResultsAvailableBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ResultsAvailable", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ResultsAvailableProperties,
        ResultsAvailableInheritedProperties,
        ResultsAvailableAllProperties,
    ] = ResultsAvailableAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ResultsAvailable"
    return model


ResultsAvailable = create_schema_org_model()


def create_resultsavailable_model(
    model: Union[
        ResultsAvailableProperties,
        ResultsAvailableInheritedProperties,
        ResultsAvailableAllProperties,
    ]
):
    _type = deepcopy(ResultsAvailableAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ResultsAvailableAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ResultsAvailableAllProperties):
    pydantic_type = create_resultsavailable_model(model=model)
    return pydantic_type(model).schema_json()
