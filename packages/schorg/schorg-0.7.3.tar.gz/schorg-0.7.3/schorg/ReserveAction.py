"""
Reserving a concrete object.Related actions:* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

https://schema.org/ReserveAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReserveActionInheritedProperties(TypedDict):
    """Reserving a concrete object.Related actions:* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

    References:
        https://schema.org/ReserveAction
    Note:
        Model Depth 5
    Attributes:
        scheduledTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The time the object is scheduled to.
    """

    scheduledTime: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]


class ReserveActionProperties(TypedDict):
    """Reserving a concrete object.Related actions:* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

    References:
        https://schema.org/ReserveAction
    Note:
        Model Depth 5
    Attributes:
    """


class ReserveActionAllProperties(
    ReserveActionInheritedProperties, ReserveActionProperties, TypedDict
):
    pass


class ReserveActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReserveAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"scheduledTime": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReserveActionProperties,
        ReserveActionInheritedProperties,
        ReserveActionAllProperties,
    ] = ReserveActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReserveAction"
    return model


ReserveAction = create_schema_org_model()


def create_reserveaction_model(
    model: Union[
        ReserveActionProperties,
        ReserveActionInheritedProperties,
        ReserveActionAllProperties,
    ]
):
    _type = deepcopy(ReserveActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReserveActionAllProperties):
    pydantic_type = create_reserveaction_model(model=model)
    return pydantic_type(model).schema_json()
