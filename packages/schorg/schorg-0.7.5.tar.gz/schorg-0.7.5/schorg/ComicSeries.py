"""
A sequential publication of comic stories under a    	unifying title, for example "The Amazing Spider-Man" or "Groo the    	Wanderer".

https://schema.org/ComicSeries
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComicSeriesInheritedProperties(TypedDict):
    """A sequential publication of comic stories under a    	unifying title, for example "The Amazing Spider-Man" or "Groo the    	Wanderer".

    References:
        https://schema.org/ComicSeries
    Note:
        Model Depth 5
    Attributes:
    """


class ComicSeriesProperties(TypedDict):
    """A sequential publication of comic stories under a    	unifying title, for example "The Amazing Spider-Man" or "Groo the    	Wanderer".

    References:
        https://schema.org/ComicSeries
    Note:
        Model Depth 5
    Attributes:
    """


class ComicSeriesAllProperties(
    ComicSeriesInheritedProperties, ComicSeriesProperties, TypedDict
):
    pass


class ComicSeriesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ComicSeries", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ComicSeriesProperties, ComicSeriesInheritedProperties, ComicSeriesAllProperties
    ] = ComicSeriesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComicSeries"
    return model


ComicSeries = create_schema_org_model()


def create_comicseries_model(
    model: Union[
        ComicSeriesProperties, ComicSeriesInheritedProperties, ComicSeriesAllProperties
    ]
):
    _type = deepcopy(ComicSeriesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ComicSeries. Please see: https://schema.org/ComicSeries"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ComicSeriesAllProperties):
    pydantic_type = create_comicseries_model(model=model)
    return pydantic_type(model).schema_json()
