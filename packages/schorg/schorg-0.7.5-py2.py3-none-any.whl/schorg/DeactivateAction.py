"""
The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).

https://schema.org/DeactivateAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DeactivateActionInheritedProperties(TypedDict):
    """The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).

    References:
        https://schema.org/DeactivateAction
    Note:
        Model Depth 4
    Attributes:
    """


class DeactivateActionProperties(TypedDict):
    """The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).

    References:
        https://schema.org/DeactivateAction
    Note:
        Model Depth 4
    Attributes:
    """


class DeactivateActionAllProperties(
    DeactivateActionInheritedProperties, DeactivateActionProperties, TypedDict
):
    pass


class DeactivateActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DeactivateAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DeactivateActionProperties,
        DeactivateActionInheritedProperties,
        DeactivateActionAllProperties,
    ] = DeactivateActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DeactivateAction"
    return model


DeactivateAction = create_schema_org_model()


def create_deactivateaction_model(
    model: Union[
        DeactivateActionProperties,
        DeactivateActionInheritedProperties,
        DeactivateActionAllProperties,
    ]
):
    _type = deepcopy(DeactivateActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DeactivateAction. Please see: https://schema.org/DeactivateAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DeactivateActionAllProperties):
    pydantic_type = create_deactivateaction_model(model=model)
    return pydantic_type(model).schema_json()
