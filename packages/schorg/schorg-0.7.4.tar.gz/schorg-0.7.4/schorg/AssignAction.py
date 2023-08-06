"""
The act of allocating an action/event/task to some destination (someone or something).

https://schema.org/AssignAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AssignActionInheritedProperties(TypedDict):
    """The act of allocating an action/event/task to some destination (someone or something).

    References:
        https://schema.org/AssignAction
    Note:
        Model Depth 5
    Attributes:
    """


class AssignActionProperties(TypedDict):
    """The act of allocating an action/event/task to some destination (someone or something).

    References:
        https://schema.org/AssignAction
    Note:
        Model Depth 5
    Attributes:
    """


class AssignActionAllProperties(
    AssignActionInheritedProperties, AssignActionProperties, TypedDict
):
    pass


class AssignActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AssignAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AssignActionProperties,
        AssignActionInheritedProperties,
        AssignActionAllProperties,
    ] = AssignActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AssignAction"
    return model


AssignAction = create_schema_org_model()


def create_assignaction_model(
    model: Union[
        AssignActionProperties,
        AssignActionInheritedProperties,
        AssignActionAllProperties,
    ]
):
    _type = deepcopy(AssignActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AssignActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AssignActionAllProperties):
    pydantic_type = create_assignaction_model(model=model)
    return pydantic_type(model).schema_json()
