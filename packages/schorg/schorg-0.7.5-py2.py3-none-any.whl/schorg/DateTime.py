"""
A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).

https://schema.org/DateTime
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class DateTimeAllProperties(DateTimeInheritedProperties, DateTimeProperties, TypedDict):
    pass


class DateTimeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DateTime", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DateTimeProperties, DateTimeInheritedProperties, DateTimeAllProperties
    ] = DateTimeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DateTime"
    return model


DateTime = create_schema_org_model()


def create_datetime_model(
    model: Union[DateTimeProperties, DateTimeInheritedProperties, DateTimeAllProperties]
):
    _type = deepcopy(DateTimeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DateTime. Please see: https://schema.org/DateTime"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DateTimeAllProperties):
    pydantic_type = create_datetime_model(model=model)
    return pydantic_type(model).schema_json()
