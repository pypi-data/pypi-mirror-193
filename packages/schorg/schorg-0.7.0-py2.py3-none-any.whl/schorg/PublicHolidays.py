"""
This stands for any day that is a public holiday; it is a placeholder for all official public holidays in some particular location. While not technically a "day of the week", it can be used with [[OpeningHoursSpecification]]. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs.

https://schema.org/PublicHolidays
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(PublicHolidaysInheritedProperties , PublicHolidaysProperties, TypedDict):
    pass


class PublicHolidaysBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PublicHolidays",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PublicHolidaysProperties, PublicHolidaysInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PublicHolidays"
    return model
    

PublicHolidays = create_schema_org_model()


def create_publicholidays_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_publicholidays_model(model=model)
    return pydantic_type(model).schema_json()


