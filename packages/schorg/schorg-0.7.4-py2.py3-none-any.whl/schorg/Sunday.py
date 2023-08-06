"""
The day of the week between Saturday and Monday.

https://schema.org/Sunday
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SundayInheritedProperties(TypedDict):
    """The day of the week between Saturday and Monday.

    References:
        https://schema.org/Sunday
    Note:
        Model Depth 5
    Attributes:
    """


class SundayProperties(TypedDict):
    """The day of the week between Saturday and Monday.

    References:
        https://schema.org/Sunday
    Note:
        Model Depth 5
    Attributes:
    """


class SundayAllProperties(SundayInheritedProperties, SundayProperties, TypedDict):
    pass


class SundayBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Sunday", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SundayProperties, SundayInheritedProperties, SundayAllProperties
    ] = SundayAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Sunday"
    return model


Sunday = create_schema_org_model()


def create_sunday_model(
    model: Union[SundayProperties, SundayInheritedProperties, SundayAllProperties]
):
    _type = deepcopy(SundayAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SundayAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SundayAllProperties):
    pydantic_type = create_sunday_model(model=model)
    return pydantic_type(model).schema_json()
