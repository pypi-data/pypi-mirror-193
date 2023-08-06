"""
The day of the week between Monday and Wednesday.

https://schema.org/Tuesday
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TuesdayInheritedProperties(TypedDict):
    """The day of the week between Monday and Wednesday.

    References:
        https://schema.org/Tuesday
    Note:
        Model Depth 5
    Attributes:
    """


class TuesdayProperties(TypedDict):
    """The day of the week between Monday and Wednesday.

    References:
        https://schema.org/Tuesday
    Note:
        Model Depth 5
    Attributes:
    """


class TuesdayAllProperties(TuesdayInheritedProperties, TuesdayProperties, TypedDict):
    pass


class TuesdayBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Tuesday", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TuesdayProperties, TuesdayInheritedProperties, TuesdayAllProperties
    ] = TuesdayAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Tuesday"
    return model


Tuesday = create_schema_org_model()


def create_tuesday_model(
    model: Union[TuesdayProperties, TuesdayInheritedProperties, TuesdayAllProperties]
):
    _type = deepcopy(TuesdayAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Tuesday. Please see: https://schema.org/Tuesday"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TuesdayAllProperties):
    pydantic_type = create_tuesday_model(model=model)
    return pydantic_type(model).schema_json()
