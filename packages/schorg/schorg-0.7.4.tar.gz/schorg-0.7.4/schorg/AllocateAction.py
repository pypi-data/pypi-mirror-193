"""
The act of organizing tasks/objects/events by associating resources to it.

https://schema.org/AllocateAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AllocateActionInheritedProperties(TypedDict):
    """The act of organizing tasks/objects/events by associating resources to it.

    References:
        https://schema.org/AllocateAction
    Note:
        Model Depth 4
    Attributes:
    """


class AllocateActionProperties(TypedDict):
    """The act of organizing tasks/objects/events by associating resources to it.

    References:
        https://schema.org/AllocateAction
    Note:
        Model Depth 4
    Attributes:
    """


class AllocateActionAllProperties(
    AllocateActionInheritedProperties, AllocateActionProperties, TypedDict
):
    pass


class AllocateActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AllocateAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AllocateActionProperties,
        AllocateActionInheritedProperties,
        AllocateActionAllProperties,
    ] = AllocateActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AllocateAction"
    return model


AllocateAction = create_schema_org_model()


def create_allocateaction_model(
    model: Union[
        AllocateActionProperties,
        AllocateActionInheritedProperties,
        AllocateActionAllProperties,
    ]
):
    _type = deepcopy(AllocateActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AllocateActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllocateActionAllProperties):
    pydantic_type = create_allocateaction_model(model=model)
    return pydantic_type(model).schema_json()
