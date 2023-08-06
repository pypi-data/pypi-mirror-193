"""
The act of notifying someone that a future event/action is going to happen as expected.Related actions:* [[CancelAction]]: The antonym of ConfirmAction.

https://schema.org/ConfirmAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ConfirmActionInheritedProperties(TypedDict):
    """The act of notifying someone that a future event/action is going to happen as expected.Related actions:* [[CancelAction]]: The antonym of ConfirmAction.

    References:
        https://schema.org/ConfirmAction
    Note:
        Model Depth 6
    Attributes:
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
    """

    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ConfirmActionProperties(TypedDict):
    """The act of notifying someone that a future event/action is going to happen as expected.Related actions:* [[CancelAction]]: The antonym of ConfirmAction.

    References:
        https://schema.org/ConfirmAction
    Note:
        Model Depth 6
    Attributes:
    """


class ConfirmActionAllProperties(
    ConfirmActionInheritedProperties, ConfirmActionProperties, TypedDict
):
    pass


class ConfirmActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ConfirmAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"event": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ConfirmActionProperties,
        ConfirmActionInheritedProperties,
        ConfirmActionAllProperties,
    ] = ConfirmActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ConfirmAction"
    return model


ConfirmAction = create_schema_org_model()


def create_confirmaction_model(
    model: Union[
        ConfirmActionProperties,
        ConfirmActionInheritedProperties,
        ConfirmActionAllProperties,
    ]
):
    _type = deepcopy(ConfirmActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ConfirmActionAllProperties):
    pydantic_type = create_confirmaction_model(model=model)
    return pydantic_type(model).schema_json()
