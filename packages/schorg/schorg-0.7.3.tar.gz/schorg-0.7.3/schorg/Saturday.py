"""
The day of the week between Friday and Sunday.

https://schema.org/Saturday
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SaturdayInheritedProperties(TypedDict):
    """The day of the week between Friday and Sunday.

    References:
        https://schema.org/Saturday
    Note:
        Model Depth 5
    Attributes:
    """


class SaturdayProperties(TypedDict):
    """The day of the week between Friday and Sunday.

    References:
        https://schema.org/Saturday
    Note:
        Model Depth 5
    Attributes:
    """


class SaturdayAllProperties(SaturdayInheritedProperties, SaturdayProperties, TypedDict):
    pass


class SaturdayBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Saturday", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SaturdayProperties, SaturdayInheritedProperties, SaturdayAllProperties
    ] = SaturdayAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Saturday"
    return model


Saturday = create_schema_org_model()


def create_saturday_model(
    model: Union[SaturdayProperties, SaturdayInheritedProperties, SaturdayAllProperties]
):
    _type = deepcopy(SaturdayAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SaturdayAllProperties):
    pydantic_type = create_saturday_model(model=model)
    return pydantic_type(model).schema_json()
