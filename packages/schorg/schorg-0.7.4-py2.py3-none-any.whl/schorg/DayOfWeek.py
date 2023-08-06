"""
The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.Originally, URLs from [GoodRelations](http://purl.org/goodrelations/v1) were used (for [[Monday]], [[Tuesday]], [[Wednesday]], [[Thursday]], [[Friday]], [[Saturday]], [[Sunday]] plus a special entry for [[PublicHolidays]]); these have now been integrated directly into schema.org.      

https://schema.org/DayOfWeek
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DayOfWeekInheritedProperties(TypedDict):
    """The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.Originally, URLs from [GoodRelations](http://purl.org/goodrelations/v1) were used (for [[Monday]], [[Tuesday]], [[Wednesday]], [[Thursday]], [[Friday]], [[Saturday]], [[Sunday]] plus a special entry for [[PublicHolidays]]); these have now been integrated directly into schema.org.

    References:
        https://schema.org/DayOfWeek
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class DayOfWeekProperties(TypedDict):
    """The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.Originally, URLs from [GoodRelations](http://purl.org/goodrelations/v1) were used (for [[Monday]], [[Tuesday]], [[Wednesday]], [[Thursday]], [[Friday]], [[Saturday]], [[Sunday]] plus a special entry for [[PublicHolidays]]); these have now been integrated directly into schema.org.

    References:
        https://schema.org/DayOfWeek
    Note:
        Model Depth 4
    Attributes:
    """


class DayOfWeekAllProperties(
    DayOfWeekInheritedProperties, DayOfWeekProperties, TypedDict
):
    pass


class DayOfWeekBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DayOfWeek", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DayOfWeekProperties, DayOfWeekInheritedProperties, DayOfWeekAllProperties
    ] = DayOfWeekAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DayOfWeek"
    return model


DayOfWeek = create_schema_org_model()


def create_dayofweek_model(
    model: Union[
        DayOfWeekProperties, DayOfWeekInheritedProperties, DayOfWeekAllProperties
    ]
):
    _type = deepcopy(DayOfWeekAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DayOfWeekAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DayOfWeekAllProperties):
    pydantic_type = create_dayofweek_model(model=model)
    return pydantic_type(model).schema_json()
