"""
A country.

https://schema.org/Country
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CountryInheritedProperties(TypedDict):
    """A country.

    References:
        https://schema.org/Country
    Note:
        Model Depth 4
    Attributes:
    """


class CountryProperties(TypedDict):
    """A country.

    References:
        https://schema.org/Country
    Note:
        Model Depth 4
    Attributes:
    """


class CountryAllProperties(CountryInheritedProperties, CountryProperties, TypedDict):
    pass


class CountryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Country", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CountryProperties, CountryInheritedProperties, CountryAllProperties
    ] = CountryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Country"
    return model


Country = create_schema_org_model()


def create_country_model(
    model: Union[CountryProperties, CountryInheritedProperties, CountryAllProperties]
):
    _type = deepcopy(CountryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Country. Please see: https://schema.org/Country"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CountryAllProperties):
    pydantic_type = create_country_model(model=model)
    return pydantic_type(model).schema_json()
