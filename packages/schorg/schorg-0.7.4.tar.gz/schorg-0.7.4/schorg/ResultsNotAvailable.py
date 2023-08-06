"""
Results are not available.

https://schema.org/ResultsNotAvailable
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ResultsNotAvailableInheritedProperties(TypedDict):
    """Results are not available.

    References:
        https://schema.org/ResultsNotAvailable
    Note:
        Model Depth 6
    Attributes:
    """


class ResultsNotAvailableProperties(TypedDict):
    """Results are not available.

    References:
        https://schema.org/ResultsNotAvailable
    Note:
        Model Depth 6
    Attributes:
    """


class ResultsNotAvailableAllProperties(
    ResultsNotAvailableInheritedProperties, ResultsNotAvailableProperties, TypedDict
):
    pass


class ResultsNotAvailableBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ResultsNotAvailable", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ResultsNotAvailableProperties,
        ResultsNotAvailableInheritedProperties,
        ResultsNotAvailableAllProperties,
    ] = ResultsNotAvailableAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ResultsNotAvailable"
    return model


ResultsNotAvailable = create_schema_org_model()


def create_resultsnotavailable_model(
    model: Union[
        ResultsNotAvailableProperties,
        ResultsNotAvailableInheritedProperties,
        ResultsNotAvailableAllProperties,
    ]
):
    _type = deepcopy(ResultsNotAvailableAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ResultsNotAvailableAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ResultsNotAvailableAllProperties):
    pydantic_type = create_resultsnotavailable_model(model=model)
    return pydantic_type(model).schema_json()
