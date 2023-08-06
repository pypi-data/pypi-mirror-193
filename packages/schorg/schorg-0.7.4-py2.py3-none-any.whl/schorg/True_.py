"""
The boolean value true.

https://schema.org/True
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class True_InheritedProperties(TypedDict):
    """The boolean value true.

    References:
        https://schema.org/True
    Note:
        Model Depth 6
    Attributes:
    """


class True_Properties(TypedDict):
    """The boolean value true.

    References:
        https://schema.org/True
    Note:
        Model Depth 6
    Attributes:
    """


class True_AllProperties(True_InheritedProperties, True_Properties, TypedDict):
    pass


class True_BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="True_", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        True_Properties, True_InheritedProperties, True_AllProperties
    ] = True_AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "True_"
    return model


True_ = create_schema_org_model()


def create_true__model(
    model: Union[True_Properties, True_InheritedProperties, True_AllProperties]
):
    _type = deepcopy(True_AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of True_AllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: True_AllProperties):
    pydantic_type = create_true__model(model=model)
    return pydantic_type(model).schema_json()
