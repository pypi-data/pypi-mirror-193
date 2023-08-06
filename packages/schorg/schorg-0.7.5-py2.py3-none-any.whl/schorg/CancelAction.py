"""
The act of asserting that a future event/action is no longer going to happen.Related actions:* [[ConfirmAction]]: The antonym of CancelAction.

https://schema.org/CancelAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CancelActionInheritedProperties(TypedDict):
    """The act of asserting that a future event/action is no longer going to happen.Related actions:* [[ConfirmAction]]: The antonym of CancelAction.

    References:
        https://schema.org/CancelAction
    Note:
        Model Depth 5
    Attributes:
        scheduledTime: (Optional[Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]]): The time the object is scheduled to.
    """

    scheduledTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]
    ]


class CancelActionProperties(TypedDict):
    """The act of asserting that a future event/action is no longer going to happen.Related actions:* [[ConfirmAction]]: The antonym of CancelAction.

    References:
        https://schema.org/CancelAction
    Note:
        Model Depth 5
    Attributes:
    """


class CancelActionAllProperties(
    CancelActionInheritedProperties, CancelActionProperties, TypedDict
):
    pass


class CancelActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CancelAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"scheduledTime": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CancelActionProperties,
        CancelActionInheritedProperties,
        CancelActionAllProperties,
    ] = CancelActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CancelAction"
    return model


CancelAction = create_schema_org_model()


def create_cancelaction_model(
    model: Union[
        CancelActionProperties,
        CancelActionInheritedProperties,
        CancelActionAllProperties,
    ]
):
    _type = deepcopy(CancelActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CancelAction. Please see: https://schema.org/CancelAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CancelActionAllProperties):
    pydantic_type = create_cancelaction_model(model=model)
    return pydantic_type(model).schema_json()
