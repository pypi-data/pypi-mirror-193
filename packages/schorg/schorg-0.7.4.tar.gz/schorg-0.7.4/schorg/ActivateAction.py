"""
The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).

https://schema.org/ActivateAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActivateActionInheritedProperties(TypedDict):
    """The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).

    References:
        https://schema.org/ActivateAction
    Note:
        Model Depth 4
    Attributes:
    """


class ActivateActionProperties(TypedDict):
    """The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).

    References:
        https://schema.org/ActivateAction
    Note:
        Model Depth 4
    Attributes:
    """


class ActivateActionAllProperties(
    ActivateActionInheritedProperties, ActivateActionProperties, TypedDict
):
    pass


class ActivateActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ActivateAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ActivateActionProperties,
        ActivateActionInheritedProperties,
        ActivateActionAllProperties,
    ] = ActivateActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActivateAction"
    return model


ActivateAction = create_schema_org_model()


def create_activateaction_model(
    model: Union[
        ActivateActionProperties,
        ActivateActionInheritedProperties,
        ActivateActionAllProperties,
    ]
):
    _type = deepcopy(ActivateActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ActivateActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ActivateActionAllProperties):
    pydantic_type = create_activateaction_model(model=model)
    return pydantic_type(model).schema_json()
