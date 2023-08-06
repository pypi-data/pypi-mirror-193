"""
A theater or other performing art center.

https://schema.org/PerformingArtsTheater
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PerformingArtsTheaterInheritedProperties(TypedDict):
    """A theater or other performing art center.

    References:
        https://schema.org/PerformingArtsTheater
    Note:
        Model Depth 4
    Attributes:
        openingHours: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. * Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>.
    """

    openingHours: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PerformingArtsTheaterProperties(TypedDict):
    """A theater or other performing art center.

    References:
        https://schema.org/PerformingArtsTheater
    Note:
        Model Depth 4
    Attributes:
    """


class PerformingArtsTheaterAllProperties(
    PerformingArtsTheaterInheritedProperties, PerformingArtsTheaterProperties, TypedDict
):
    pass


class PerformingArtsTheaterBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PerformingArtsTheater", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"openingHours": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PerformingArtsTheaterProperties,
        PerformingArtsTheaterInheritedProperties,
        PerformingArtsTheaterAllProperties,
    ] = PerformingArtsTheaterAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PerformingArtsTheater"
    return model


PerformingArtsTheater = create_schema_org_model()


def create_performingartstheater_model(
    model: Union[
        PerformingArtsTheaterProperties,
        PerformingArtsTheaterInheritedProperties,
        PerformingArtsTheaterAllProperties,
    ]
):
    _type = deepcopy(PerformingArtsTheaterAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PerformingArtsTheaterAllProperties):
    pydantic_type = create_performingartstheater_model(model=model)
    return pydantic_type(model).schema_json()
