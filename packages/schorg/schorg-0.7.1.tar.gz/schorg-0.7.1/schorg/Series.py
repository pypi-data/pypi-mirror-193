"""
A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].

https://schema.org/Series
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SeriesInheritedProperties(TypedDict):
    """A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].

    References:
        https://schema.org/Series
    Note:
        Model Depth 3
    Attributes:
    """

    


class SeriesProperties(TypedDict):
    """A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].

    References:
        https://schema.org/Series
    Note:
        Model Depth 3
    Attributes:
    """

    


class AllProperties(SeriesInheritedProperties , SeriesProperties, TypedDict):
    pass


class SeriesBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Series",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SeriesProperties, SeriesInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Series"
    return model
    

Series = create_schema_org_model()


def create_series_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_series_model(model=model)
    return pydantic_type(model).schema_json()


