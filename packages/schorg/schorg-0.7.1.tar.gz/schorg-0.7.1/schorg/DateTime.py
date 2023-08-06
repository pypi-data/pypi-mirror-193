"""
A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).

https://schema.org/DateTime
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DateTimeInheritedProperties(TypedDict):
    """A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).

    References:
        https://schema.org/DateTime
    Note:
        Model Depth 5
    Attributes:
    """

    


class DateTimeProperties(TypedDict):
    """A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).

    References:
        https://schema.org/DateTime
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DateTimeInheritedProperties , DateTimeProperties, TypedDict):
    pass


class DateTimeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DateTime",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DateTimeProperties, DateTimeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DateTime"
    return model
    

DateTime = create_schema_org_model()


def create_datetime_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_datetime_model(model=model)
    return pydantic_type(model).schema_json()


