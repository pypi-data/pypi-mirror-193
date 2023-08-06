"""
A movie rental store.

https://schema.org/MovieRentalStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MovieRentalStoreInheritedProperties(TypedDict):
    """A movie rental store.

    References:
        https://schema.org/MovieRentalStore
    Note:
        Model Depth 5
    Attributes:
    """


class MovieRentalStoreProperties(TypedDict):
    """A movie rental store.

    References:
        https://schema.org/MovieRentalStore
    Note:
        Model Depth 5
    Attributes:
    """


class MovieRentalStoreAllProperties(
    MovieRentalStoreInheritedProperties, MovieRentalStoreProperties, TypedDict
):
    pass


class MovieRentalStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MovieRentalStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MovieRentalStoreProperties,
        MovieRentalStoreInheritedProperties,
        MovieRentalStoreAllProperties,
    ] = MovieRentalStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MovieRentalStore"
    return model


MovieRentalStore = create_schema_org_model()


def create_movierentalstore_model(
    model: Union[
        MovieRentalStoreProperties,
        MovieRentalStoreInheritedProperties,
        MovieRentalStoreAllProperties,
    ]
):
    _type = deepcopy(MovieRentalStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MovieRentalStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MovieRentalStoreAllProperties):
    pydantic_type = create_movierentalstore_model(model=model)
    return pydantic_type(model).schema_json()
