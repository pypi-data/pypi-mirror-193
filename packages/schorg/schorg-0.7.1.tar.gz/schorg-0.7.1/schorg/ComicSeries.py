"""
A sequential publication of comic stories under a    	unifying title, for example "The Amazing Spider-Man" or "Groo the    	Wanderer".

https://schema.org/ComicSeries
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ComicSeriesInheritedProperties , ComicSeriesProperties, TypedDict):
    pass


class ComicSeriesBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ComicSeries",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ComicSeriesProperties, ComicSeriesInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComicSeries"
    return model
    

ComicSeries = create_schema_org_model()


def create_comicseries_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_comicseries_model(model=model)
    return pydantic_type(model).schema_json()


