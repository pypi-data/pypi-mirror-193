"""
The day of the week between Sunday and Tuesday.

https://schema.org/Monday
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MondayInheritedProperties(TypedDict):
    """The day of the week between Sunday and Tuesday.

    References:
        https://schema.org/Monday
    Note:
        Model Depth 5
    Attributes:
    """


class MondayProperties(TypedDict):
    """The day of the week between Sunday and Tuesday.

    References:
        https://schema.org/Monday
    Note:
        Model Depth 5
    Attributes:
    """


class MondayAllProperties(MondayInheritedProperties, MondayProperties, TypedDict):
    pass


class MondayBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Monday", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MondayProperties, MondayInheritedProperties, MondayAllProperties
    ] = MondayAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Monday"
    return model


Monday = create_schema_org_model()


def create_monday_model(
    model: Union[MondayProperties, MondayInheritedProperties, MondayAllProperties]
):
    _type = deepcopy(MondayAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MondayAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MondayAllProperties):
    pydantic_type = create_monday_model(model=model)
    return pydantic_type(model).schema_json()
