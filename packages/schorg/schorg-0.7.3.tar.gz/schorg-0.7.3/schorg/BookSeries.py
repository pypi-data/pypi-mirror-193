"""
A series of books. Included books can be indicated with the hasPart property.

https://schema.org/BookSeries
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BookSeriesInheritedProperties(TypedDict):
    """A series of books. Included books can be indicated with the hasPart property.

    References:
        https://schema.org/BookSeries
    Note:
        Model Depth 4
    Attributes:
        issn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        startDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    issn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]


class BookSeriesProperties(TypedDict):
    """A series of books. Included books can be indicated with the hasPart property.

    References:
        https://schema.org/BookSeries
    Note:
        Model Depth 4
    Attributes:
    """


class BookSeriesAllProperties(
    BookSeriesInheritedProperties, BookSeriesProperties, TypedDict
):
    pass


class BookSeriesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BookSeries", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"issn": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BookSeriesProperties, BookSeriesInheritedProperties, BookSeriesAllProperties
    ] = BookSeriesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BookSeries"
    return model


BookSeries = create_schema_org_model()


def create_bookseries_model(
    model: Union[
        BookSeriesProperties, BookSeriesInheritedProperties, BookSeriesAllProperties
    ]
):
    _type = deepcopy(BookSeriesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BookSeriesAllProperties):
    pydantic_type = create_bookseries_model(model=model)
    return pydantic_type(model).schema_json()
