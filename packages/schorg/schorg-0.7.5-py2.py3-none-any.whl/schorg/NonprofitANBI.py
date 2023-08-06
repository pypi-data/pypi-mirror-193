"""
NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

https://schema.org/NonprofitANBI
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NonprofitANBIInheritedProperties(TypedDict):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    References:
        https://schema.org/NonprofitANBI
    Note:
        Model Depth 6
    Attributes:
    """


class NonprofitANBIProperties(TypedDict):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    References:
        https://schema.org/NonprofitANBI
    Note:
        Model Depth 6
    Attributes:
    """


class NonprofitANBIAllProperties(
    NonprofitANBIInheritedProperties, NonprofitANBIProperties, TypedDict
):
    pass


class NonprofitANBIBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NonprofitANBI", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NonprofitANBIProperties,
        NonprofitANBIInheritedProperties,
        NonprofitANBIAllProperties,
    ] = NonprofitANBIAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NonprofitANBI"
    return model


NonprofitANBI = create_schema_org_model()


def create_nonprofitanbi_model(
    model: Union[
        NonprofitANBIProperties,
        NonprofitANBIInheritedProperties,
        NonprofitANBIAllProperties,
    ]
):
    _type = deepcopy(NonprofitANBIAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of NonprofitANBI. Please see: https://schema.org/NonprofitANBI"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: NonprofitANBIAllProperties):
    pydantic_type = create_nonprofitanbi_model(model=model)
    return pydantic_type(model).schema_json()
