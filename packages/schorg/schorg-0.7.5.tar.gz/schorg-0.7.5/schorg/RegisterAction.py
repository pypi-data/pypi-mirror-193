"""
The act of registering to be a user of a service, product or web page.Related actions:* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.* [[FollowAction]]: Unlike FollowAction, RegisterAction doesn't imply that the agent is expecting to poll for updates from the object.* [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn't imply that the agent is expecting updates from the object.

https://schema.org/RegisterAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RegisterActionInheritedProperties(TypedDict):
    """The act of registering to be a user of a service, product or web page.Related actions:* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.* [[FollowAction]]: Unlike FollowAction, RegisterAction doesn't imply that the agent is expecting to poll for updates from the object.* [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn't imply that the agent is expecting updates from the object.

    References:
        https://schema.org/RegisterAction
    Note:
        Model Depth 4
    Attributes:
    """


class RegisterActionProperties(TypedDict):
    """The act of registering to be a user of a service, product or web page.Related actions:* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.* [[FollowAction]]: Unlike FollowAction, RegisterAction doesn't imply that the agent is expecting to poll for updates from the object.* [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn't imply that the agent is expecting updates from the object.

    References:
        https://schema.org/RegisterAction
    Note:
        Model Depth 4
    Attributes:
    """


class RegisterActionAllProperties(
    RegisterActionInheritedProperties, RegisterActionProperties, TypedDict
):
    pass


class RegisterActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RegisterAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RegisterActionProperties,
        RegisterActionInheritedProperties,
        RegisterActionAllProperties,
    ] = RegisterActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RegisterAction"
    return model


RegisterAction = create_schema_org_model()


def create_registeraction_model(
    model: Union[
        RegisterActionProperties,
        RegisterActionInheritedProperties,
        RegisterActionAllProperties,
    ]
):
    _type = deepcopy(RegisterActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of RegisterAction. Please see: https://schema.org/RegisterAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: RegisterActionAllProperties):
    pydantic_type = create_registeraction_model(model=model)
    return pydantic_type(model).schema_json()
