"""
The boolean value false.

https://schema.org/False
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class False_InheritedProperties(TypedDict):
    """The boolean value false.

    References:
        https://schema.org/False
    Note:
        Model Depth 6
    Attributes:
    """


class False_Properties(TypedDict):
    """The boolean value false.

    References:
        https://schema.org/False
    Note:
        Model Depth 6
    Attributes:
    """


class False_AllProperties(False_InheritedProperties, False_Properties, TypedDict):
    pass


class False_BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="False_", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        False_Properties, False_InheritedProperties, False_AllProperties
    ] = False_AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "False_"
    return model


False_ = create_schema_org_model()


def create_false__model(
    model: Union[False_Properties, False_InheritedProperties, False_AllProperties]
):
    _type = deepcopy(False_AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of False_AllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: False_AllProperties):
    pydantic_type = create_false__model(model=model)
    return pydantic_type(model).schema_json()
