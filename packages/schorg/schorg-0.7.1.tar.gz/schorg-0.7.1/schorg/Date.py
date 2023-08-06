"""
A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).

https://schema.org/Date
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DateInheritedProperties(TypedDict):
    """A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).

    References:
        https://schema.org/Date
    Note:
        Model Depth 5
    Attributes:
    """

    


class DateProperties(TypedDict):
    """A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).

    References:
        https://schema.org/Date
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DateInheritedProperties , DateProperties, TypedDict):
    pass


class DateBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Date",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DateProperties, DateInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Date"
    return model
    

Date = create_schema_org_model()


def create_date_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_date_model(model=model)
    return pydantic_type(model).schema_json()


