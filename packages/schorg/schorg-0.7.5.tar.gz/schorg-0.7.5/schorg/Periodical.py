"""
A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

https://schema.org/Periodical
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PeriodicalInheritedProperties(TypedDict):
    """A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    References:
        https://schema.org/Periodical
    Note:
        Model Depth 4
    Attributes:
        issn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    issn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]


class PeriodicalProperties(TypedDict):
    """A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    References:
        https://schema.org/Periodical
    Note:
        Model Depth 4
    Attributes:
    """


class PeriodicalAllProperties(
    PeriodicalInheritedProperties, PeriodicalProperties, TypedDict
):
    pass


class PeriodicalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Periodical", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"issn": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PeriodicalProperties, PeriodicalInheritedProperties, PeriodicalAllProperties
    ] = PeriodicalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Periodical"
    return model


Periodical = create_schema_org_model()


def create_periodical_model(
    model: Union[
        PeriodicalProperties, PeriodicalInheritedProperties, PeriodicalAllProperties
    ]
):
    _type = deepcopy(PeriodicalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Periodical. Please see: https://schema.org/Periodical"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PeriodicalAllProperties):
    pydantic_type = create_periodical_model(model=model)
    return pydantic_type(model).schema_json()
