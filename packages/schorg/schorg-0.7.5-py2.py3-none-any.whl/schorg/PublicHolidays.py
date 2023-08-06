"""
This stands for any day that is a public holiday; it is a placeholder for all official public holidays in some particular location. While not technically a "day of the week", it can be used with [[OpeningHoursSpecification]]. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs.

https://schema.org/PublicHolidays
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PublicHolidaysInheritedProperties(TypedDict):
    """This stands for any day that is a public holiday; it is a placeholder for all official public holidays in some particular location. While not technically a "day of the week", it can be used with [[OpeningHoursSpecification]]. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs.

    References:
        https://schema.org/PublicHolidays
    Note:
        Model Depth 5
    Attributes:
    """


class PublicHolidaysProperties(TypedDict):
    """This stands for any day that is a public holiday; it is a placeholder for all official public holidays in some particular location. While not technically a "day of the week", it can be used with [[OpeningHoursSpecification]]. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs.

    References:
        https://schema.org/PublicHolidays
    Note:
        Model Depth 5
    Attributes:
    """


class PublicHolidaysAllProperties(
    PublicHolidaysInheritedProperties, PublicHolidaysProperties, TypedDict
):
    pass


class PublicHolidaysBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PublicHolidays", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PublicHolidaysProperties,
        PublicHolidaysInheritedProperties,
        PublicHolidaysAllProperties,
    ] = PublicHolidaysAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PublicHolidays"
    return model


PublicHolidays = create_schema_org_model()


def create_publicholidays_model(
    model: Union[
        PublicHolidaysProperties,
        PublicHolidaysInheritedProperties,
        PublicHolidaysAllProperties,
    ]
):
    _type = deepcopy(PublicHolidaysAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PublicHolidays. Please see: https://schema.org/PublicHolidays"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PublicHolidaysAllProperties):
    pydantic_type = create_publicholidays_model(model=model)
    return pydantic_type(model).schema_json()
