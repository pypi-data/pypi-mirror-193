"""
A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).

https://schema.org/Date
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class DateAllProperties(DateInheritedProperties, DateProperties, TypedDict):
    pass


class DateBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Date", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DateProperties, DateInheritedProperties, DateAllProperties
    ] = DateAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Date"
    return model


Date = create_schema_org_model()


def create_date_model(
    model: Union[DateProperties, DateInheritedProperties, DateAllProperties]
):
    _type = deepcopy(DateAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DateAllProperties):
    pydantic_type = create_date_model(model=model)
    return pydantic_type(model).schema_json()
