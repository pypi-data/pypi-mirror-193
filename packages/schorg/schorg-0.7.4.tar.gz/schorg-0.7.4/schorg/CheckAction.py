"""
An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.

https://schema.org/CheckAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CheckActionInheritedProperties(TypedDict):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.

    References:
        https://schema.org/CheckAction
    Note:
        Model Depth 4
    Attributes:
    """


class CheckActionProperties(TypedDict):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.

    References:
        https://schema.org/CheckAction
    Note:
        Model Depth 4
    Attributes:
    """


class CheckActionAllProperties(
    CheckActionInheritedProperties, CheckActionProperties, TypedDict
):
    pass


class CheckActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CheckAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CheckActionProperties, CheckActionInheritedProperties, CheckActionAllProperties
    ] = CheckActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CheckAction"
    return model


CheckAction = create_schema_org_model()


def create_checkaction_model(
    model: Union[
        CheckActionProperties, CheckActionInheritedProperties, CheckActionAllProperties
    ]
):
    _type = deepcopy(CheckActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CheckActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CheckActionAllProperties):
    pydantic_type = create_checkaction_model(model=model)
    return pydantic_type(model).schema_json()
