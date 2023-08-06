"""
A tennis complex.

https://schema.org/TennisComplex
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TennisComplexInheritedProperties(TypedDict):
    """A tennis complex.

    References:
        https://schema.org/TennisComplex
    Note:
        Model Depth 5
    Attributes:
    """


class TennisComplexProperties(TypedDict):
    """A tennis complex.

    References:
        https://schema.org/TennisComplex
    Note:
        Model Depth 5
    Attributes:
    """


class TennisComplexAllProperties(
    TennisComplexInheritedProperties, TennisComplexProperties, TypedDict
):
    pass


class TennisComplexBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TennisComplex", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TennisComplexProperties,
        TennisComplexInheritedProperties,
        TennisComplexAllProperties,
    ] = TennisComplexAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TennisComplex"
    return model


TennisComplex = create_schema_org_model()


def create_tenniscomplex_model(
    model: Union[
        TennisComplexProperties,
        TennisComplexInheritedProperties,
        TennisComplexAllProperties,
    ]
):
    _type = deepcopy(TennisComplexAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TennisComplex. Please see: https://schema.org/TennisComplex"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TennisComplexAllProperties):
    pydantic_type = create_tenniscomplex_model(model=model)
    return pydantic_type(model).schema_json()
