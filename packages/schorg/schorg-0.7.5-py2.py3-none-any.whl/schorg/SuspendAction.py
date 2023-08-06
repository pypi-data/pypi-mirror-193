"""
The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).

https://schema.org/SuspendAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SuspendActionInheritedProperties(TypedDict):
    """The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).

    References:
        https://schema.org/SuspendAction
    Note:
        Model Depth 4
    Attributes:
    """


class SuspendActionProperties(TypedDict):
    """The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).

    References:
        https://schema.org/SuspendAction
    Note:
        Model Depth 4
    Attributes:
    """


class SuspendActionAllProperties(
    SuspendActionInheritedProperties, SuspendActionProperties, TypedDict
):
    pass


class SuspendActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SuspendAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SuspendActionProperties,
        SuspendActionInheritedProperties,
        SuspendActionAllProperties,
    ] = SuspendActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SuspendAction"
    return model


SuspendAction = create_schema_org_model()


def create_suspendaction_model(
    model: Union[
        SuspendActionProperties,
        SuspendActionInheritedProperties,
        SuspendActionAllProperties,
    ]
):
    _type = deepcopy(SuspendActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SuspendAction. Please see: https://schema.org/SuspendAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SuspendActionAllProperties):
    pydantic_type = create_suspendaction_model(model=model)
    return pydantic_type(model).schema_json()
