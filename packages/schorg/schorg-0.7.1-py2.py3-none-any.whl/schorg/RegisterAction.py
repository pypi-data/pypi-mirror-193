"""
The act of registering to be a user of a service, product or web page.Related actions:* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.* [[FollowAction]]: Unlike FollowAction, RegisterAction doesn't imply that the agent is expecting to poll for updates from the object.* [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn't imply that the agent is expecting updates from the object.

https://schema.org/RegisterAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(RegisterActionInheritedProperties , RegisterActionProperties, TypedDict):
    pass


class RegisterActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RegisterAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RegisterActionProperties, RegisterActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RegisterAction"
    return model
    

RegisterAction = create_schema_org_model()


def create_registeraction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_registeraction_model(model=model)
    return pydantic_type(model).schema_json()


