"""
NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).

https://schema.org/NonprofitSBBI
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NonprofitSBBIInheritedProperties(TypedDict):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).

    References:
        https://schema.org/NonprofitSBBI
    Note:
        Model Depth 6
    Attributes:
    """


class NonprofitSBBIProperties(TypedDict):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).

    References:
        https://schema.org/NonprofitSBBI
    Note:
        Model Depth 6
    Attributes:
    """


class NonprofitSBBIAllProperties(
    NonprofitSBBIInheritedProperties, NonprofitSBBIProperties, TypedDict
):
    pass


class NonprofitSBBIBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NonprofitSBBI", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NonprofitSBBIProperties,
        NonprofitSBBIInheritedProperties,
        NonprofitSBBIAllProperties,
    ] = NonprofitSBBIAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NonprofitSBBI"
    return model


NonprofitSBBI = create_schema_org_model()


def create_nonprofitsbbi_model(
    model: Union[
        NonprofitSBBIProperties,
        NonprofitSBBIInheritedProperties,
        NonprofitSBBIAllProperties,
    ]
):
    _type = deepcopy(NonprofitSBBIAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of NonprofitSBBI. Please see: https://schema.org/NonprofitSBBI"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: NonprofitSBBIAllProperties):
    pydantic_type = create_nonprofitsbbi_model(model=model)
    return pydantic_type(model).schema_json()
