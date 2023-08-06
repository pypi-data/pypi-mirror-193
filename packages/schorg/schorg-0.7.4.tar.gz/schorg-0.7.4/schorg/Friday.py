"""
The day of the week between Thursday and Saturday.

https://schema.org/Friday
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FridayInheritedProperties(TypedDict):
    """The day of the week between Thursday and Saturday.

    References:
        https://schema.org/Friday
    Note:
        Model Depth 5
    Attributes:
    """


class FridayProperties(TypedDict):
    """The day of the week between Thursday and Saturday.

    References:
        https://schema.org/Friday
    Note:
        Model Depth 5
    Attributes:
    """


class FridayAllProperties(FridayInheritedProperties, FridayProperties, TypedDict):
    pass


class FridayBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Friday", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FridayProperties, FridayInheritedProperties, FridayAllProperties
    ] = FridayAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Friday"
    return model


Friday = create_schema_org_model()


def create_friday_model(
    model: Union[FridayProperties, FridayInheritedProperties, FridayAllProperties]
):
    _type = deepcopy(FridayAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FridayAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FridayAllProperties):
    pydantic_type = create_friday_model(model=model)
    return pydantic_type(model).schema_json()
