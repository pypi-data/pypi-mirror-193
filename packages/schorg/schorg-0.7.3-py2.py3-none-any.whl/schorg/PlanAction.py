"""
The act of planning the execution of an event/task/action/reservation/plan to a future date.

https://schema.org/PlanAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PlanActionInheritedProperties(TypedDict):
    """The act of planning the execution of an event/task/action/reservation/plan to a future date.

    References:
        https://schema.org/PlanAction
    Note:
        Model Depth 4
    Attributes:
    """


class PlanActionProperties(TypedDict):
    """The act of planning the execution of an event/task/action/reservation/plan to a future date.

    References:
        https://schema.org/PlanAction
    Note:
        Model Depth 4
    Attributes:
        scheduledTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The time the object is scheduled to.
    """

    scheduledTime: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]


class PlanActionAllProperties(
    PlanActionInheritedProperties, PlanActionProperties, TypedDict
):
    pass


class PlanActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PlanAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"scheduledTime": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PlanActionProperties, PlanActionInheritedProperties, PlanActionAllProperties
    ] = PlanActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PlanAction"
    return model


PlanAction = create_schema_org_model()


def create_planaction_model(
    model: Union[
        PlanActionProperties, PlanActionInheritedProperties, PlanActionAllProperties
    ]
):
    _type = deepcopy(PlanActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PlanActionAllProperties):
    pydantic_type = create_planaction_model(model=model)
    return pydantic_type(model).schema_json()
