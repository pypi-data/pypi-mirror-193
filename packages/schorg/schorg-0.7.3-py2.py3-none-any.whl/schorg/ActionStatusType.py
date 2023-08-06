"""
The status of an Action.

https://schema.org/ActionStatusType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActionStatusTypeInheritedProperties(TypedDict):
    """The status of an Action.

    References:
        https://schema.org/ActionStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class ActionStatusTypeProperties(TypedDict):
    """The status of an Action.

    References:
        https://schema.org/ActionStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class ActionStatusTypeAllProperties(
    ActionStatusTypeInheritedProperties, ActionStatusTypeProperties, TypedDict
):
    pass


class ActionStatusTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ActionStatusType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ActionStatusTypeProperties,
        ActionStatusTypeInheritedProperties,
        ActionStatusTypeAllProperties,
    ] = ActionStatusTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActionStatusType"
    return model


ActionStatusType = create_schema_org_model()


def create_actionstatustype_model(
    model: Union[
        ActionStatusTypeProperties,
        ActionStatusTypeInheritedProperties,
        ActionStatusTypeAllProperties,
    ]
):
    _type = deepcopy(ActionStatusTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ActionStatusTypeAllProperties):
    pydantic_type = create_actionstatustype_model(model=model)
    return pydantic_type(model).schema_json()
